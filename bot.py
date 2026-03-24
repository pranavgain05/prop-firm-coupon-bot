import asyncio
import telebot
from twscrape import API, gather
import os

bot = telebot.TeleBot("8762357437:AAFAHjLWWZJ2Gq3AoYPJbe9wDX08k-HmAjE")
api = API()

WORDS = [
    "coupon", "discount code", "discount", "100% discount", 
    "100% discount code", "100% discount coupon", "free prop account", 
    "free funded account", "free funded prop account", "prop firm discount"
]

last_id = 0

async def main():
    global last_id
    print("Bot starting...")
    while True:
        query = " OR ".join(WORDS)
        posts = await gather(api.search(query, limit=20))
        for p in posts:
            if p.id > last_id:
                bot.send_message(os.getenv("CHAT_ID"), f"{p.url}\n{p.rawContent}")
                last_id = max(last_id, p.id)
        await asyncio.sleep(5)

asyncio.run(main())
