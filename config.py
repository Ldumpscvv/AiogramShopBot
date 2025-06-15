import os
from dotenv import load_dotenv

from enums.currency import Currency
from enums.runtime_environment import RuntimeEnvironment

load_dotenv(".env")

# Runtime Umgebung
RUNTIME_ENVIRONMENT = RuntimeEnvironment(os.environ.get("RUNTIME_ENVIRONMENT"))

# Fixe Webhook URL (keine ngrok oder sslip.io)
WEBHOOK_HOST = os.environ.get("WEBHOOK_HOST")  # Manuell in .env eintragen
WEBHOOK_PATH = os.environ.get("WEBHOOK_PATH")
WEBAPP_HOST = os.environ.get("WEBAPP_HOST")
WEBAPP_PORT = int(os.environ.get("WEBAPP_PORT"))
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

# Bot-Zeug
TOKEN = os.environ.get("TOKEN")
ADMIN_ID_LIST = os.environ.get("ADMIN_ID_LIST").split(',')
ADMIN_ID_LIST = [int(admin_id) for admin_id in ADMIN_ID_LIST]

# Optionales
SUPPORT_LINK = os.environ.get("SUPPORT_LINK")
DB_ENCRYPTION = os.environ.get("DB_ENCRYPTION", False) == 'true'
DB_NAME = os.environ.get("DB_NAME")
DB_PASS = os.environ.get("DB_PASS")
PAGE_ENTRIES = int(os.environ.get("PAGE_ENTRIES"))
BOT_LANGUAGE = os.environ.get("BOT_LANGUAGE")
MULTIBOT = os.environ.get("MULTIBOT", False) == 'true'
ETHPLORER_API_KEY = os.environ.get("ETHPLORER_API_KEY")
CURRENCY = Currency(os.environ.get("CURRENCY"))
WEBHOOK_SECRET_TOKEN = os.environ.get("WEBHOOK_SECRET_TOKEN")
REDIS_HOST = os.environ.get("REDIS_HOST")
REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD")
