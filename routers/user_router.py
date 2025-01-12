
# routers/user.py
from fastapi import APIRouter
from app.users.users import get_user_list

router = APIRouter() #总路由页面

@router.get("/")
async def get_users():
    print('用户总路由')
    return get_user_list()

# @router.get("/{user_id}")
# async def get_user(user_id: int):
#     return get_user_details(user_id)