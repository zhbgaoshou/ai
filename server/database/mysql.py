from sqlalchemy.ext.asyncio import create_async_engine
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("MYSQL_URL")
engine = create_async_engine(
    DATABASE_URL,
    pool_size=10,  # 设置连接池的最大连接数
    max_overflow=20,  # 允许的最大溢出连接数
    pool_timeout=30,  # 获取连接的超时时间
    pool_recycle=1800,  # 连接回收时间（秒），防止连接闲置太久被数据库关闭
    pool_pre_ping=True,  # 检查连接的可用性
)
