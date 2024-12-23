from .base import DomainError


class UserAlreadyExistsError(DomainError):
    pass


class AuthenticationError(DomainError):
    pass


class RequestLimitExceededError(DomainError):
    pass


class UserNotActiveError(DomainError):
    pass


class UserDoesNotExistError(DomainError):
    pass
