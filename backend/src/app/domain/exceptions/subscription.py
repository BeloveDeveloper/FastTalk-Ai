from .base import DomainError


class SubscriptionAlreadyExistsError(DomainError):
    pass

class SubscriptionDoesNotExistError(DomainError):
    pass
