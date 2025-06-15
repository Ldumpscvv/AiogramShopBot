import os
from dotenv import load_dotenv

from enums.currency import Currency
from enums.runtime_environment import RuntimeEnvironment

# .env Variablen laden
load_dotenv(".env")

# Umgebung (z. B. PROD oder DEV)
RUNTIME_ENVIRONMENT = RuntimeEnvironment(os.environ.get("RUNTIME_ENVIRONMENT", "PROD"))

# Webhook & Server Konfiguration
WEBHOOK_HOST = os.environ.get("WEBHOOK_HOST")  # z. B. https://dein-projekt.onrender.com
WEBHOOK_PATH = os.environ.get("WEBHOOK_PATH", "/webhook")
WEBAPP_HOST = os.environ.get("WEBAPP_HOST", "0.0.0.0")
WEBAPP_PORT = int(os.environ.get("WEBAPP_PORT", 10000))
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"
WEBHOOK_SECRET_TOKEN = os.environ.get("WEBHOOK_SECRET_TOKEN")

# Telegram Bot Token & Admins
TOKEN = os.environ.get("TOKEN")
ADMIN_ID_LIST = os.environ.get("ADMIN_ID_LIST", "").split(",")
ADMIN_ID_LIST = [int(admin_id) for admin_id in ADMIN_ID_LIST if admin_id]

# Weitere Einstellungen
SUPPORT_LINK = os.environ.get("SUPPORT_LINK")
DB_ENCRYPTION = os.environ.get("DB_ENCRYPTION", "false").lower() == "true"
DB_NAME = os.environ.get("DB_NAME")
DB_PASS = os.environ.get("DB_PASS")
PAGE_ENTRIES = int(os.environ.get("PAGE_ENTRIES", "10"))
BOT_LANGUAGE = os.environ.get("BOT_LANGUAGE", "en")
MULTIBOT = os.environ.get("MULTIBOT", "false").lower() == "true"
ETHPLORER_API_KEY = os.environ.get("ETHPLORER_API_KEY")
CURRENCY = Currency(os.environ.get("CURRENCY", "USD"))

# Redis
REDIS_HOST = os.environ.get("REDIS_HOST", "localhost")
REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD")
