from serpapi import search as GoogleSearch
from pydantic import BaseModel

from typing import AnyStr, List

from config import SERPAPI_KEY

class ImageResponse(BaseModel):
    url: AnyStr
    image_id: AnyStr
    name: AnyStr
    width: int
    height: int

class GoogleScraper():
    def __init__(self, location: AnyStr, lang: AnyStr = "en"):
        self.api_key = SERPAPI_KEY
        self.location = location
        self.lang = lang
        self.images: List[ImageResponse] = None

    def scrape(self, q: AnyStr) -> None:
        image_results = GoogleSearch({
            "engine": "google_images",
            "q": q,
            "location": self.location,
            "api_key": self.api_key,
            "hl": self.lang
        }).as_dict()["images_results"]
        
        #format response and save

    def save(self) -> List[AnyStr]:
        pass