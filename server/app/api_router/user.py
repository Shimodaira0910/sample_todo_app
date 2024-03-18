import sys
import os
from fastapi import APIRouter
from starlette.requests import Request
import json
from ..business.user_service import UserService

router = APIRouter()
user_service = UserService()

#ユーザー登録エンドポイント
@router.post("register")
async def register_user(request: Request):
    user = json.loads(request)
    username = user['user_name']
    password = user['password']
    response = user_service.register_user(username, password)
    return response
    
