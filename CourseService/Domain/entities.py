import uuid
from dataclasses import dataclass, field
from datetime import datetime
from typing import List

@dataclass
class Module:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    title: str = ""
    content: str = ""
    order: int = 0

@dataclass
class Course:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    title: str = ""
    description: str = ""
    instructor_id: str = ""
    modules: List[Module] = field(default_factory=list)
    published: bool = False
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)

    def add_module(self, module: Module):
        self.modules.append(module)
        self.updated_at = datetime.utcnow()

    def publish(self):
        self.published = True
        self.updated_at = datetime.utcnow()
