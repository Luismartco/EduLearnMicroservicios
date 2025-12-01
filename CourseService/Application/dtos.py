from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class ModuleDTO:
    title: str
    content: str
    order: int = 0

@dataclass
class CreateCourseDTO:
    title: str
    description: str
    instructor_id: str
    modules: List[ModuleDTO] = field(default_factory=list)

@dataclass
class UpdateCourseDTO:
    title: Optional[str] = None
    description: Optional[str] = None
    modules: Optional[List[ModuleDTO]] = None
