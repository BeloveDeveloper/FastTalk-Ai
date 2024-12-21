import os
from typing import AsyncIterator

from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.application.interfaces.gateways.user import UserGateway
from app.application.interfaces.gateways.subscription import SubscriptionGateway
from app.application.interfaces.uow import UoW

from app.infrastructure.database.mappers.user import UserMapper
from app.infrastructure.database.mappers.subscription import SubcriptionMapper



class DatabaseProvider(Provider):
    @provide(scope=Scope.APP)
    def get_engine(self) -> AsyncEngine:
        engine = create_async_engine(
            os.getenv("DB_URL"),
            query_cache_size=1200,
            pool_size=20,
            max_overflow=200,
            future=True,
            echo=False,
        )
        return engine
    
    @provide(scope=Scope.APP)
    def get_session_pool(
            self, engine: AsyncEngine
    ) -> async_sessionmaker[AsyncSession]:
        session_pool = async_sessionmaker(bind=engine, expire_on_commit=False)
        return session_pool


    @provide(scope=Scope.REQUEST)
    async def get_session(
            self, session_pool: async_sessionmaker[AsyncSession]
    ) -> AsyncIterator[AsyncSession]:
        async with session_pool() as session:
            yield session

    @provide(scope=Scope.REQUEST, provides=UoW)
    async def get_uow(
            self, session: AsyncSession
    ) -> AsyncIterator[AsyncSession]:
        return session

    @provide(scope=Scope.REQUEST, provides=UserGateway)
    async def get_user_mapper(
            self, session: AsyncSession
    ) -> UserMapper:
        return UserMapper(session)
    
    @provide(scope=Scope.REQUEST, provides=SubscriptionGateway)
    async def get_subscription_mapper(
            self, session: AsyncSession
    ) -> SubcriptionMapper:
        return SubcriptionMapper(session)