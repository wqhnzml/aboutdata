
# routers/user.py
from fastapi import APIRouter
from app.users.users import get_user_list

router = APIRouter(
    prefix="/users",
    tags=["users"]
)


# 路由只负责调用服务层，保持清晰
@router.get("/{useranme}/")
async def get_users(username=str):   #动态路径有参数此处需要传参数
    print("用户子路由部分",username)
    return get_user_list(username)

# @router.get("/{user_id}")
# async def get_user(user_id: int):
#     return get_user_details(user_id)