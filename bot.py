import os

print("BOT_TOKEN =", bool(os.getenv("BOT_TOKEN")))
print("API_ID =", os.getenv("API_ID"))
print("API_HASH =", bool(os.getenv("API_HASH")))

print("TEST SUCCESS")
