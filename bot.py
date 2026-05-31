import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

app = Client(
    "gsgw_bot",
    bot_token=os.getenv("BOT_TOKEN")
)

CHANNEL_LINK = "https://t.me/GSGW01"
STORAGE_LINK = "https://t.me/+T2eOSVsgXANiMTU6"

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply(
        "Welcome to Got Dropped into a Ghost Story, Still Gotta Work!",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("📚 Read Manhwa", url=CHANNEL_LINK)],
                [InlineKeyboardButton("📦 Chapter Storage", url=STORAGE_LINK)]
            ]
        )
    )

    if __name__ == "__main__":
    try:
        app.run()
    except Exception as e:
        print(f"ERROR: {e}")
        raise
