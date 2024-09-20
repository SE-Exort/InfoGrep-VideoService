import random

from google_scraper import scraper
from models.keyphrase_extractor import extract
from models.tokenize import text_chunk
from models.tts import tts

chunks = text_chunk("temp/demo.txt")
gs = scraper.GoogleScraper(location="Canada")

for index, chunk in enumerate(chunks):
    keyphrases = extract(chunk)
    gs.scrape(random.choice(keyphrases), index)