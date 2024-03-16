from fastapi import APIRouter
from starlette.requests import Request
import json

router = APIRouter()

#テスト用エンドポイント
@router.get("/test_user")
async def test_user():
    return {"test": "OK!!"}

#ユーザー登録エンドポイント
@router.post("register_user")
async def register_user(request: Request):
    received_user_data = json.loads(request)
    