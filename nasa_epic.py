import os
import datetime

from requests import get

from tools import load_image


def fetch_nasa_epic(nasa_api_key, download_quantity=8):
    url = "https://api.nasa.gov/EPIC/api/natural/images"
    payload = {
        "api_key": nasa_api_key,
        "count": images_quantity,
    }
    response = get(url, params=payload)
    response.raise_for_status()
    for number, image in enumerate(response.json(), start=1):
        date = datetime.datetime.fromisoformat(image["date"])
        date = date.strftime('%Y/%m/%d')
        image_url = f"https://api.nasa.gov/EPIC/archive/natural/{date}/png/{image['image']}.png"
        load_image(image_url,
                    f"images/epic_nasa_{number}.png",
                    params={"api_key": nasa_api_key})


def main():
    os.makedirs("images", exist_ok=True)
    nasa_api_key = os.environ["NASA_API_KEY"]
    fetch_nasa_epic(nasa_api_key)


if __name__ == "__main__":
    main()
