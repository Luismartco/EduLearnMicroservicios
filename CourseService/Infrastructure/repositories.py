from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

db = SQLAlchemy()

class CourseModel(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.String, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)
    instructor_id = db.Column(db.String, nullable=False)
    modules = db.Column(db.Text, nullable=True)  # JSON list
    published = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

    def to_entity(self):
        from CourseService.Domain.entities import Course, Module
        data = json.loads(self.modules) if self.modules else []
        modules = [Module(id=m.get('id'), title=m.get('title'), content=m.get('content'), order=m.get('order')) for m in data]
        c = Course(id=self.id, title=self.title, description=self.description, instructor_id=self.instructor_id, modules=modules, published=self.published, created_at=self.created_at, updated_at=self.updated_at)
        return c

class CourseRepository:
    def __init__(self, app=None):
        if app:
            self.init_app(app)

    def init_app(self, app):
        db.init_app(app)
        with app.app_context():
            db.create_all()

    def save(self, course):
        cm = CourseModel.query.get(course.id)
        import json
        if not cm:
            cm = CourseModel(id=course.id, created_at=course.created_at)
        cm.title = course.title
        cm.description = course.description
        cm.instructor_id = course.instructor_id
        cm.modules = json.dumps([{'id': m.id, 'title': m.title, 'content': m.content, 'order': m.order} for m in course.modules])
        cm.published = course.published
        cm.updated_at = course.updated_at
        db.session.add(cm)
        db.session.commit()
        return cm.to_entity()

    def list_all(self, only_published=True):
        q = CourseModel.query
        if only_published:
            q = q.filter_by(published=True)
        models = q.all()
        return [m.to_entity() for m in models]

    def get_by_id(self, course_id: str):
        cm = CourseModel.query.get(course_id)
        return cm.to_entity() if cm else None
