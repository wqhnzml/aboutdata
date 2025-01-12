# app/router.py

from fastapi import APIRouter
from app.users.router import router as user_router

# 创建总路由
api_router = APIRouter()
api_router.include_router(user_router)  #用户总路由