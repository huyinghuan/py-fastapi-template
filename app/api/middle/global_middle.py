from fastapi import Request
import logging



async def custom_response_middleware(request: Request, call_next):
    """
    全局响应拦截器：统一包装返回数据
    """
    response = await call_next(request)
    # 统一处理响应数据
    # logger = request.app.state.logger  # 获取日志记录器
    # logger.info(f"Processing request: {request.method} {request.url}")
    return response
