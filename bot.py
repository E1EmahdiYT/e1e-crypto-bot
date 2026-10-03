import os
import re
import json
import requests

from decimal import Decimal, InvalidOperation

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)


# =========================================================
# تنظیمات
# =========================================================

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise RuntimeError(
        "BOT_TOKEN تنظیم نشده است. "
        "توکن را در Environment Variables هاست قرار بده."
    )

CHANNEL_LINK = "https://t.me/mahdiyt1"
ADMIN_ID = 6205425637

USERS_FILE = "users.json"


# =========================================================
# نام ارزها
# =========================================================

COINS = {
    "btc": "bitcoin",
    "bitcoin": "bitcoin",
    "بیتکوین": "bitcoin",

    "eth": "ethereum",
    "ethereum": "ethereum",
    "اتریوم": "ethereum",

    "ton": "the-open-network",
    "تون": "the-open-network",

    "dogs": "dogs-2",
    "داگز": "dogs-2",

    "trx": "tron",
    "tron": "tron",
    "ترون": "tron",

    "xrp": "ripple",
    "ریپل": "ripple",

    "doge": "dogecoin",
    "dogecoin": "dogecoin",
    "دوج": "dogecoin",

    "sol": "solana",
    "solana": "solana",
    "سولانا": "solana",

    "usdt": "tether",
    "تتر": "tether",

    "ltc": "litecoin",
    "لایتکوین": "litecoin",

    "ada": "cardano",
    "کاردانو": "cardano",

    "dot": "polkadot",
    "پولکادات": "polkadot",

    "shib": "shiba-inu",
    "شیبا": "shiba-inu",

    "bnb": "binancecoin",
    "بایننس": "binancecoin",

    "avax": "avalanche-2",
    "آوالانچ": "avalanche-2",

    "matic": "matic-network",
    "پالیگان": "matic-network",

    "link": "chainlink",
    "چین‌لینک": "chainlink",
    "چین لینک": "chainlink",

    "uni": "uniswap",
    "یونی": "uniswap",

    "atom": "cosmos",
    "کازماس": "cosmos",

    "near": "near",
    "نیر": "near",

    "arb": "arbitrum",
    "آربیتروم": "arbitrum",

    "op": "optimism",
    "آپتیمیسم": "optimism",

    "apt": "aptos",
    "آپتوس": "aptos",

    "sui": "sui",
    "سوئی": "sui",

    "pepe": "pepe",
    "پیپ": "pepe",
}


# =========================================================
# تبدیل اعداد فارسی و عربی به انگلیسی
# =========================================================

def normalize_digits(text):
    table = str.maketrans(
        "۰۱۲۳۴۵۶۷۸۹٠١٢٣٤٥٦٧٨٩",
        "01234567890123456789"
    )

    return text.translate(table)


# =========================================================
# فرمت عدد
# =========================================================

def fmt(value):
    try:
        value = Decimal(str(value))

        if value == value.to_integral():
            return f"{int(value):,}"

        text = f"{value:.12f}".rstrip("0").rstrip(".")

        if "." in text:
            integer, decimal = text.split(".")
            integer = f"{int(integer):,}"
            return f"{integer}.{decimal}"

        return f"{int(value):,}"

    except Exception:
        return str(value)


# =========================================================
# دکمه کانال
# =========================================================

def channel_button():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "📢 کانال 𝑬'𝑬",
                url=CHANNEL_LINK
            )
        ]
    ])


# =========================================================
# ذخیره کاربران
# =========================================================

def load_users():
    try:
        if not os.path.exists(USERS_FILE):
            return {}

        with open(
            USERS_FILE,
            "r",
            encoding="utf-8"
        ) as file:
            return json.load(file)

    except Exception:
        return {}


def save_users(users):
    try:
        with open(
            USERS_FILE,
            "w",
            encoding="utf-8"
        ) as file:
            json.dump(
                users,
                file,
                ensure_ascii=False,
                indent=2
            )

    except Exception as e:
        print("USER SAVE ERROR:", e)


def register_user(user):
    users = load_users()

    user_id = str(user.id)

    if user_id not in users:
        users[user_id] = {
            "id": user.id,
            "username": user.username or "",
            "first_name": user.first_name or "",
        }

        save_users(users)


# =========================================================
# پیدا کردن ارز
# =========================================================

def find_coin(symbol):
    symbol = symbol.strip().lower()

    if symbol in COINS:
        return COINS[symbol]

    try:
        url = "https://api.coingecko.com/api/v3/search"

        response = requests.get(
            url,
            params={
                "query": symbol
            },
            headers={
                "User-Agent": "Mozilla/5.0"
            },
            timeout=15
        )

        if response.status_code != 200:
            return None

        data = response.json()

        coins = data.get("coins", [])

        if not coins:
            return None

        # اول دنبال نماد دقیق می‌گردیم
        for coin in coins:
            coin_symbol = coin.get(
                "symbol",
                ""
            ).lower()

            if coin_symbol == symbol:
                return coin.get("id")

        # اگر پیدا نشد، اولین نتیجه
        return coins[0].get("id")

    except Exception as e:
        print("FIND COIN ERROR:", e)
        return None


# =========================================================
# قیمت کریپتو
# =========================================================

def get_crypto_price(coin_id):
    try:
        url = (
            "https://api.coingecko.com/api/v3/"
            "simple/price"
        )

        response = requests.get(
            url,
            params={
                "ids": coin_id,
                "vs_currencies": "usd"
            },
            headers={
                "User-Agent": "Mozilla/5.0"
            },
            timeout=15
        )

        if response.status_code != 200:
            print(
                "COINGECKO STATUS:",
                response.status_code
            )
            return None

        data = response.json()

        if coin_id not in data:
            return None

        return data[coin_id].get("usd")

    except Exception as e:
        print("CRYPTO PRICE ERROR:", e)
        return None


# =========================================================
# قیمت دلار
# =========================================================

def get_dollar_toman():
    """
    قیمت دلار را از TGJU می‌گیرد.

    TGJU مقدار را به ریال ارائه می‌کند.
    برای تبدیل به تومان تقسیم بر 10 می‌شود.
    """

    try:
        # چند مسیر را امتحان می‌کنیم
        urls = [
            "https://api.tgju.org/v1/market/indicator/price_dollar_rl",
            "https://www.tgju.org/profile/price_dollar_rl",
        ]

        headers = {
            "User-Agent": (
                "Mozilla/5.0 "
                "(Linux; Android 10) "
                "AppleWebKit/537.36 "
                "Chrome/140.0 Mobile Safari/537.36"
            ),
            "Accept": "*/*",
        }

        for url in urls:

            try:
                response = requests.get(
                    url,
                    headers=headers,
                    timeout=15
                )

                if response.status_code != 200:
                    continue

                text = normalize_digits(
                    response.text
                )

                # -----------------------------------------
                # حالت JSON
                # -----------------------------------------

                try:
                    data = response.json()

                    # جستجوی بازگشتی برای پیدا کردن عدد
                    def find_number(obj):

                        if isinstance(obj, dict):

                            for key, value in obj.items():

                                key_text = str(key).lower()

                                if (
                                    "price" in key_text
                                    or "value" in key_text
                                    or "current" in key_text
                                    or "last" in key_text
                                ):
                                    if isinstance(
                                        value,
                                        (int, float, str)
                                    ):
                                        try:
                                            number = Decimal(
                                                str(value)
                                                .replace(",", "")
                                            )

                                            if number > 500000:
                                                return (
                                                    number
                                                    / Decimal("10")
                                                )

                                        except Exception:
                                            pass

                                result = find_number(value)

                                if result:
                                    return result

                        elif isinstance(obj, list):

                            for item in obj:
                                result = find_number(item)

                                if result:
                                    return result

                        return None

                    result = find_number(data)

                    if result:
                        return result

                except Exception:
                    pass

                # -----------------------------------------
                # حالت HTML
                # -----------------------------------------

                patterns = [
                    r'"price"\s*:\s*"?(.*?)"?[,}]',
                    r'"value"\s*:\s*"?(.*?)"?[,}]',
                    r'"current"\s*:\s*"?(.*?)"?[,}]',
                    r'"last"\s*:\s*"?(.*?)"?[,}]',
                    r'([0-9]{1,3}(?:[,][0-9]{3})+)',
                ]

                for pattern in patterns:

                    matches = re.findall(
                        pattern,
                        text,
                        re.IGNORECASE
                    )

                    for match in matches:

                        try:
                            number_text = (
                                str(match)
                                .replace(",", "")
                                .replace(" ", "")
                            )

                            number = Decimal(
                                number_text
                            )

                            if number > 500000:
                                return (
                                    number
                                    / Decimal("10")
                                )

                        except Exception:
                            continue

            except Exception as e:
                print(
                    "DOLLAR REQUEST ERROR:",
                    e
                )

        return None

    except Exception as e:
        print(
            "DOLLAR ERROR:",
            e
        )

        return None


# =========================================================
# محاسبه قیمت
# =========================================================

def calculate(text):
    text = normalize_digits(text)
    text = text.strip()

    # مثال:
    # 100 DOGS
    # 1 BTC
    # 0.5 TON

    pattern = (
        r"^\s*"
        r"([0-9]+(?:[.,][0-9]+)?)"
        r"\s+"
        r"([^\s]+)"
        r"\s*$"
    )

    match = re.match(
        pattern,
        text,
        re.IGNORECASE
    )

    if not match:
        return None

    quantity_text = match.group(1)
    symbol = match.group(2)

    quantity_text = quantity_text.replace(
        ",",
        "."
    )

    try:
        quantity = Decimal(
            quantity_text
        )

    except InvalidOperation:
        return None

    if quantity <= 0:
        return None

    # محدودیت منطقی برای جلوگیری از ورودی اشتباه
    if quantity > Decimal("1000000000000000"):
        return None

    coin_id = find_coin(symbol)

    if not coin_id:
        return {
            "error": "coin"
        }

    crypto_price = get_crypto_price(
        coin_id
    )

    if crypto_price is None:
        return {
            "error": "crypto"
        }

    dollar_price = get_dollar_toman()

    if dollar_price is None:
        return {
            "error": "dollar"
        }

    crypto_price = Decimal(
        str(crypto_price)
    )

    dollar_price = Decimal(
        str(dollar_price)
    )

    usd_total = (
        quantity
        * crypto_price
    )

    toman_total = (
        usd_total
        * dollar_price
    )

    return {
        "quantity": quantity,
        "symbol": symbol.upper(),
        "coin_id": coin_id,
        "crypto_price": crypto_price,
        "dollar_price": dollar_price,
        "usd_total": usd_total,
        "toman_total": toman_total,
    }


# =========================================================
# پیام شروع
# =========================================================

async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    user = update.effective_user

    if user:
        register_user(user)

    text = (
        "🪙 𝑬'𝑬 | Crypto\n\n"
        "💰 محاسبه قیمت ارز دیجیتال\n\n"
        "مثال:\n"
        "🔹 1 BTC\n"
        "🔹 100 DOGS\n"
        "🔹 0.5 TON\n"
        "🔹 1000 TRX\n\n"
        "📌 مقدار + نام ارز را ارسال کن."
    )

    await update.message.reply_text(
        text,
        reply_markup=channel_button()
    )


# =========================================================
# پیام قیمت
# =========================================================

async def handle_message(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    if not update.message:
        return

    user = update.effective_user

    if user:
        register_user(user)

    text = update.message.text

    if not text:
        return

    result = calculate(text)

    # اگر پیام مربوط به قیمت نبود
    if result is None:
        return

    # -----------------------------------------------------
    # خطاها
    # -----------------------------------------------------

    if result.get("error") == "coin":

        await update.message.reply_text(
            "❌ ارز موردنظر پیدا نشد.\n\n"
            "مثال:\n"
            "1 BTC\n"
            "100 DOGS\n"
            "0.5 TON",
            reply_markup=channel_button()
        )

        return

    if result.get("error") == "crypto":

        await update.message.reply_text(
            "❌ دریافت قیمت ارز با مشکل مواجه شد.\n"
            "لطفاً چند لحظه بعد دوباره امتحان کن.",
            reply_markup=channel_button()
        )

        return

    if result.get("error") == "dollar":

        await update.message.reply_text(
            "❌ قیمت دلار دریافت نشد.\n"
            "لطفاً چند لحظه بعد دوباره امتحان کن.",
            reply_markup=channel_button()
        )

        return

    # -----------------------------------------------------
    # اطلاعات
    # -----------------------------------------------------

    quantity = result["quantity"]
    symbol = result["symbol"]

    crypto_price = result["crypto_price"]
    dollar_price = result["dollar_price"]

    usd_total = result["usd_total"]
    toman_total = result["toman_total"]

    response = (
        "🪙 𝑬'𝑬 | Crypto\n\n"

        f"💎 مقدار: {fmt(quantity)} {symbol}\n\n"

        f"💵 قیمت هر واحد:\n"
        f"${fmt(crypto_price)}\n\n"

        f"💲 قیمت دلار:\n"
        f"{fmt(dollar_price)} تومان\n\n"

        "━━━━━━━━━━━━━━\n\n"

        f"💵 ارزش کل دلاری:\n"
        f"${fmt(usd_total)}\n\n"

        f"💰 ارزش کل:\n"
        f"{fmt(toman_total)} تومان\n\n"

        "⚡ قیمت‌ها به‌صورت آنلاین دریافت می‌شوند."
    )

    await update.message.reply_text(
        response,
        reply_markup=channel_button()
    )


# =========================================================
# پنل ادمین
# =========================================================

async def admin(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    user = update.effective_user

    if not user:
        return

    if user.id != ADMIN_ID:
        await update.message.reply_text(
            "⛔ دسترسی ندارید."
        )
        return

    keyboard = [
        [
            InlineKeyboardButton(
                "👥 کاربران",
                callback_data="admin_users"
            ),
            InlineKeyboardButton(
                "📊 آمار",
                callback_data="admin_stats"
            ),
        ]
    ]

    await update.message.reply_text(
        "🛠 پنل مدیریت 𝑬'𝑬 | Crypto\n\n"
        "یکی از گزینه‌ها را انتخاب کن:",
        reply_markup=InlineKeyboardMarkup(
            keyboard
        )
    )


# =========================================================
# دکمه‌های ادمین
# =========================================================

async def admin_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query

    await query.answer()

    user = query.from_user

    if user.id != ADMIN_ID:
        return

    users = load_users()

    if query.data == "admin_users":

        await query.edit_message_text(
            "👥 تعداد کاربران ثبت‌شده:\n\n"
            f"📌 {len(users)} نفر"
        )

    elif query.data == "admin_stats":

        await query.edit_message_text(
            "📊 آمار ربات\n\n"
            f"👥 کاربران: {len(users)}\n"
            "🟢 وضعیت: فعال"
        )


# =========================================================
# اجرای ربات
# =========================================================

def main():

    print(
        "✅ 𝑬'𝑬 | Crypto Bot Started"
    )

    app = (
        Application
        .builder()
        .token(TOKEN)
        .build()
    )

    # شروع
    app.add_handler(
        CommandHandler(
            "start",
            start
        )
    )

    # پنل ادمین
    app.add_handler(
        CommandHandler(
            "admin",
            admin
        )
    )

    # دکمه‌های ادمین
    app.add_handler(
        CallbackQueryHandler(
            admin_callback,
            pattern=r"^admin_"
        )
    )

    # پیام‌های متنی
    app.add_handler(
        MessageHandler(
            filters.TEXT
            & ~filters.COMMAND,
            handle_message
        )
    )

    app.run_polling(
        drop_pending_updates=True
    )


# =========================================================
# START
# =========================================================

if __name__ == "__main__":
    main()
