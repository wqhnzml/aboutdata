# services/user_service.py
from fastapi import HTTPException


def get_user_list(username:str):
    # 这里可以是数据库查询或其他业务逻辑
    print("-----",username)
    fake_users_db = {
        "user1": {"username": "user1", "email": "user1@example.com"},
        "user2": {"username": "user2", "email": "user2@example.com"}
    }
    user = fake_users_db.get(username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user



def get_user_details(username: int):
    # 这里可以是数据库查询或其他业务逻辑
    print("helloword")

    fake_users_db = {
        "user1": {"username": "user1", "email": "user1@example.com"},
        "user2": {"username": "user2", "email": "user2@example.com"}
    }

    return {"message": f"User details for user with ID: {fake_users_db.get('user1')}"}