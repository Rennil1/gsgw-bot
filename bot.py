import os
from pyrogram import Client, filters

try:
    app = Client(
        "gsgw_bot",
        api_id=int(os.getenv("API_ID")),
        api_hash=os.getenv("API_HASH"),
        bot_token=os.getenv("BOT_TOKEN")
    )

    @app.on_message(filters.command("start"))
    async def start(client, message):
        await message.reply("Bot works!")

    print("STARTING BOT...")
    app.run()

except Exception as e:
    print("ERROR:", repr(e))
    raise
