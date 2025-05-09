from app.api.version import router as version_router

from app.api.middle.global_middle import custom_response_middleware
# 将所有路由统一暴露
routers = [
    version_router
]

middlewares = [
    custom_response_middleware
]