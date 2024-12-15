from fastapi import FastAPI

from neurogram.presentation.routers.root import root_router
from neurogram.domain.exceptions import user as user_exc
from neurogram.presentation.routers.exc_handler import (
    user_already_exists_error,
    authentication_error,
    request_limit_exceeded_error,
    user_does_not_exist_error,
    user_not_active_error
)


def init_routers(app: FastAPI) -> None:
    app.include_router(root_router)

def register_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(
        user_exc.UserAlreadyExistsError, user_already_exists_error
    )
    app.add_exception_handler(
        user_exc.AuthenticationError, authentication_error
    )
    app.add_exception_handler(
        user_exc.RequestLimitExceededError, request_limit_exceeded_error
    )
    app.add_exception_handler(
        user_exc.UserDoesNotExistError, user_does_not_exist_error
    )
    app.add_exception_handler(
        user_exc.UserNotActiveError, user_not_active_error
    )
