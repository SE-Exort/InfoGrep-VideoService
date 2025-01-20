from fastapi import APIRouter, Request

router = APIRouter()

@router.post("/test")
async def test(request: Request):
    print(request.headers)
    return {
        "status": 200,
        "payload": "test request received"
    }
