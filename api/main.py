from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routers import task, file, appearing, appearing_detail, search, wiseword
from dotenv import load_dotenv
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# 環境変数を .env から読み込む。
dotenv_path = os.path.join(BASE_DIR, '.env')
load_dotenv(dotenv_path)
origin = os.environ.get("ALLOW_ORIGIN")
origin = origin.split(",")

app = FastAPI()
app.include_router(task.router)
app.include_router(file.router)
app.include_router(appearing.router)
app.include_router(appearing_detail.router)
app.include_router(search.router)
app.include_router(wiseword.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins = origin,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)
