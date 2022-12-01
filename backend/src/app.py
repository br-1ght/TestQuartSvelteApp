import quart_auth
from quart import Quart, websocket
from quart_cors import cors

from backend.src.models.AuthedUser import AuthedUser
from blueprints.api import API_BP
from blueprints.user import USER_BP


app = Quart(__name__)
app = cors(app,
           allow_credentials=True,
           allow_origin=["http://localhost"])
auth_manager = quart_auth.AuthManager()
auth_manager.user_class = AuthedUser
auth_manager.init_app(app)
API_BP.register_blueprint(USER_BP)
app.register_blueprint(API_BP)
DEBUG = True
app.secret_key = "secret123"


@app.websocket("/ws")
async def ws():
    while True:
        data = await websocket.receive()
        print(data)
        await websocket.send(data)


@app.errorhandler(quart_auth.Unauthorized)
async def unauthorized(*_):
    return {"message": "Not authorized"}, 401

if __name__ == "__main__":
    app.run(debug=DEBUG, use_reloader=True)
