from openai import OpenAI
from config import OPENAI_KEY

client = OpenAI(api_key=OPENAI_KEY)

def tts(save_path, input_text):
    print(f"Converting {input_text} to {save_path}")
    
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=input_text
    )

    response.stream_to_file(save_path)

    print(f"{save_path} created!")
