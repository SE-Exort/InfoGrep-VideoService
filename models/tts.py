import os

from openai import OpenAI
from config import OPENAI_KEY

client = OpenAI(api_key=OPENAI_KEY)

def tts(frame: int, input_text: str) -> str:
    
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=input_text
    )

    audio_path = f"audio/{frame}.mp3"
    if not os.path.exists("audio/"):
        os.makedirs("audio/")
    
    response.stream_to_file(audio_path)

    print(f"{audio_path} created! for {input_text} \n")

    return audio_path