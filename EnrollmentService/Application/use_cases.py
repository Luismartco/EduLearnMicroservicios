from Domain.entities import Enrollment
from Domain.exceptions import (
    EnrollmentAlreadyExists,
    CourseNotFound,
    UserNotFound,
    UserIsNotStudent
)

class EnrollmentServiceUseCases:
    def __init__(self, repo, auth_client, course_client):
        self.repo = repo
        self.auth = auth_client
        self.course = course_client

    def enroll(self, dto):
        # 1️⃣ Validar estudiante en AuthService
        student = self.auth.get_user(dto.student_id)
        if not student:
            raise UserNotFound("Student not found")

        if student.get("role") != "student":
            raise UserIsNotStudent("Only students can enroll")

        # 2️⃣ Validar curso en CourseService
        course = self.course.get_course(dto.course_id)
        if not course:
            raise CourseNotFound("Course not found")

        # 3️⃣ Validar no existe inscripción duplicada
        if self.repo.get_enrollment(dto.student_id, dto.course_id):
            raise EnrollmentAlreadyExists("Student already enrolled")

        enrollment = Enrollment(
            student_id=dto.student_id,
            course_id=dto.course_id
        )

        self.repo.save(enrollment)
        return enrollment

    def list_by_course(self, course_id):
        return self.repo.list_by_course(course_id)

    def list_by_student(self, student_id):
        return self.repo.list_by_student(student_id)
