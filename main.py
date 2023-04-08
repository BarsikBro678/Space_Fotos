import datetime
import os
from urllib.parse import urlparse

from requests import get


def load_image(image_url, image_pass, params=None):
	response = get(image_url, params=params)
	response.raise_for_status()

	with open(image_pass, 'wb') as file:
		file.write(response.content)


def fetch_spacex_last_launch():
	url = "https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a"
	response = get(url)
	response.raise_for_status()
	spase_x_images = response.json()["links"]["flickr"]["original"]

	for number, spase_x_image in enumerate(spase_x_images):
		load_image(spase_x_image,
		           "images/Spase_X_{number}.jpg".format(number=number + 1))


def fetch_extection(url):
	return os.path.splitext(urlparse(url).path)[1]


def fetch_nasa_last_launch(nasa_api_key):
	url = "https://api.nasa.gov/planetary/apod"
	payload = {
		"api_key": nasa_api_key,
		"count": 30,
	}
	response = get(url, params=payload)
	response.raise_for_status()
	nasa_images = response.json()
	for number, nasa_image in enumerate(nasa_images):
		if fetch_extection(nasa_image['media_type']) != 'image':
			continue
		load_image(nasa_image["url"],
		           f"images/nasa_image_{number + 1}{fetch_extection(nasa_image['url'])}")


def fetch_nasa_epic(nasa_api_key):
	url = "https://api.nasa.gov/EPIC/api/natural/images"
	payload = {
		"api_key": nasa_api_key,
		"count": 8,
	}
	response = get(url, params=payload)
	response.raise_for_status()
	for number, image in enumerate(response.json()):
		date = datetime.datetime.fromisoformat(image["date"])
		date = date.strftime('%Y/%m/%d')
		image_url = f"https://api.nasa.gov/EPIC/archive/natural/{date}/png/{image['image']}.png"
		load_image(image_url,
				    f"images/epic_nasa_{number}.png",
				    params={"api_key": nasa_api_key,})


def main():
	nasa_api_key = os.environ["NASA_API_KEY"]
	fetch_spacex_last_launch()
	fetch_nasa_last_launch(nasa_api_key)
	fetch_nasa_epic(nasa_api_key)


if __name__ == "__main__":
	main()
