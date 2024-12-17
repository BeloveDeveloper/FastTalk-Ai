from neurogram.domain.exceptions import user as user_exc
from neurogram.domain.exceptions import subcription as sub_exc
from starlette.responses import JSONResponse
from fastapi import Request


error_map = {
    user_exc.UserAlreadyExistsError: (409, "User already exists"),
    user_exc.AuthenticationError: (401, "Invalid login or password"),
    user_exc.RequestLimitExceededError: (429, "Request limit exceeded"),
    user_exc.UserDoesNotExistError: (404, "User does not exist"),
    user_exc.UserNotActiveError: (403, "User not active"),
    sub_exc.SubcriptionAlreadyExistsError: (409, "Subscription already exists")
}

async def generic_error_handler(request: Request, exc: Exception) -> JSONResponse:
    status_code, detail = error_map.get(type(exc), (500, "Internal Server Error"))
    return JSONResponse(status_code=status_code, content={"detail": detail})