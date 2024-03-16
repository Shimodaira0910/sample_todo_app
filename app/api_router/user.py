from fastapi import APIRouter
from starlette.requests import Request
from ..bussiness.user_service import UserService
import json

router = APIRouter()
user_service = UserService()

#ユーザー登録エンドポイント
@router.post("register_user")
async def register_user(request: Request):
    user = json.loads(request)
    username = user['user_name']
    password = user['password']
    response = user_service.register_user(username, password)
    return response
    