from dotenv import load_dotenv
# 環境変数ファイルを読み込む
load_dotenv(verbose=True, dotenv_path='.env')

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api_router.user import router as user
from app.api_router.tasks import router as tasks
from app.api_router.auth import router as auth

#FastAPIアプリケーション開始
app = FastAPI()

#CORS設定

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user)
app.include_router(tasks)
app.include_router(auth)