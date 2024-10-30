from fastapi import APIRouter, Request

from google_scraper import scraper
from models.keyphrase_extractor import extract
from models.tokenize import text_chunk
from models.tts import tts
from ffmpeg.ffmpeg import FFMPEG

import random

router = APIRouter()
gs = scraper.GoogleScraper(location="Canada")


def create_video(text: str, index: int) -> str:

    keyphrases = extract(text)
    
    image_path = gs.scrape(random.choice(keyphrases), index)

    audio_path = tts(index, text)

    video_path = f"/Users/hahafhaha/code/FYDP/VisualGenerationDemo/public/{index}.mp4"
    FFMPEG(video_path).create_frame(image_path=image_path, audio_path=audio_path)

    return video_path

def create_image(text: str, index: int) -> str:

    keyphrases = extract(text)
    
    image_path = gs.scrape(random.choice(keyphrases), index)

    return image_path

@router.post("/visual")
async def text_to_visual(request: Request):
    """ Demo Plan
    - chunk with NLTK, and randomly selects a sentence or two for demoing the video aspect
    - keyword extract with image, and then demo the image part and key phrase
    """
    text_file_path = None
    result_list = []

    try:
        data = await request.json()
        text_file_path = data["text_file_url"]
    
    except Exception as e:
        print(f"Error occured: {str(e)}")
        return {
            "status": 500,
            "payload": {}
        }

    print("Start processing for: ", text_file_path, end="\n\n")

    chunks: list = text_chunk(text_file_path)
    for index, chunk in enumerate(chunks):
        rdint = random.randint(1,3)
        if not rdint % 3:
            # normal text for 0
            result_list.append({
                "index": index,
                "text": chunk,
                "text_type": "text",
                "url": None
            })
        elif rdint % 3 == 1:
            # video for 1
            video_path = create_video(chunk, index)
            result_list.append({
                "index": index,
                "text": chunk,
                "text_type": "video",
                "url": video_path
            })
        # elif rdint % 2 == 2 and len(chunk) <= 50:
        #     # image for 2
        #     image_path = create_image(chunk, index)
        #     result_list.append({
        #         "index": index,
        #         "text": chunk,
        #         "text_type": "image",
        #         "url": image_path
        #     })

    return {
        "status": 200,
        "payload": result_list
    }

"""
TODO
- accurate image locating for each frame for video generated
- image gen highlighted for a word instead of the whole sentence
"""