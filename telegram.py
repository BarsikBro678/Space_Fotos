import os
import random
from time import sleep

import telegram 


def telegram_bot(bot, chat_id):
	with open(randomize(), "rb") as photo:
		bot.send_photo(chat_id = chat_id, photo = photo)	


def randomize():
	images = os.listdir("images")
	return f"images/{random.choice(images)}"

	
def main():
	time = os.environ["TIME"]
	bot_token = os.environ["BOT_TOKEN"]
	chat_id = os.environ["CHAT_ID"]
	bot = telegram.Bot(token=bot_token)
	while True:
		telegram_bot(bot, chat_id)
		sleep(time)
		

if __name__ == "__main__":
	main()
