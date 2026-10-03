Welcome to Termux

Docs:       https://doc.termux.com
Community:  https://community.termux.com

Working with packages:
 - Search:  pkg search <query>
 - Install: pkg install <package>
 - Upgrade: pkg upgrade

Report issues at https://bugs.termux.com
~ $ pkg update && pkg upgrade -y
Get:1 https://termux.net stable InRelease [1089 B]
Get:2 https://termux.net stable/main aarch64 Packages [254 kB]
Fetched 255 kB in 2s (143 kB/s)
7 packages can be upgraded. Run 'apt list --upgradable' to see them.
Hit:1 https://termux.net stable InRelease
7 packages can be upgraded. Run 'apt list --upgradable' to see them.
Upgrading:
  coreutils  less     libsmartcols  util-linux
  curl       libcurl  nano

Summary:
  Upgrading: 7, Installing: 0, Removing: 0, Not Upgrading: 0
  Download size: 3320 kB
  Space needed: 135 kB

Get:1 https://termux.net stable/main aarch64 coreutils aarch64 9.11-1 [812 kB]
Get:2 https://termux.net stable/main aarch64 libcurl aarch64 8.21.0 [1015 kB]
Get:3 https://termux.net stable/main aarch64 curl aarch64 8.21.0 [241 kB]
Get:4 https://termux.net stable/main aarch64 less aarch64 704 [138 kB]
Get:5 https://termux.net stable/main aarch64 libsmartcols aarch64 2.42.1-2 [103 kB]
Get:6 https://termux.net stable/main aarch64 util-linux aarch64 2.42.1-2 [772 kB]
Get:7 https://termux.net stable/main aarch64 nano aarch64 9.1 [240 kB]
Fetched 3320 kB in 2s (1726 kB/s)
(Reading database ... 3796 files and directories currently installed.)
Preparing to unpack .../coreutils_9.11-1_aarch64.deb ...
Unpacking coreutils (9.11-1) over (9.11) ...
Setting up coreutils (9.11-1) ...
(Reading database ... 3796 files and directories currently installed.)
Preparing to unpack .../libcurl_8.21.0_aarch64.deb ...
Unpacking libcurl (8.21.0) over (8.20.0) ...
Setting up libcurl (8.21.0) ...
(Reading database ... 3796 files and directories currently installed.)
Preparing to unpack .../curl_8.21.0_aarch64.deb ...
Unpacking curl (8.21.0) over (8.20.0) ...
Setting up curl (8.21.0) ...
(Reading database ... 3796 files and directories currently installed.)
Preparing to unpack .../archives/less_704_aarch64.deb ...
Unpacking less (704) over (702) ...
Setting up less (704) ...
(Reading database ... 3796 files and directories currently installed.)
Preparing to unpack .../libsmartcols_2.42.1-2_aarch64.deb ...
Unpacking libsmartcols (2.42.1-2) over (2.42.1) ...
Setting up libsmartcols (2.42.1-2) ...
(Reading database ... 3796 files and directories currently installed.)
Preparing to unpack .../util-linux_2.42.1-2_aarch64.deb ...
Unpacking util-linux (2.42.1-2) over (2.42.1) ...
Setting up util-linux (2.42.1-2) ...
(Reading database ... 3796 files and directories currently installed.)
Preparing to unpack .../archives/nano_9.1_aarch64.deb ...
Unpacking nano (9.1) over (9.0) ...
Setting up nano (9.1) ...
~ $ pkg install python -y
Installing:
  python

Installing dependencies:
  clang           libicu     ncurses-ui-libs
  gdbm            libllvm    ndk-sysroot
  glib            libsqlite  pkg-config
  libcompiler-rt  libxml2    python-ensurepip-wheels
  libcrypt        lld        python-pip
  libexpat        llvm       resolv-conf
  libffi          make       zstd

Summary:
  Upgrading: 0, Installing: 22, Removing: 0, Not Upgrading: 0
  Download size: 105 MB
  Space needed: 619 MB

Get:1 https://termux.net stable/main aarch64 libcompiler-rt aarch64 21.1.8-2 [2792 kB]
Get:2 https://termux.net stable/main aarch64 libffi aarch64 3.5.2 [31.2 kB]
Get:3 https://termux.net stable/main aarch64 libicu aarch64 78.3 [10.2 MB]
Get:4 https://termux.net stable/main aarch64 libxml2 aarch64 2.15.3 [440 kB]
Get:5 https://termux.net stable/main aarch64 zstd aarch64 1.5.7-1 [360 kB]
Get:6 https://termux.net stable/main aarch64 libllvm aarch64 21.1.8-2 [30.3 MB]
Get:7 https://termux.net stable/main aarch64 lld aarch64 21.1.8-2 [2800 kB]
Get:8 https://termux.net stable/main aarch64 llvm aarch64 21.1.8-2 [14.7 MB]
Get:9 https://termux.net stable/main aarch64 ndk-sysroot aarch64 29-2 [1954 kB]
Get:10 https://termux.net stable/main aarch64 clang aarch64 21.1.8-2 [30.1 MB]
Get:11 https://termux.net stable/main aarch64 gdbm aarch64 1.26-1 [150 kB]
Get:12 https://termux.net stable/main aarch64 resolv-conf aarch64 1.3 [992 B]
Get:13 https://termux.net stable/main aarch64 libcrypt aarch64 0.2-6 [8868 B]
Get:14 https://termux.net stable/main aarch64 libexpat aarch64 2.8.1 [93.7 kB]
Get:15 https://termux.net stable/main aarch64 libsqlite aarch64 3.53.2 [756 kB]
Get:16 https://termux.net stable/main aarch64 ncurses-ui-libs aarch64 6.6.20260307+really6.5.20250830 [33.0 kB]
Get:17 https://termux.net stable/main aarch64 python aarch64 3.13.13-1 [4521 kB]
Get:18 https://termux.net stable/main aarch64 glib aarch64 2.88.1 [2555 kB]
Get:19 https://termux.net stable/main aarch64 make aarch64 4.4.1-1 [240 kB]
Get:20 https://termux.net stable/main aarch64 pkg-config aarch64 0.29.2-3 [32.8 kB]
Get:21 https://termux.net stable/main aarch64 python-ensurepip-wheels all 3.13.13-1 [1713 kB]
Get:22 https://termux.net stable/main aarch64 python-pip all 26.1.2 [1190 kB]
Fetched 105 MB in 26s (3986 kB/s)
Selecting previously unselected package libcompiler-rt.
(Reading database ... 3796 files and directories currently installed.)
Preparing to unpack .../00-libcompiler-rt_21.1.8-2_aarch64.deb ...
Unpacking libcompiler-rt (21.1.8-2) ...
Selecting previously unselected package libffi.
Preparing to unpack .../01-libffi_3.5.2_aarch64.deb ...
Unpacking libffi (3.5.2) ...
Selecting previously unselected package libicu.
Preparing to unpack .../02-libicu_78.3_aarch64.deb ...
Unpacking libicu (78.3) ...
Selecting previously unselected package libxml2.
Preparing to unpack .../03-libxml2_2.15.3_aarch64.deb ...
Unpacking libxml2 (2.15.3) ...
Selecting previously unselected package zstd.
Preparing to unpack .../04-zstd_1.5.7-1_aarch64.deb ...
Unpacking zstd (1.5.7-1) ...
Selecting previously unselected package libllvm.
Preparing to unpack .../05-libllvm_21.1.8-2_aarch64.deb ...
Unpacking libllvm (21.1.8-2) ...
Selecting previously unselected package lld.
Preparing to unpack .../06-lld_21.1.8-2_aarch64.deb ...
Unpacking lld (21.1.8-2) ...
Selecting previously unselected package llvm.
Preparing to unpack .../07-llvm_21.1.8-2_aarch64.deb ...
Unpacking llvm (21.1.8-2) ...
Selecting previously unselected package ndk-sysroot.
Preparing to unpack .../08-ndk-sysroot_29-2_aarch64.deb ...
Unpacking ndk-sysroot (29-2) ...
Selecting previously unselected package clang.
Preparing to unpack .../09-clang_21.1.8-2_aarch64.deb ...
Unpacking clang (21.1.8-2) ...
Selecting previously unselected package gdbm.
Preparing to unpack .../10-gdbm_1.26-1_aarch64.deb ...
Unpacking gdbm (1.26-1) ...
Selecting previously unselected package resolv-conf.
Preparing to unpack .../11-resolv-conf_1.3_aarch64.deb ...
Unpacking resolv-conf (1.3) ...
Selecting previously unselected package libcrypt.
Preparing to unpack .../12-libcrypt_0.2-6_aarch64.deb ...
Unpacking libcrypt (0.2-6) ...
Selecting previously unselected package libexpat.
Preparing to unpack .../13-libexpat_2.8.1_aarch64.deb ...
Unpacking libexpat (2.8.1) ...
Selecting previously unselected package libsqlite.
Preparing to unpack .../14-libsqlite_3.53.2_aarch64.deb ...
Unpacking libsqlite (3.53.2) ...
Selecting previously unselected package ncurses-ui-libs.
Preparing to unpack .../15-ncurses-ui-libs_6.6.20260307+really6.5.20250830_aarch64.deb ...
Unpacking ncurses-ui-libs (6.6.20260307+really6.5.20250830) ...
Selecting previously unselected package python.
Preparing to unpack .../16-python_3.13.13-1_aarch64.deb ...
Unpacking python (3.13.13-1) ...
Selecting previously unselected package glib.
Preparing to unpack .../17-glib_2.88.1_aarch64.deb ...
Unpacking glib (2.88.1) ...
Selecting previously unselected package make.
Preparing to unpack .../18-make_4.4.1-1_aarch64.deb ...
Unpacking make (4.4.1-1) ...
Selecting previously unselected package pkg-config.
Preparing to unpack .../19-pkg-config_0.29.2-3_aarch64.deb ...
Unpacking pkg-config (0.29.2-3) ...
Selecting previously unselected package python-ensurepip-wheels.
Preparing to unpack .../20-python-ensurepip-wheels_3.13.13-1_all.deb ...
Unpacking python-ensurepip-wheels (3.13.13-1) ...
Selecting previously unselected package python-pip.
Preparing to unpack .../21-python-pip_26.1.2_all.deb ...
Unpacking python-pip (26.1.2) ...
Setting up resolv-conf (1.3) ...
Setting up gdbm (1.26-1) ...
Setting up ndk-sysroot (29-2) ...
Setting up libexpat (2.8.1) ...
Setting up libicu (78.3) ...
Setting up libsqlite (3.53.2) ...
Setting up libffi (3.5.2) ...
Setting up libcrypt (0.2-6) ...
Setting up ncurses-ui-libs (6.6.20260307+really6.5.20250830) ...
Setting up make (4.4.1-1) ...
Setting up libcompiler-rt (21.1.8-2) ...
Setting up python (3.13.13-1) ...
Setting up libxml2 (2.15.3) ...
Setting up zstd (1.5.7-1) ...
Setting up python-ensurepip-wheels (3.13.13-1) ...
Setting up python-pip (26.1.2) ...
pip setup...
Writing to /data/data/com.termux/files/usr/etc/pip.conf
Setting up libllvm (21.1.8-2) ...
Setting up glib (2.88.1) ...
No schema files found: doing nothing.
Setting up lld (21.1.8-2) ...
Setting up pkg-config (0.29.2-3) ...
Setting up llvm (21.1.8-2) ...
Setting up clang (21.1.8-2) ...
~ $ pip install python-telegram-bot requests
Collecting python-telegram-bot
  Downloading python_telegram_bot-22.8-py3-none-any.whl.metadata (17 kB)
Collecting requests
  Downloading requests-2.34.2-py3-none-any.whl.metadata (4.8 kB)
Collecting httpx<0.29,>=0.27 (from python-telegram-bot)
  Downloading httpx-0.28.1-py3-none-any.whl.metadata (7.1 kB)
Collecting anyio (from httpx<0.29,>=0.27->python-telegram-bot)
  Downloading anyio-4.15.1-py3-none-any.whl.metadata (4.7 kB)
Collecting certifi (from httpx<0.29,>=0.27->python-telegram-bot)
  Downloading certifi-2026.7.22-py3-none-any.whl.metadata (2.5 kB)
Collecting httpcore==1.* (from httpx<0.29,>=0.27->python-telegram-bot)
  Downloading httpcore-1.0.9-py3-none-any.whl.metadata (21 kB)
Collecting idna (from httpx<0.29,>=0.27->python-telegram-bot)
  Downloading idna-3.20-py3-none-any.whl.metadata (7.2 kB)
Collecting h11>=0.16 (from httpcore==1.*->httpx<0.29,>=0.27->python-telegram-bot)
  Downloading h11-0.16.0-py3-none-any.whl.metadata (8.3 kB)
Collecting charset_normalizer<4,>=2 (from requests)
  Downloading charset_normalizer-3.5.2-cp313-cp313-android_24_arm64_v8a.whl.metadata (46 kB)
Collecting urllib3<3,>=1.26 (from requests)
  Downloading urllib3-2.8.0-py3-none-any.whl.metadata (7.4 kB)
Collecting typing_extensions>=4.16.0 (from anyio->httpx<0.29,>=0.27->python-telegram-bot)
  Downloading typing_extensions-4.16.0-py3-none-any.whl.metadata (3.3 kB)
Downloading python_telegram_bot-22.8-py3-none-any.whl (769 kB)
   ━━━━━━━━━━━━━━━━━━━━ 769.4/769.4 kB 2.2 MB/s  0:00:00
Downloading httpx-0.28.1-py3-none-any.whl (73 kB)
Downloading httpcore-1.0.9-py3-none-any.whl (78 kB)
Downloading requests-2.34.2-py3-none-any.whl (73 kB)
Downloading charset_normalizer-3.5.2-cp313-cp313-android_24_arm64_v8a.whl (225 kB)
Downloading idna-3.20-py3-none-any.whl (69 kB)
Downloading urllib3-2.8.0-py3-none-any.whl (135 kB)
Downloading certifi-2026.7.22-py3-none-any.whl (136 kB)
Downloading h11-0.16.0-py3-none-any.whl (37 kB)
Downloading anyio-4.15.1-py3-none-any.whl (132 kB)
Downloading typing_extensions-4.16.0-py3-none-any.whl (45 kB)
Installing collected packages: urllib3, typing_extensions, idna, h11, charset_normalizer, certifi, requests, httpcore, anyio, httpx, python-telegram-bot
Successfully installed anyio-4.15.1 certifi-2026.7.22 charset_normalizer-3.5.2 h11-0.16.0 httpcore-1.0.9 httpx-0.28.1 idna-3.20 python-telegram-bot-22.8 requests-2.34.2 typing_extensions-4.16.0 urllib3-2.8.0
~ $ mkdir ee_crypto_bot
~ $ cd ee_crypto_bot
~/ee_crypto_bot $ nano bot.py
~/ee_crypto_bot $ python bot.py
🤖 Bot is running...
^C~/ee_crypto_bot $ nano bot.py
~/ee_crypto_bot $ python bot.py
🤖 𝑬'𝑬 Crypto Bot is running...
^C~/ee_crypto_bot $ python -c "import requests; print(requests.get('https://netarz.ir/api/fx/v1/rates/USD', timeout=10).status_code)"
401
~/ee_crypto_bot $ python -c 'import requests; k=input("API Key: "); r=requests.get("https://netarz.ir/api/fx/v1/me",headers={"Authorization":"Bearer "+k},timeout=10); print(r.status_code); print(r.text)'
API Key: netarz-fx-verify=ntz-w8wvr28n3rxa6h5eqvfs43vcfdp7jyd9
401
{"error":{"code":"invalid_api_key","message":"کلید API نامعتبر است.","status":401,"docs":"https://netarz.ir/docs/fx/errors#invalid_api_key"}}
~/ee_crypto_bot $ grep NETARZ_API_KEY bot.py
NETARZ_API_KEY = "fx-ntz-v1-HmfUypHkcPqviPxGcLowGM25zGqomlj5wQXU99B3"
        "Authorization": f"Bearer {NETARZ_API_KEY}"
~/ee_crypto_bot $ python bot.py
🤖 𝑬'𝑬 Crypto Bot is running...
^C~/ee_crypto_bot $ curl -i "https://netarz.ir/api/fx/v1/rates/USD" \
> -H "Authorization: Bearer netarz-fx-verify=ntz-w8wvr28n3rxa6h5eqvfs43vcfdp7jyd9"
HTTP/2 401
date: Sat, 03 Oct 2026 04:57:15 GMT
content-type: application/json
server: cloudflare
cache-control: no-cache, private
x-ratelimit-limit: 30
x-ratelimit-remaining: 29
cf-cache-status: DYNAMIC
nel: {"report_to":"cf-nel","success_fraction":0.0,"max_age":604800}
strict-transport-security: max-age=15552000
report-to: {"group":"cf-nel","max_age":604800,"endpoints":[{"url":"https://a.nel.cloudflare.com/report/v4?s=ZQcprDYOuxFuQmejv4zuKHnd5%2B22wveN1C%2BtJbM5kbt1QuvTj%2BSZF3QrKykY%2FKBZXjVi1XMC5GihfM0lIBVXLdXFOOoIpefgRbt5d%2B%2FoqIz%2F7z7%2FHx%2F28pugn8U%3D"}]}
cf-ray: a4495d6cdb51d22f-FRA
alt-svc: h3=":443"; ma=86400

{"error":{"code":"invalid_api_key","message":"کلید API نامعتبر است.","status":401,"docs":"https://netarz.ir/docs~/ee_crypto_bot $ ^C
~/ee_crypto_bot $ python -c 'import requests; k=input("API Key: "); r=requests.get("https://netarz.ir/api/fx/v1/me",headers={"Authorization":"Bearer "+k},timeout=10); print(r.status_code); print(r.text)'
API Key: netarz-fx-verify=ntz-w8wvr28n3rxa6h5eqvfs43vcfdp7jyd9
401
{"error":{"code":"invalid_api_key","message":"کلید API نامعتبر است.","status":401,"docs":"https://netarz.ir/docs/fx/errors#invalid_api_key"}}
~/ee_crypto_bot $ ^C
~/ee_crypto_bot $ nano bot.py
~/ee_crypto_bot $ python bot.py
🤖 𝑬'𝑬 Crypto Bot is running...
CRYPTO ERROR: قیمت دلار از TGJU پیدا نشد
CRYPTO ERROR: قیمت دلار از TGJU پیدا نشد
~/ee_crypto_bot $ python -c "import requests; r=requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd',timeout=15); print(r.status_code); print(r.text)"
200
{"bitcoin":{"usd":84558}}
~/ee_crypto_bot $ python -c "import requests; r=requests.get('https://www.tgju.org/profile/price_dollar_rl',timeout=15); print(r.status_code); print(len(r.text))"
200
875324
~/ee_crypto_bot $ python -c "import requests,re; t=requests.get('https://www.tgju.org/profile/price_dollar_rl',timeout=15).text; m=re.findall(r'[\d,]{4,}',t); print(m[:30])"
['202610038', '35608', '00004887', '00004887', '2011', '982191010004', '1559713820', '180,', '982191014609', '107718924', '107718924', '99999', '99999999', '263238', '867474', '134,', '134,', '134,', '146,', '146,', '255,', '1728', '1023', '1023', '100,', '8331', '8331', '131313', '525151', '7471']
~/ee_crypto_bot $ python -c "import requests,re; t=requests.get('https://www.tgju.org/profile/price_dollar_rl',timeout=15).text; i=t.find('price_dollar_rl'); print(t[i:i+2000])"
price_dollar_rl">
        <meta property="og:type" content="website">
        <meta property="og:description" content="قیمت دلار,دلار,فیمت دلار,قبمت دلار,قسمت دلار,قمت دلار,قمیت دلار,قیت دلار,قيمت دلار,قیمت دلار,قيمت دلار امروز,قیمته دلار,قیمث دلار,قینت دلار,نرح دلار,یمت دلار">


        <meta name="twitter:card" content="summary">
        <meta name="twitter:title" content="قیمت دلار آزاد | شبکه اطلاع‌ رسانی طلا و ارز ">
        <meta name="twitter:site" content="@tgjuofficial">
        <meta name="twitter:creator" content="@tgjuofficial">
        <meta name="twitter:description" content="قیمت دلار,دلار,فیمت دلار,قبمت دلار,قسمت دلار,قمت دلار,قمیت دلار,قیت دلار,قيمت دلار,قیمت دلار,قيمت دلار امروز,قیمته دلار,قیمث دلار,قینت دلار,نرح دلار,یمت دلار">

        <link rel="canonical" href="https://www.tgju.org/profile/price_dollar_rl">

        <link rel="stylesheet" href="https://static.tgju.org/views/default/css/init-new.css?revision=00004887.css">
        <script data-cfasync="false" src="https://static.tgju.org/views/default/js/init.js?revision=00004887.js" defer></script>
<style>
                @font-face {
                        font-family: iranyekan;
                        font-style: normal;
                        font-weight: 700;
                        src: url("https://static.tgju.org/views/default/fonts/iranyekan/Farsi_numerals_(Non_Standard)/WebFonts/fonts/eot/iranyekanwebbold(fanum).eot");
                        src: url("https://static.tgju.org/views/default/fonts/iranyekan/Farsi_numerals_(Non_Standard)/WebFonts/fonts/eot/iranyekanwebbold(fanum).eot?#iefix") format("embedded-opentype"), url("https://static.tgju.org/views/default/fonts/iranyekan/Farsi_numerals_(Non_Standard)/WebFonts/fonts/woff2/iranyekanwebbold(fanum).woff2") format("woff2"), url("https://static.tgju.org/views/default/fonts/iranyekan/Farsi_numerals_(Non_Standard)/WebFonts/fonts/woff/iranyekanwebbold(fanum).woff") format("woff"), url("https://static.tgju.org/views/default/fonts/iranyekan/Farsi_numerals_(Non_Standard)/WebFonts/fonts/ttf/iranyekanwebbold(fanum).ttf") format("truetype")
                }

                @font-face {
                        font-family: iranyekan;
                        font-style: normal;
                        font-weigh
~/ee_crypto_bot $ python -c "import requests,re; t=requests.get('https://www.tgju.org/profile/price_dollar_rl',timeout=15).text; m=re.findall(r'price_dollar_rl.{0,500}',t); print('\n---\n'.join(m[:5]))"
price_dollar_rl">
---
price_dollar_rl">
---
price_dollar_rl",
---
price_dollar_rl"
---
price_dollar_rl"
~/ee_crypto_bot $ ^C
~/ee_crypto_bot $ nano ~/ee_crypto_bot/bot.py
~/ee_crypto_bot $ cd ~/ee_crypto_bot
~/ee_crypto_bot $ python bot.py
✅ 𝑬'𝑬 | Crypto Bot Started
ERROR: Exception('قیمت دلار از TGJU پیدا نشد')
ERROR: Exception('قیمت دلار از TGJU پیدا نشد')
ERROR: Exception('قیمت دلار از TGJU پیدا نشد')
^C~/ee_crypto_bot $ python -c "import requests; r=requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd',timeout=20); print('STATUS:',r.status_code); print('BODY:',r.text[:500])"
STATUS: 200
BODY: {"bitcoin":{"usd":84609}}
~/ee_crypto_bot $ python -c "exec(open('bot.py').read().replace('main()','')) ; print(get_dollar_toman())"
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    exec(open('bot.py').read().replace('main()','')) ; print(get_dollar_toman())
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<string>", line 300
    def :
        ^
SyntaxError: invalid syntax
~/ee_crypto_bot $ nano ~/ee_crypto_bot/bot.py
~/ee_crypto_bot $ cd ~/ee_crypto_bot
~/ee_crypto_bot $ python bot.py
✅ 𝑬'𝑬 | Crypto Bot Started
~/ee_crypto_bot $ nano ~/ee_crypto_bot/bot.py
~/ee_crypto_bot $ cd ~/ee_crypto_bot
~/ee_crypto_bot $ python bot.py
✅ 𝑬'𝑬 | Crypto Bot Started
Network Retry Loop (Polling Updates): Invalid token. Aborting retry loop.
Traceback (most recent call last):
  File "/data/data/com.termux/files/usr/lib/python3.13/site-packages/telegram/ext/_utils/networkloop.py", line 161, in network_retry_loop
    await do_action()
  File "/data/data/com.termux/files/usr/lib/python3.13/site-packages/telegram/ext/_utils/networkloop.py", line 154, in do_action
    action_cb_task.result()
    ~~~~~~~~~~~~~~~~~~~~~^^
  File "/data/data/com.termux/files/usr/lib/python3.13/site-packages/telegram/ext/_updater.py", line 340, in polling_action_cb
    updates = await self.bot.get_updates(
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ...<3 lines>...
    )
    ^
  File "/data/data/com.termux/files/usr/lib/python3.13/site-packages/telegram/ext/_extbot.py", line 680, in get_updates
    updates = await super().get_updates(
              ^^^^^^^^^^^^^^^^^^^^^^^^^^
    ...<9
