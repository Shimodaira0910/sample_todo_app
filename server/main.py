from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from api_router.user import router as user
# from api_router.tasks import router as tasks
# from api_router.auth import router as auth
from app.api_router.user import router as user
from server.app.api_router.tasks import router as tasks
from server.app.api_router.auth import router as auth


#FastAPIアプリケーション開始
app = FastAPI()

#CORS設定
origins = [
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(user)
app.include_router(tasks)
app.include_router(auth)