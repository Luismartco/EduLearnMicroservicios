from flask_sqlalchemy import SQLAlchemy
from Domain.entities import Enrollment

db = SQLAlchemy()

class EnrollmentModel(db.Model):
    __tablename__ = "enrollments"

    id = db.Column(db.String, primary_key=True)
    student_id = db.Column(db.String, nullable=False)
    course_id = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    def to_entity(self):
        return Enrollment(
            id=self.id,
            student_id=self.student_id,
            course_id=self.course_id,
            created_at=self.created_at
        )

class EnrollmentRepository:
    def __init__(self, app=None):
        if app:
            self.init_app(app)

    def init_app(self, app):
        db.init_app(app)
        with app.app_context():
            db.create_all()

    def save(self, enrollment):
        model = EnrollmentModel(
            id=enrollment.id,
            student_id=enrollment.student_id,
            course_id=enrollment.course_id,
            created_at=enrollment.created_at,
        )
        db.session.add(model)
        db.session.commit()

    def get_enrollment(self, student_id, course_id):
        m = EnrollmentModel.query.filter_by(
            student_id=student_id,
            course_id=course_id
        ).first()
        return m.to_entity() if m else None

    def list_by_course(self, course_id):
        return [m.to_entity() for m in EnrollmentModel.query.filter_by(course_id=course_id).all()]

    def list_by_student(self, student_id):
        return [m.to_entity() for m in EnrollmentModel.query.filter_by(student_id=student_id).all()]
