from fastapi import Request
from starlette.responses import JSONResponse


async def error_response(
        request: Request,
        status_code: int,
        detail: str
) -> JSONResponse:
    return JSONResponse(status_code=status_code, content={"detail": detail})


async def user_already_exists_error(request: Request, exception: Exception) -> JSONResponse:
    return await error_response(request, 409, "User already exists")

async def authentication_error(request: Request, exception: Exception) -> JSONResponse:
    return await error_response(request, 401, "Invalid login or password")

async def request_limit_exceeded_error(request: Request, exception: Exception) -> JSONResponse:
    return await error_response(request, 429, "Request limit exceeded")

async def user_does_not_exist_error(request: Request, exception: Exception) -> JSONResponse:
    return await error_response(request, 404, "User does not exist")

async def user_not_active_error(request: Request, exception: Exception) -> JSONResponse:
    return await error_response(request, 403, "User not active")
