import os
from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from core.core_data import Entity


class DatabaseManager:

    def __init__(self):
        self._engine = None
        self.AsyncSessionFactory = None

    def __initialize(self) -> None:
        # Ensure the database directory exists
        db_path = "data/db"
        os.makedirs(db_path, exist_ok=True)
        
        self._engine = create_async_engine(
            "sqlite+aiosqlite:///data/db/project_analyzer.db",
            echo=True,
            poolclass=NullPool,
            connect_args={"check_same_thread": False}
        )
        self.AsyncSessionFactory = async_sessionmaker(bind=self._engine, expire_on_commit=False)

    @staticmethod
    def build() -> 'DatabaseManager':
        dm = DatabaseManager()
        dm.__initialize()
        return dm

    async def setup_entities(self):
        print('Creating tables')
        from business_requests import br_data
        from projects import projects_data

        async with self._engine.begin() as conn:
            await conn.run_sync(Entity.metadata.create_all)


database_manager: DatabaseManager = DatabaseManager.build()