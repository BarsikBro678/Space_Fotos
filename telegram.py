import os
import random
from time import sleep

import telegram 


def send_photo_telegram_bot(bot, chat_id):
	with open(randomaizing_pictures(), "rb") as photo:
		bot.send_photo(chat_id = chat_id, photo = photo)	


def randomaizing_pictures():
	images = os.listdir("images")
	return f"images/{random.choice(images)}"

	
def main():
	bot_time = os.environ["BOT_TIME"]
	bot_telegram_token = os.environ["BOT_TELEGRAM_TOKEN"]
	tg_chat_id = os.environ["TG_CHAT_ID"]
	bot = telegram.Bot(token=bot_telegram_token)
	while True:
		send_photo_telegram_bot(bot, tg_chat_id)
		sleep(bot_time)
		

if __name__ == "__main__":
	main()
