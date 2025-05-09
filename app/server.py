
import logging
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from datetime import datetime, timedelta
from typing import Any, AsyncGenerator
from app.config import get_config
from app.core.error_handle import CustomException
from app.api import routers,middlewares
import app.db.session as session

# 配置日志格式
logging.basicConfig(
    level=logging.INFO,  # 设置日志级别
    format="%(levelname)s: [%(asctime)s] %(message)s",  # 日志格式
    datefmt="%Y-%m-%d %H:%M:%S",  # 自定义时间格式
)

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
   
    # scheduler.start()
    # 如果有其他初始化逻辑，可以在这里添加
    # 例如启动调度器、加载缓存等
    # scheduler.start()
    c = get_config("database")
    await session.init_db_pool(c)
    yield
    await session.close_db_pool()
    # scheduler.shutdown()
    # 关闭时：清理资源
    # scheduler.shutdown()  # 如果有调度器，可以在这里关闭

app = FastAPI(
    lifespan=lifespan,
    version=f"{datetime.now():%y-%m-%d %H:%M:%S}",
    root_path="/api",
    docs_url="/swagger",
    redoc_url=None,
)

app.state.logger = logging.getLogger("app")

for router in routers:
    app.include_router(router)

for middleware in middlewares:
    app.middleware("http")(middleware)

@app.exception_handler(CustomException)
async def unicorn_exception_handler(request: Request, exc: CustomException):
    code = 200
    if exc.err.code >= 500 and exc.err.code < 600:
        code = 500

    return JSONResponse(
        status_code=code,
        content= exc.toJson(),
    )