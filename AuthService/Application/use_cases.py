from Domain.entities import User
from Domain.value_objects import Email
from Domain.exceptions import UserAlreadyExists, InvalidCredentials
from Infrastructure.repositories import UserRepository
from passlib.hash import bcrypt
import jwt, datetime
from Infrastructure.config import SECRET_KEY

class AuthService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def register(self, dto):
        Email(dto.email)

        if self.repo.find_by_email(dto.email):
            raise UserAlreadyExists('User with email exists')

        user = User(
            email=dto.email,
            password_hash=bcrypt.hash(dto.password),
            name=dto.name,
            role=dto.role  # 🔥 Agregado
        )

        self.repo.save(user)
        return user

    def login(self, dto):
        user = self.repo.find_by_email(dto.email)
        if not user or not bcrypt.verify(dto.password, user.password_hash):
            raise InvalidCredentials('Invalid email or password')
        payload = {
            'sub': user.id,
            'email': user.email,
            'role': user.role,  # 🔥 Se agrega el rol al token
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=8)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        # PyJWT returns str in newer versions; if bytes, decode accordingly in older versions
        if isinstance(token, bytes):
            token = token.decode('utf-8')
        return token
