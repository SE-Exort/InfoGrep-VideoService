from fastapi import APIRouter, Request

router = APIRouter()

@router.post("/visual")
async def text_to_visual(request: Request):
    """ Demo Plan
    - chunk with NLTK, and randomly selects a sentence or two for demoing the video aspect
    - keyword extract with image, and then demo the image part and key phrase
    """
    
    try:
        data = await request.json()
        text_file_path = data["text_file_url"]

        print("Start processing for: ", text_file_path, end="\n\n")

        return {
            "status": 200,
            "payload": {}
        }
    
    except Exception as e:
        print(f"Error occured: {str(e)}")
        return {
            "status": 500,
            "payload": {}
        }