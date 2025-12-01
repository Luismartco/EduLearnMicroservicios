import uuid
from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Enrollment:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    student_id: str = ""
    course_id: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
