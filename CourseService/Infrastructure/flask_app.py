from flask import Flask
import os
from Infrastructure.auth_client import AuthClient
from Application.use_cases import CourseService
from Infrastructure.repositories import CourseRepository
from Infrastructure.controllers import bp
from Infrastructure.config import SQLALCHEMY_DATABASE_URI

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

    repo = CourseRepository(app)
    auth = AuthClient()

    from Infrastructure import controllers
    controllers.repo = repo
    controllers.service = CourseService(repo, auth)

    app.register_blueprint(bp)
    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT',5100)), debug=True)
