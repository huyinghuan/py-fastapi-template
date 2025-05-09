from typing import Generic, TypeVar, Optional
from pydantic import BaseModel

class Page(BaseModel):
    """
    分页参数
    """
    page: int = 1  # 当前页码
    page_size: int = 10  # 每页大小
    total: int = 0  # 总记录数
    total_page: int = 0  # 总页数

    def calcu(self, total: int) -> None:
        """
        计算总页数
        """
        self.total = total
        if total % self.page_size == 0:
            self.total_page = total // self.page_size
        else:
            self.total_page = total // self.page_size + 1

# 定义泛型类型
T = TypeVar("T")

class ResponseModel(BaseModel, Generic[T]):
    code: int = 0  # 状态码
    msg: str = "success"  # 消息
    data: Optional[T] = None  # 数据，默认为 None

    def append_msg(self, extra_msg: str) -> "ResponseModel[T]":
        """
        返回一个新的 ResponseModel 对象，其中 msg 为 extra_msg 加上原对象的 msg 值。
        """
        return ResponseModel(
            code=self.code,
            msg=f"{self.msg}:{extra_msg}",
            data=self.data
        )
    
def success(data: Optional[T] = None) -> ResponseModel[T]:
    """
    返回一个成功的 ResponseModel 对象。
    """
    return ResponseModel(code=0, msg="success", data=data)

def successList(data: Optional[T] = None, page: Page = None) -> ResponseModel[T]:
    """
    返回一个成功的 ResponseModel 对象，数据为列表。
    """
    return ResponseModel(code=0, msg="success", data=dict(
        list=data,
        page=page
    ))