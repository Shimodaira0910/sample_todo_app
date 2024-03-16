from fastapi import APIRouter

router = APIRouter()

#テスト用エンドポイント
@router.get("/test_auth")
async def test_auth():
    return {"test_auth": "OK!!!"}