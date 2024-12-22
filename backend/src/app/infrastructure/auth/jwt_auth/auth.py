from app.application.interfaces.gateways.user import UserGateway
from app.application.interfaces.hasher import IPasswordHasher
from app.application.dto.user import UserLoginDTO
from app.domain.entities.user import User
from app.domain.exceptions.user import AuthenticationError
from app.infrastructure.auth.jwt_auth.jwt_service import JwtProcessor


class AuthService:
    def __init__(
            self,
            user_gateway: UserGateway,
            hasher: IPasswordHasher,
            jwt: JwtProcessor
    ) -> None:
        self.user_gateway = user_gateway
        self.hasher = hasher
        self.jwt = jwt

    async def _check_user(self, login_user: UserLoginDTO) -> User:
        user = await self.user_gateway.get_by_email(login_user.email)

        if not user:
            raise AuthenticationError
        if not self.hasher.verify(
            password=login_user.password, hashed_password=user.password
        ):
            raise AuthenticationError
        if not user.is_active:
            raise AuthenticationError

        return user

    async def authenticate(self, login_user: UserLoginDTO) -> str:
        user = await self._check_user(login_user)
        token = self.jwt.create_token(user)
        return token
