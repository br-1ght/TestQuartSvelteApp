from hmac import compare_digest
from backend.src.blueprints.user.models.LoginData import LoginData

from quart import Blueprint
from quart_auth import (
    login_user,
    logout_user,
    AuthUser,
    login_required, current_user
)
from quart_schema import validate_request

USER_BP = Blueprint('user', __name__, url_prefix="/user")
DB = [
    {
        "id": "1",
        "username": "bob",
        "email": "bob@gmail.com",
        "password": "password123"
    },
    {
        "id": "2",
        "username": "alice",
        "email": "alice@gmail.com",
        "password": "hello456"
    }
]


@USER_BP.post("/login")
@validate_request(LoginData)
async def login(data: LoginData):
    global DB
    for entry in DB:
        if data.username == entry['username'] and compare_digest(data.password, entry['password']):
            login_user(AuthUser(entry['id']))
            return {"message": "login success"}, 200
    return {"message": "invalid credentials"}, 401


@USER_BP.post("/logout")
@login_required
async def logout():
    logout_user()
    return {"message": "successful logout"}, 200


@USER_BP.get("/is-logged-in")
async def is_logged_in():
    if await current_user.is_authenticated:
        return {"message": "user authenticated",
                "user": {
                    "user_id": current_user.auth_id,
                    "is_authenticated": True
                }}
    return {"message": "not authenticated"}
