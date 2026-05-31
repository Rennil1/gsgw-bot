import os
from pyrogram import Client

try:
    app = Client(
        "gsgw_bot",
        api_id=int(os.getenv("API_ID")),
        api_hash=os.getenv("API_HASH"),
        bot_token=os.getenv("BOT_TOKEN")
    )

    print("Starting bot...")
    app.run()

except Exception as e:
    print("ERROR:", repr(e))
    raise
