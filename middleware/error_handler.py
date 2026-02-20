from fastapi import Request
from fastapi.responses import JSONResponse
from errors.custom_exceptions import BaseAppException


async def app_exception_handler(request: Request, exc: BaseAppException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.message},
    )