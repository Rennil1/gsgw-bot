import os
from pyrogram import Client, filters

app = Client(
    "gsgw_bot",
    api_id=int(os.getenv("API_ID")),
    api_hash=os.getenv("API_HASH"),
    bot_token=os.getenv("BOT_TOKEN")
)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("Bot works!")

if __name__ == "__main__":
    app.run()
