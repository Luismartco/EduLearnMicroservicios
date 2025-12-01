from flask import Flask
from .controllers import bp
from .repositories import EnrollmentRepository
from .auth_client import AuthClient
from .course_client import CourseClient
from ..Application.use_cases import EnrollmentServiceUseCases
from .config import SQLALCHEMY_DATABASE_URI

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    repo = EnrollmentRepository(app)
    auth = AuthClient()
    course = CourseClient()

    from . import controllers
    controllers.repo = repo
    controllers.service = EnrollmentServiceUseCases(repo, auth, course)

    app.register_blueprint(bp)
    return app

app = create_app()

if __name__ == "__main__":
    app.run(port=5200, debug=True)
