from dataclasses import dataclass

@dataclass
class RegisterDTO:
    email: str
    password: str
    name: str = ''
    role: str = 'student'

@dataclass
class LoginDTO:
    email: str
    password: str
