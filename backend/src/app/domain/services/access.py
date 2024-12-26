from app.domain.entities.user_id import UserId
from app.domain.entities.user import User
from app.domain.exceptions.user import (
    AuthenticationError,
    RequestLimitExceededError,
    UserNotActiveError,
)


class AccessService:
    def ensure_can_send_message(self, user: User) -> None:
        if not user.is_active:
            raise UserNotActiveError
        if user.total_req <= 0:
            raise RequestLimitExceededError
        return

    def ensure_can_chat(self, user_id: UserId, chat_owner_id: int) -> None:
        if user_id != chat_owner_id:
            raise AuthenticationError
        return
