from flask import Flask
from Infrastructure.controllers import bp
from Infrastructure.repositories import EnrollmentRepository
from Infrastructure.auth_client import AuthClient
from Infrastructure.course_client import CourseClient
from Application.use_cases import EnrollmentServiceUseCases
from Infrastructure.config import SQLALCHEMY_DATABASE_URI

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    repo = EnrollmentRepository(app)
    auth = AuthClient()
    course = CourseClient()

    from Infrastructure import controllers
    controllers.repo = repo
    controllers.service = EnrollmentServiceUseCases(repo, auth, course)

    app.register_blueprint(bp)
    return app

app = create_app()

if __name__ == "__main__":
    app.run(port=5200, debug=True)
