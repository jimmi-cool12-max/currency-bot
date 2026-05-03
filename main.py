import requests
from datetime import datetime
import os

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def get_rates():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    data = requests.get(url).json()

    usd_rub = data["rates"]["RUB"]
    eur_rub = data["rates"]["EUR"] * usd_rub

    return usd_rub, eur_rub

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": text
    })

usd, eur = get_rates()

message = f"""💱 Курс валют на {datetime.now().strftime('%d.%m.%Y')}:

🇺🇸 USD — {round(usd,2)} ₽  
🇪🇺 EUR — {round(eur,2)} ₽
"""

send_message(message)
