from fastapi import APIRouter

router = APIRouter()

#テスト用エンドポイント
@router.get("/test_tasks")
async def test_tasks():
    return {"test_tasks": "OK!!!"}