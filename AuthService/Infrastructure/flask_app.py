from flask import Flask
from Infrastructure.controllers import bp
from Infrastructure.repositories import UserRepository
from Infrastructure.config import SQLALCHEMY_DATABASE_URI, SECRET_KEY
import os

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = SECRET_KEY

    # init repository (and create DB tables)
    user_repo = UserRepository(app)

    # inject repo and service into controllers
    from Infrastructure import controllers
    controllers.repo = user_repo
    from Application.use_cases import AuthService
    controllers.service = AuthService(user_repo)

    # register routes
    app.register_blueprint(bp)
    return app

# create app for flask CLI / gunicorn
app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT',5000)), debug=True)
