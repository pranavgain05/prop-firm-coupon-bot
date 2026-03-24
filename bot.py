import asyncio
import telebot
from twscrape import API, gather

bot = telebot.TeleBot("8715379481:AAH3DDvgE_53hGuO3ZgMbFfk-DdXLnZt2zM")
api = API()

WORDS = ["coupon", "discount", "code", "prop firm"]

last_id = 0

async def main():
    global last_id
    print("Bot starting...")
    while True:
        query = " OR ".join(WORDS)
        posts = await gather(api.search(query, limit=20))
        for p in posts:
            if p.id > last_id:
                bot.send_message("YOUR_CHAT_ID", f"{p.url}\n{p.rawContent}")
                last_id = max(last_id, p.id)
        await asyncio.sleep(5)

asyncio.run(main())
