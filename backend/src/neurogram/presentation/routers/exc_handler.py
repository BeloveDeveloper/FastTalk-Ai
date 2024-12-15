from fastapi import Request
from starlette.responses import JSONResponse


async def user_alredy_exists_error(
        request: Request,
        exception: Exception
) -> JSONResponse:
    return JSONResponse(status_code=409, content={"detail": "User alredy exists"})

async def authentication_error(
        request: Request,
        exception: Exception
):
    return JSONResponse(status_code=429, content={"detail": "Invalid login or password"})

async def request_limit_exceeded_error(
        request: Request,
        exception: Exception
):
    return JSONResponse(status_code=401, content={"detail": "Request limit exceeded"})

async def user_does_not_exist_error(
        request: Request,
        exception: Exception
):
    return JSONResponse(status_code=404, content={"detail": "User does not exist"})

async def user_not_active_error(
        request: Request,
        exception: Exception
):
    return JSONResponse(status_code=403, content={"detail": "User not active"})
