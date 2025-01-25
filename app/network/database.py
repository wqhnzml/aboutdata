from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from settings.settings_dev import DATABASE_URL  # 从配置文件中导入数据库连接字符串

# 创建数据库引擎
# `create_engine` 函数用于创建一个新的 SQLAlchemy 引擎实例。
# 这个引擎将用于与数据库进行交互。
engine = create_engine(DATABASE_URL)

# 创建数据库会话工厂
# `sessionmaker` 是一个工厂函数，用于创建新的数据库会话。
# `autocommit=False` 表示在每次操作后不自动提交事务。
# `autoflush=False` 表示在查询之前不自动刷新会话。
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 创建基础类
# `declarative_base` 函数用于创建一个基础类，所有的模型类都应该继承这个基础类。
Base = declarative_base()

# 获取数据库会话的依赖项
def get_db() -> Session:
    """
    生成一个数据库会话的依赖项。
    使用 FastAPI 的依赖注入机制，确保在请求处理期间创建和关闭会话。
    """
    db = SessionLocal()  # 创建一个新的数据库会话
    try:
        yield db  # 将会话返回给请求处理
    finally:
        db.close()  # 请求处理完成后关闭会话
