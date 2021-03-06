from flask import (
    Flask,
    Response,
)
import json
import time

from dto import User

app = Flask(__name__)


@app.route("/v1/users/<int:user_id>", methods=['GET'])
def get_user(user_id):
    user = User()
    user.id = user_id
    user.username = UsernameService().process(user_id)
    user.name = NameService().process(user_id)
    user.twitter = TwitterService().process(user_id)

    return Response(json.dumps(user.__dict__), status=200, mimetype='application/json')


class UsernameService:

    def process(self, user_id):
        return 'ariel' if user_id == 1 else 'pepe'


class NameService:

    def process(self, user_id):
        return 'Ariel Parra' if user_id == 1 else 'Pepe Argento'


class TwitterService:

    def process(self, user_id):
        time.sleep(0.5)
        return '@darkaico' if user_id == 1 else '@pepeargento'


if __name__ == '__main__':
    app.run(debug=True)
