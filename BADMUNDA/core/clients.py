# starting all clients
import logging
import platform

from SukhPB.start_bot import start_bot
from pyrogram import Client as call
from pyrogram import __version__ as py_version
from pyrogram import idle

from BADMUNDA.Config import *

version = "v2.0"
group_username = "@visible_spam_hub"
logging.basicConfig(format="%(levelname)s  %(message)s", level=logging.INFO)


if ":" in BOT_TOKEN:
    Client1 = call(
        "visible spam",
        api_id=APP_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN,
        plugins=dict(root="visiblespam/visible_spam007"),
    )
    print("BadSpam : Bot token 1 has been found")
else:
    print("BadSpam : Client 1 not Found")


if BOT_TOKEN2:
    Client2 = call(
        "BadSpam2",
        api_id=APP_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN2,
        plugins=dict(root="ᴠɪsɪʙʟᴇ sᴘᴀᴍ"),
    )
    print("ᴠɪsɪʙʟᴇ sᴘᴀᴍ: Bot token 2 Found")
else:
    Client2 = None


if BOT_TOKEN3:
    Client3 = call(
        "ᴠɪsɪʙʟᴇ sᴘᴀᴍ 𝟹",
        api_id=APP_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN3,
        plugins=dict(root="ᴠɪsɪʙʟᴇ sᴘᴀᴍ"),
    )
    print("ᴠɪsɪʙʟᴇ sᴘᴀᴍ: Bot token 3 Found")
else:
    Client3 = None


if BOT_TOKEN4:
    Client4 = call(
        "ᴠɪsɪʙʟᴇ sᴘᴀᴍ 𝟺",
        api_id=APP_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN4,
        plugins=dict(root="ᴠɪsɪʙʟᴇ sᴘᴀᴍ"),
    )
    print(" ᴠɪsɪʙʟᴇ sᴘᴀᴍ- [INFO]: Bot token 4 Found")
else:
    Client4 = None

if BOT_TOKEN5:
    Client5 = call(
        "ᴠɪsɪʙʟᴇ sᴘᴀᴍ 𝟻",
        api_id=APP_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN5,
        plugins=dict(root="ᴠɪsɪʙʟᴇ sᴘᴀᴍ"),
    )
    print("ᴠɪsɪʙʟᴇ sᴘᴀᴍ 𝟼: Bot token 5 Found")
else:
    Client5 = None

if BOT_TOKEN6:
    Client6 = call(
        "ᴠɪsɪʙʟᴇ sᴘᴀᴍ 𝟼",
        api_id=APP_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN6,
        plugins=dict(root="ᴠɪsɪʙʟᴇ sᴘᴀᴍ"),
    )
    print("ᴠɪsɪʙʟᴇ sᴘᴀᴍ 𝟼: Bot token 6 Found")
else:
    Client6 = None

if BOT_TOKEN7:
    Client7 = call(
        "ᴠɪsɪʙʟᴇ sᴘᴀᴍ 𝟽",
        api_id=APP_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN7,
        plugins=dict(root="ᴠɪsɪʙʟᴇ sᴘᴀᴍ"),
    )
    print("ᴠɪsɪʙʟᴇ sᴘᴀᴍ : Bot token 7 Found")
else:
    Client7 = None

if BOT_TOKEN8:
    Client8 = call(
        "ᴠɪsɪʙʟᴇ sᴘᴀᴍ 𝟾",
        api_id=APP_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN8,
        plugins=dict(root="ᴠɪsɪʙʟᴇ sᴘᴀᴍ"),
    )
    print("ᴠɪsɪʙʟᴇ sᴘᴀᴍ: Bot token 8 Found")
else:
    Client8 = None

if BOT_TOKEN9:
    Client9 = call(
        "ᴠɪsɪʙʟᴇ sᴘᴀᴍ 𝟿",
        api_id=APP_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN9,
        plugins=dict(root="ᴠɪsɪʙʟᴇ sᴘᴀᴍ"),
    )
    print("ᴠɪsɪʙʟᴇ sᴘᴀᴍ : Bot token 9 Found")
else:
    Client9 = None

if BOT_TOKEN10:
    Client10 = call(
        "ᴠɪsɪʙʟᴇ sᴘᴀᴍ 𝟷𝟶",
        api_id=APP_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN10,
        plugins=dict(root="ᴠɪsɪʙʟᴇ sᴘᴀᴍ"),
    )
    print("ᴠɪsɪʙʟᴇ sᴘᴀᴍ : Bot token 10 Found")
else:
    Client10 = None

if BOT_TOKEN11:
    Client11 = call(
        "ᴠɪsɪʙʟᴇ sᴘᴀᴍ 𝟷𝟷",
        api_id=APP_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN11,
        plugins=dict(root="ᴠɪsɪʙʟᴇ sᴘᴀᴍ"),
    )
    print("ᴠɪsɪʙʟᴇ sᴘᴀᴍ : Bot token 11 Found")
else:
    Client11 = None

if BOT_TOKEN12:
    Client12 = call(
        "ᴠɪsɪʙʟᴇ sᴘᴀᴍ 𝟷𝟸",
        api_id=APP_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN12,
        plugins=dict(root="ᴠɪsɪʙʟᴇ sᴘᴀᴍ"),
    )
    print(" ᴠɪsɪʙʟᴇ sᴘᴀᴍ : Bot token 12 Found")
else:
    Client12 = None

if BOT_TOKEN13:
    Client13 = call(
        "ᴠɪsɪʙʟᴇ sᴘᴀᴍ 𝟷𝟹",
        api_id=APP_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN13,
        plugins=dict(root="ᴠɪsɪʙʟᴇ sᴘᴀᴍ "),
    )
    print(" ᴠɪsɪʙʟᴇ sᴘᴀᴍ 𝟷𝟹: Bot token 13 Found")
else:
    Client13 = None

if BOT_TOKEN14:
    Client14 = call(
        "ᴠɪsɪʙʟᴇ sᴘᴀᴍ 𝟷𝟺",
        api_id=APP_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN14,
        plugins=dict(root="ᴠɪsɪʙʟᴇ sᴘᴀᴍ"),
    )
    print("ᴠɪsɪʙʟᴇ sᴘᴀᴍ 𝟷𝟺: Bot token 14 Found")
else:
    Client14 = None

if BOT_TOKEN15:
    Client15 = call(
        "BadSpam15",
        api_id=APP_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN15,
        plugins=dict(root=" ᴠɪsɪʙʟᴇ sᴘᴀᴍ"),
    )
    print("ᴠɪsɪʙʟᴇ sᴘᴀᴍ 𝟷𝟻: Bot token 15 Found")
else:
    Client15 = None

if BOT_TOKEN16:
    Client16 = call(
        "ᴠɪsɪʙʟᴇ sᴘᴀᴍ 𝟷𝟼",
        api_id=APP_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN16,
        plugins=dict(root="ᴠɪsɪʙʟᴇ sᴘᴀᴍ"),
    )
    print("ᴠɪsɪʙʟᴇ sᴘᴀᴍ 𝟷𝟼: Bot token 16 Found")
else:
    Client16 = None

if BOT_TOKEN17:
    Client17 = call(
        "ᴠɪsɪʙʟᴇ sᴘᴀᴍ 𝟷𝟽",
        api_id=APP_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN17,
        plugins=dict(root="ᴠɪsɪʙʟᴇ sᴘᴀᴍ"),
    )
    print("ᴠɪsɪʙʟᴇ sᴘᴀᴍ : Bot token 17 Found")
else:
    Client17 = None

if BOT_TOKEN18:
    Client18 = call(
        "ᴠɪsɪʙʟᴇ sᴘᴀᴍ 𝟷𝟾",
        api_id=APP_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN18,
        plugins=dict(root="ᴠɪsɪʙʟᴇ sᴘᴀᴍ"),
    )
    print("ᴠɪsɪʙʟᴇ sᴘᴀᴍ: Bot token 18 Found")
else:
    Client18 = None

if BOT_TOKEN19:
    Client19 = call(
        "ᴠɪsɪʙʟᴇ sᴘᴀᴍ 𝟷𝟿",
        api_id=APP_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN19,
        plugins=dict(root="ᴠɪsɪʙʟᴇ sᴘᴀᴍ"),
    )
    print("ᴠɪsɪʙʟᴇ sᴘᴀᴍ : Bot token 19 Found")
else:
    Client19 = None

if BOT_TOKEN20:
    Client20 = call(
        "ᴠɪsɪʙʟᴇ sᴘᴀᴍ 𝟸𝟶",
        api_id=APP_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN20,
        plugins=dict(root="ᴠɪsɪʙʟᴇ sᴘᴀᴍ"),
    )
    print("ᴠɪsɪʙʟᴇ sᴘᴀᴍ : Bot token 20 Found")
else:
    Client20 = None

if BOT_TOKEN21:
    Client21 = call(
        "ᴠɪsɪʙʟᴇ sᴘᴀᴍ 𝟸𝟷",
        api_id=APP_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN21,
        plugins=dict(root="ᴠɪsɪʙʟᴇ sᴘᴀᴍ "),
    )
    print("ᴠɪsɪʙʟᴇ sᴘᴀᴍ : Bot token 12 Found")
else:
    Client21 = None

if BOT_TOKEN22:
    Client22 = call(
        "ᴠɪsɪʙʟᴇ sᴘᴀᴍ 𝟸𝟸",
        api_id=APP_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN22,
        plugins=dict(root="ᴠɪsɪʙʟᴇ sᴘᴀᴍ"),
    )
    print("ᴠɪsɪʙʟᴇ sᴘᴀᴍ : Bot token 22 Found")
else:
    Client22 = None

if BOT_TOKEN23:
    Client23 = call(
        "ᴠɪsɪʙʟᴇ sᴘᴀᴍ 𝟸𝟹",
        api_id=APP_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN23,
        plugins=dict(root="ᴠɪsɪʙʟᴇ sᴘᴀᴍ "),
    )
    print("ᴠɪsɪʙʟᴇ sᴘᴀᴍ: Bot token 23 Found")
else:
    Client23 = None

if BOT_TOKEN24:
    Client24 = call(
        "ᴠɪsɪʙʟᴇ sᴘᴀᴍ 𝟷𝟺",
        api_id=APP_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN14,
        plugins=dict(root="ᴠɪsɪʙʟᴇ sᴘᴀᴍ"),
    )
    print(" ᴠɪsɪʙʟᴇ sᴘᴀᴍ : Bot token 24 Found")
else:
    Client24 = None

if BOT_TOKEN25:
    Client25 = call(
        "ᴠɪsɪʙʟᴇ sᴘᴀᴍ 𝟸𝟻",
        api_id=APP_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN25,
        plugins=dict(root="ᴠɪsɪʙʟᴇ sᴘᴀᴍ"),
    )
    print("BadSpam : Bot token 25 Found")
else:
    Client25 = None


async def Start_BotSpam():
    for i in range(1, 26):
        var = globals()[f"Client{i}"]
        if var is not None:
            await start_bot(var)
    print("➖➖➖➖➖➖➖➖➖➖➖➖")
    print(f"💥ʙᴏᴛ sᴘᴀᴍ 🔥[INFO] : ɢʀᴘᴜᴘ ᴜsᴇʀɴᴀᴍᴇ {group_username}")
    print(f"💥 ʙᴏᴛ sᴘᴀᴍ 🔥[INFO] : ᴠᴇʀsɪᴏɴ - {platform.python_version()}")
    print(f"💥 ʙᴏᴛ sᴘᴀᴍ  🔥[INFO]: sᴘᴀᴍʙᴏᴛ ᴠᴇʀsɪᴏɴ - {version}")
    print(f"💥 ʙᴏᴛ sᴘᴀᴍ 🔥[INFO]: ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ - {py_version}")
    print("➖➖➖➖➖➖➖➖➖➖➖➖")
    await idle()
