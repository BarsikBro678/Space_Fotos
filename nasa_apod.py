import os

from requests import get

from tools import fetch_extection, load_image


def fetch_nasa_apod(nasa_api_key, images_quantity=30):
    url = "https://api.nasa.gov/planetary/apod"
    payload = {
        "api_key": nasa_api_key,
        "count": images_quantity,
    }
    response = get(url, params=payload)
    response.raise_for_status()
    nasa_images = response.json()
    for number, nasa_image in enumerate(nasa_images, start=1):
        if nasa_image['media_type'] != 'image':
            continue
        load_image(nasa_image["url"],
                    f"images/nasa_image_{number}{fetch_extection(nasa_image['url'])}")


def main():
    os.makedirs("images", exist_ok=True)
    nasa_api_key = os.environ["NASA_API_KEY"]
    fetch_nasa_apod(nasa_api_key)


if __name__ == "__main__":
    main()
