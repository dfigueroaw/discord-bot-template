from dotenv import load_dotenv
from os import getenv
from interactions import Client, Intents

load_dotenv(verbose=True)

dev_mode = True

bot_token = getenv("BOT_TOKEN")

if not bot_token:
    raise ValueError("❌ Environment variable BOT_TOKEN is missing. Please check your .env file.")

scope = getenv("DEFAULT_SCOPE") if dev_mode else None

if dev_mode and not scope:
    raise ValueError("❌ Environment variable DEFAULT_SCOPE is missing. Please check your .env file.")

bot = Client(
    token=bot_token,
    intents=Intents.ALL,
    default_scope=int(scope) if dev_mode else None,
)
