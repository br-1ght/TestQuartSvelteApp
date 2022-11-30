import asyncio
from sqlalchemy import select
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
)
from sqlalchemy.orm import sessionmaker
from backend.src.models import Base, User, Room


DEBUG = False
connection_string = "mysql+asyncmy://bubbles:bubbles@localhost:3306/bubbles"
engine = create_async_engine(connection_string, echo=DEBUG)
async_session = sessionmaker(engine, class_=AsyncSession)
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())  # Windows specific issue https://stackoverflow.com/questions/61543406/asyncio-run-runtimeerror-event-loop-is-closed


async def main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    async with async_session() as session:
        async with session.begin():
            session.add(User("bob", "bob@gmail.com", "bob123"))
            session.add(User("alice", "alice@yahoo.com", "alice456"))


async def query():
    async with async_session() as session:
        stmt = select(User)
        result = await session.execute(stmt)
        for item in result.scalars():
            print(item.username)


asyncio.run(query())
