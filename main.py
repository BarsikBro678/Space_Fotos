import os
from urllib.parse import urlparse

from requests import get


def load_image(image_url, image_pass, params=None):
	response = get(image_url, params=params)
	response.raise_for_status()

	with open(image_pass, 'wb') as file:
		file.write(response.content)


def fetch_extection(url):
	return os.path.splitext(urlparse(url).path)[1]
