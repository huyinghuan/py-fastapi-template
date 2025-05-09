from fastapi import APIRouter

import app.api.error_code as error_code
from app.core.error_handle import CustomException
import app.core.rcode  as rcode

router = APIRouter()

@router.get("/version", tags=["version"], summary="Get API version")
async def get_version():
    """
    Get the version of the API.
    """
    return {"version": "1.0.0"}

@router.get("/test/error", tags=["version"], summary="Test error handling")
async def get_error():
    raise CustomException(error_code.ERROR_SERVER)

@router.get("/test/json", tags=["version"], summary="Test json response")
async def get_json():
    return rcode.success("test json")

@router.get("/test/json-list", tags=["version"], summary="Test json list")
async def get_json_list():
    return rcode.successList([1,2,34])