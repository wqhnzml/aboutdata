import os

# 数据库连接字符串
DATABASE_URL = os.getenv("DATABASE_URL", 
                         "mysql+pymysql://user:password@localhost:3306/db_name")