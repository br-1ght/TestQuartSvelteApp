from quart import Blueprint
from quart_auth import (
    login_user,
    logout_user,
    login_required,
    current_user
)
from quart_schema import validate_request

import sqlalchemy as sa

from backend.src.db_access.globals import async_session
from backend.src.models import (
    User,
    AuthedUser,
    LoginData
)

auth_bp = Blueprint('auth', __name__, url_prefix="/auth")


@auth_bp.post("/login")
@validate_request(LoginData)
async def login(data: LoginData):
    async with async_session() as session:
        statement = sa.select(User).where((User.email == data.username) & (User.password == data.password))
        result = await session.execute(statement)
        user = result.scalars().first()
        if user:
            login_user(AuthedUser(user.user_id))
            return {"message": "login success"}, 200
    return {"message": "invalid credentials"}, 401


@auth_bp.post("/logout")
@login_required
async def logout():
    logout_user()
    return {"message": "successful logout"}, 200


@auth_bp.get("/is-logged-in")
async def is_logged_in():
    if not await current_user.is_authenticated:
        return {"message": "not authenticated"}, 401

    return {
            "username": await current_user.username,
            "email": await current_user.email,
            "profile_pic": await current_user.profile_pic,
            "dark_mode": await current_user.dark_mode,
            "malware_scan": await current_user.malware_scan,
            "friends_only": await current_user.friends_only,
            "censor": await current_user.censor
    }


@auth_bp.get("/info")
@login_required
async def user_info():
    return {
        "username": await current_user.username,
        "email": await current_user.email,
        "profile_pic": await current_user.profile_pic,
        "dark_mode": await current_user.dark_mode,
        "malware_scan": await current_user.malware_scan,
        "friends_only": await current_user.friends_only,
        "censor": await current_user.censor
    }
