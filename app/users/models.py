from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(length=255), unique=True, nullable=False)
    email = Column(String(length=255), unique=True, nullable=False)
    hashed_password = Column(String(length=255), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=255), unique=True, nullable=False)
    description = Column(String(length=255))

class UserIP(Base):
    __tablename__="user_ips"
    id=Column(Integer,primary_key=True,index=True)
    user_id = Column(Integer, nullable=False)  # 用户 ID，不使用外键
    ip_address = Column(String(length=45), nullable=False)  # IPv4 和 IPv6 地址
    subnet = Column(String(length=18), nullable=False)  # 子网掩码，例如 "192.168.1.0/24"

    def __repr__(self):
        return f"<UserIP(user_id={self.user_id}, ip_address={self.ip_address}, subnet={self.subnet})>"
