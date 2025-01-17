import os
from typing import AsyncIterator

from dishka import Provider, Scope, from_context, provide
from fastapi import Request
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from redis.asyncio import ConnectionPool, Redis

from app.infrastructure.database.mappers.chat import ChatMapper
from app.application.interfaces.gateways.chat import ChatGateway
from app.application.interfaces.gateways.user import UserGateway
from app.application.interfaces.gateways.subscription import SubscriptionGateway
from app.application.interfaces.uow import UoW
from app.infrastructure.auth.jwt_auth.password_hasher import PasswordHasher
from app.infrastructure.auth.jwt_auth.auth import AuthService
from app.infrastructure.auth.jwt_auth.jwt_service import JwtProcessor, TokenPayloadDTO
from app.infrastructure.auth.jwt_auth.jwt_id_provider import TokenIdProvider
from app.infrastructure.database.mappers.user import UserMapper
from app.infrastructure.database.mappers.subscription import SubcriptionMapper
from app.domain.exceptions.subscription import TokenNotFoundError


class AuthProvider(Provider):
    request = from_context(provides=Request, scope=Scope.REQUEST)

    @provide(scope=Scope.APP)
    def get_password_hasher(self) -> PasswordHasher:
        return PasswordHasher()

    @provide(scope=Scope.APP)
    def get_jwt_service(self) -> JwtProcessor:
        return JwtProcessor(private_key=os.getenv("JWT_SECRET"), algorithm="HS256")

    @provide(scope=Scope.REQUEST)
    def get_token_id_provider(self, token: TokenPayloadDTO) -> TokenIdProvider:
        return TokenIdProvider(token=token)

    @provide(scope=Scope.REQUEST)
    def get_token(
        self, request: Request, token_processor: JwtProcessor
    ) -> TokenPayloadDTO:
        token = request.cookies.get("access_token")
        if not token:
            raise TokenNotFoundError
        return token_processor.decode_jwt(token)

    @provide(scope=Scope.REQUEST)
    async def get_auth_service(
        self,
        user_gateway: UserGateway,
        hasher: PasswordHasher,
        jwt: JwtProcessor,
    ) -> AuthService:
        return AuthService(user_gateway, hasher, jwt)


class DatabaseProvider(Provider):
    @provide(scope=Scope.APP)
    def get_engine(self) -> AsyncEngine:
        engine = create_async_engine(
            os.getenv("DB_URL"),
            query_cache_size=1200,
            pool_size=10
            ,
            max_overflow=2,
            future=True,
            echo=False,
        )
        return engine

    @provide(scope=Scope.APP)
    def get_session_pool(self, engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
        session_pool = async_sessionmaker(bind=engine, expire_on_commit=False)
        return session_pool

    @provide(scope=Scope.REQUEST)
    async def get_session(
        self, session_pool: async_sessionmaker[AsyncSession]
    ) -> AsyncIterator[AsyncSession]:
        async with session_pool() as session:
            yield session

    @provide(scope=Scope.REQUEST, provides=UoW)
    async def get_uow(self, session: AsyncSession) -> AsyncIterator[AsyncSession]:
        return session


class RedisProvider(Provider):
    @provide(scope=Scope.APP)
    def get_connection_pool(self) -> ConnectionPool: 
        redis_url = os.getenv('REDIS_URL')
        connection_pool = ConnectionPool.from_url(redis_url)
        return connection_pool

    @provide(scope=Scope.REQUEST)
    async def get_connection(self, connection_pool: ConnectionPool) -> Redis:
        connection = Redis(connection_pool=connection_pool, decode_responses=True)
        return connection


class MapperProvider(Provider):
    @provide(scope=Scope.REQUEST, provides=UserGateway)
    async def get_user_mapper(self, session: AsyncSession) -> UserMapper:
        return UserMapper(session)

    @provide(scope=Scope.REQUEST, provides=SubscriptionGateway)
    async def get_subscription_mapper(self, session: AsyncSession, cache: Redis) -> SubcriptionMapper:
        return SubcriptionMapper(session, cache)

    @provide(scope=Scope.REQUEST, provides=ChatGateway)
    async def get_chat_mapper(self, session: AsyncSession) -> ChatMapper:
        return ChatMapper(session)


class InfrastructureProvider(AuthProvider, DatabaseProvider, RedisProvider, MapperProvider): ...
