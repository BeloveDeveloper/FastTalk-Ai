from app.application.interfaces.id_provider import IdProvider
from app.domain.entities.user_id import UserId
from app.infrastructure.auth.jwt_auth.jwt_service import TokenPayloadDTO


class TokenIdProvider(IdProvider):
    def __init__(self, token: TokenPayloadDTO) -> None:
        self.token = token

    def get_current_user_id(self) -> UserId:
        return self.token.sub
