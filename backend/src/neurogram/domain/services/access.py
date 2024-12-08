from backend.src.neurogram.domain.entities.user import User
from backend.src.neurogram.domain.exceptions.access import RequestLimitExceededError, UserNotActiveError


class AccessService:
    def ensure_can_send_request(self, user: User):
        if not user.is_active:
            raise UserNotActiveError("User is not active")
        if user.total_req <= 0:
            raise RequestLimitExceededError("Request limit exceeded")
        return
    