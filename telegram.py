import os
import random
from time import sleep

import telegram 


def send_photo_telegram_bot(bot, chat_id):
	with open(get_random_picture(), "rb") as photo:
		bot.send_photo(chat_id = chat_id, photo = photo)	


def get_random_picture():
	images = os.listdir("images")
	return f"images/{random.choice(images)}"

	
def main():
	bot_wait = os.environ["BOT_WAIT"]
	bot_telegram_token = os.environ["BOT_TELEGRAM_TOKEN"]
	tg_chat_id = os.environ["TG_CHAT_ID"]
	bot = telegram.Bot(token=bot_telegram_token)
	while True:
		send_photo_telegram_bot(bot, tg_chat_id)
		sleep(bot_wait)
		

if __name__ == "__main__":
	main()
