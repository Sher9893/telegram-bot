import requests
import time
import asyncio
from telegram import Bot

TOKEN = "7504805023:AAHaMeQW1BBR7fPKPLHxzya2j6obZq2G7ro"
CHANNEL_ID = "@pi_network_price1"  # Yoki manfiy ID

bot = Bot(token=TOKEN)

def get_pi_network_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=pi-network&vs_currencies=usd"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if "pi-network" in data:
            return data["pi-network"]["usd"]
    return None

async def send_price_to_channel():
    try:
        price = get_pi_network_price()
        if price:
            message = f"Pi Network price: ${price} USD"
            await bot.send_message(chat_id=CHANNEL_ID, text=message)  # await ishlatildi
        else:
            await bot.send_message(chat_id=CHANNEL_ID, text="Kursni olishda xatolik yuz berdi.")
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")

async def main():
    while True:
        await send_price_to_channel()
        await asyncio.sleep(60)  # Har 60 soniyada yangilash

if __name__ == "__main__":
    asyncio.run(main())  # Asinxron dasturni ishga tushirish