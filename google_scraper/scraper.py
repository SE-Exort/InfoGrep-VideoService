from serpapi import search as GoogleSearch
from PIL import Image
import requests

from typing import AnyStr
import os

from config import SERPAPI_KEY

class ImageInvalid(Exception):
    pass

class GoogleScraper():
    def __init__(self, location: AnyStr, lang: AnyStr = "en"):
        self.api_key = SERPAPI_KEY
        self.location = location
        self.lang = lang

    def scrape(self, q: AnyStr, frame: int, page=1) -> None:
        print("Scraping for q: ", q)

        image_results = GoogleSearch({
            "engine": "google_images",
            "q": q,
            "location": self.location,
            "api_key": self.api_key,
            "hl": self.lang,
            "ijn": page
        }).as_dict()["images_results"]
        
        # format response and save
        for result in image_results:
            url = result["original"]
            height, width = result["original_width"], result["original_height"]
            if width >= 540 and height >= 360:
                try:
                    self.download_image(url, frame)
                    return
                except ImageInvalid:
                    continue
        
        # page += 1
        # self.scrape(q, frame, page)

    @staticmethod
    def valid_image(image_path: AnyStr) -> bool:
        try:
            with Image.open(image_path) as img:
                img.verify()
                return True
        except Exception:
            return False

    def download_image(self, url: AnyStr, frame: int) -> None:
        image_ext = url.split(".")[-1]
        if image_ext not in ["jpg", "jpeg", "png", "webp", "tiff"]:
            raise ImageInvalid
        
        img_data = requests.get(url).content

        if not os.path.exists("images/"):
            os.makedirs("images/")
        
        img_file = f'images/{frame}.{image_ext}'
        with open(img_file, 'wb') as handler:
            handler.write(img_data)
            if not self.valid_image(img_file):
                os.remove(img_file)
                raise ImageInvalid

