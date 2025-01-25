from sqlalchemy import Column, Integer, String, Boolean
from app.network.database import Base

class NetworkSegment(Base):
    __tablename__ = 'network_segments'

    id = Column(Integer, primary_key=True, index=True)
    segment = Column(String(length=18), nullable=False,unique=True)  # 存储网段
    sensitive_info_enabled = Column(Boolean, default=False)  # 敏感信息开关

    def __repr__(self):

        return f"<NetworkSegment(id={self.id}, segment={self.segment},sensitive_info_enabled={self.sensitive_info_enabled})>"
    #__repr__ 是 Python 中的一个特殊方法，用于定义对象的“官方”字符串表示形式。这个方法通常用于调试和日志记录，以便在打印对象时能够看到对象的有用信息。