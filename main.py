from config import API_ID, API_HASH, BOT_TOKEN
from pyrogram import Client, idle

app = Client(
    "bot",
    api_id=env.API_ID,
    api_hash=env.API_HASH,
    bot_token=env.BOT_TOKEN,
)

print("BOT TELAH AKTIF")
idle()
