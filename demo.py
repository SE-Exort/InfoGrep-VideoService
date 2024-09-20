import random, os

from google_scraper import scraper
from models.keyphrase_extractor import extract
from models.tokenize import text_chunk
from models.tts import tts
from ffmpeg.ffmpeg import FFMPEG

chunks = text_chunk("temp/demo.txt")
gs = scraper.GoogleScraper(location="Canada")

frames_file = "frames.txt"

for index, chunk in enumerate(chunks):
    keyphrases = extract(chunk)
    image_path = gs.scrape(random.choice(keyphrases), index)
    audio_path = tts(index, chunk)

    if not os.path.exists("video/"):
        os.makedirs("video/")
    
    video_path = f"video/{index}.mp4"
    FFMPEG(video_path).create_frame(image_path=image_path, audio_path=audio_path)
    with open(frames_file, "a") as frames_txt:
        frames_txt.write(f"file '{video_path}'\n")

FFMPEG("./result.mp4").concat(frames_file)