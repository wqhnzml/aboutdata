# services/user_service.py

def get_user_list():
    # 这里可以是数据库查询或其他业务逻辑
    
    return {"message": "----------User list"}
def get_user_details(user_id: int):
    # 这里可以是数据库查询或其他业务逻辑
    print("helloword")
    return {"message": f"User details for user with ID: {user_id}"}