from flask_sqlalchemy import SQLAlchemy
from Domain.entities import User
db = SQLAlchemy()

class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=True)
    role = db.Column(db.String, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False)

    def to_entity(self):
        from Domain.entities import User
        u = User(id=self.id, email=self.email, password_hash=self.password_hash, name=self.name, role=self.role, created_at=self.created_at)
        return u

class UserRepository:
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        db.init_app(app)
        with app.app_context():
            db.create_all()

    def save(self, user: User):
        um = UserModel.query.get(user.id)
        if not um:
            um = UserModel(id=user.id)
        um.email = user.email
        um.password_hash = user.password_hash
        um.name = user.name
        um.role = user.role
        um.created_at = user.created_at
        db.session.add(um)
        db.session.commit()
        return um.to_entity()

    def find_by_email(self, email: str):
        um = UserModel.query.filter_by(email=email).first()
        return um.to_entity() if um else None
