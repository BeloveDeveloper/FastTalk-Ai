from app.domain.exceptions import user as user_exc
from app.domain.exceptions import subscription as sub_exc
from starlette.responses import JSONResponse
from fastapi import Request


error_map = {
    user_exc.UserAlreadyExistsError: (409, "User already exists"),
    user_exc.AuthenticationError: (401, "Invalid login or password"),
    user_exc.RequestLimitExceededError: (429, "Request limit exceeded"),
    user_exc.UserDoesNotExistError: (404, "User does not exist"),
    user_exc.UserNotActiveError: (403, "User not active"),
    sub_exc.SubscriptionAlreadyExistsError: (409, "Subscription already exists"),
    sub_exc.SubscriptionDoesNotExistError: (404, "Subscription does not exist"),
    sub_exc.TokenNotFoundError: (401, "Token not found"),
}


async def generic_error_handler(request: Request, exc: Exception) -> JSONResponse:
    status_code, detail = error_map.get(type(exc), (500, "Internal Server Error"))
    return JSONResponse(status_code=status_code, content={"detail": detail})
