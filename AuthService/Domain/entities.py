import uuid
from datetime import datetime
from dataclasses import dataclass, field

VALID_ROLES = ["student", "teacher"] 

@dataclass
class User:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    email: str = ""
    password_hash: str = ""
    name: str = ""
    role: str = "student" 
    created_at: datetime = field(default_factory=datetime.utcnow)

    def __post_init__(self):
        if self.role not in VALID_ROLES:
            raise ValueError(f"Invalid role '{self.role}'. Valid roles: {VALID_ROLES}")
