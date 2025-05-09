import argparse
from fastapi.responses import JSONResponse
import uvicorn
from fastapi import FastAPI, Request
from datetime import datetime, timedelta
from app.api import routers,middlewares
import logging

from app.core.error_handle import CustomException

# 配置日志格式
logging.basicConfig(
    level=logging.INFO,  # 设置日志级别
    format="%(levelname)s: [%(asctime)s] %(message)s",  # 日志格式
    datefmt="%Y-%m-%d %H:%M:%S",  # 自定义时间格式
)

app = FastAPI(
    # lifespan=lifespan,
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


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="示例命令行参数解析")
    parser.add_argument("--port", type=int, help="环境变量文件", default=8000)
    parser.add_argument(
        "--conf", type=str, help="配置文件", default="conf/conf.yaml")
    # load the environment variables from `.env` file
    args = parser.parse_args()

    uvicorn.run(
        app=app, port=args.port)
