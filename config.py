import os

class Config:
    TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    ADMIN_ID = int(os.getenv("ADMIN_ID"))
    DATABASE_URL = os.getenv("DATABASE_URL")
    V2RAY_PANEL_URL = os.getenv("V2RAY_PANEL_URL")
    V2RAY_PANEL_API_KEY = os.getenv("V2RAY_PANEL_API_KEY")
    PAYPAL_CLIENT_ID = os.getenv("PAYPAL_CLIENT_ID")
    PAYPAL_CLIENT_SECRET = os.getenv("PAYPAL_CLIENT_SECRET")