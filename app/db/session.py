import logging
import aiomysql
from typing import AsyncGenerator

log = logging.getLogger("db:session")
# 全局连接池
mysql_pool: aiomysql.Pool = None

async def init_db_pool(conf:dict):
    """初始化 MySQL 连接池"""
    global mysql_pool
    mysql_pool = await aiomysql.create_pool(**conf)
     
    # 测试连接
    async with mysql_pool.acquire() as conn:
        async with conn.cursor() as cursor:
            await cursor.execute("SELECT 1")
            result = await cursor.fetchone()
            if result is None or result[0] != 1:
                raise Exception("MySQL 测试查询失败")

    log.info("MySQL 连接池初始化成功")

async def close_db_pool():
    """关闭 MySQL 连接池"""
    global mysql_pool
    if mysql_pool:
        mysql_pool.close()
        await mysql_pool.wait_closed()

async def get_db() -> AsyncGenerator[aiomysql.Connection, None]:
    """获取一个数据库连接"""
    global mysql_pool
    async with mysql_pool.acquire() as conn:
        yield conn