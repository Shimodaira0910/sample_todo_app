from fastapi import FastAPI
from api_router.user import router as user
from api_router.tasks import router as tasks
from api_router.auth import router as auth


#FastAPIアプリケーション開始ファイル
app = FastAPI()

app.include_router(user)
app.include_router(tasks)
app.include_router(auth)