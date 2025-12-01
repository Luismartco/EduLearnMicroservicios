from dataclasses import dataclass

@dataclass(frozen=True)
class CourseSummary:
    title: str
    short_description: str
