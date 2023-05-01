import os

from requests import get

from tools import load_image


def fetch_spasex_last_launch():
    url = "https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a"
        response = get(url)
    response.raise_for_status()
    spase_x_images = response.json()["links"]["flickr"]["original"]

    for number, spase_x_image in enumerate(spase_x_images, start=1):
        load_image(spase_x_image,
                    "images/Spase_X_{number}.jpg".format(number=number))


def main():
    os.makedirs("images", exist_ok=True)
    fetch_spasex_last_launch()


if __name__ == "main":
    main()
