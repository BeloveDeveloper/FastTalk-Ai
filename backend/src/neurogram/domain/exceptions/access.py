from .base import DomainError


class UserNotActiveError(DomainError):
    pass


class RequestLimitExceededError(DomainError):
    pass