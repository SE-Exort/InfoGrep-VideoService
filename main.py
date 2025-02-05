# encoding:utf-8

import os
import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from router import router
from InfoGrep_BackendSDK.middleware import TracingMiddleware, LoggingMiddleware
from InfoGrep_BackendSDK.infogrep_logger.logger import Logger

app = FastAPI()
service_logger = Logger("VideoServiceLogger")

os.environ["no_proxy"]="*"
os.environ['OBJC_DISABLE_INITIALIZE_FORK_SAFETY'] = 'YES'
origins = [
    "*",
]

app.add_middleware(TracingMiddleware)
app.add_middleware(LoggingMiddleware, logger=service_logger)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8879, log_level="info", host="0.0.0.0")