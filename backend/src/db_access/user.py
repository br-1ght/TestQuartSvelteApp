from .globals import async_session
import sqlalchemy as sa

from ..models import User


async def get_user_details(user_id):
    async with async_session as session:
        statement = sa.select(User.email,
                              User.profile_pic,
                              User.dark_mode,
                              User.malware_scan,
                              User.friends_only,
                              User.censor).where(User.id == user_id)
        result = await session.execute(statement)
        return result.scalars().first()

