from typing import Final
from app.core.rcode import ResponseModel

ERROR_SERVER: Final[ResponseModel] = ResponseModel(
    code=500,
    msg="服务器错误",
    data=None
)

ERROR_NOT_FOUND: Final[ResponseModel] = ResponseModel(
    code=404,
    msg="资源未找到",
    data=None
)

ERROR_QUERY: Final[ResponseModel] = ResponseModel(
    code=400,
    msg="查询参数错误",
    data=None
)

ERROR_PARAM: Final[ResponseModel] = ResponseModel(
    code=401,
    msg="路径参数错误",
    data=None
)

ERROR_BODY: Final[ResponseModel] = ResponseModel(
    code=402,
    msg="请求体参数错误",
    data=None
)
ERROR_NO_PROMISE: Final[ResponseModel] = ResponseModel(
    code=403,
    msg="权限不足",
    data=None
)