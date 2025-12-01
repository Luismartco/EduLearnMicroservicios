from Domain.exceptions import UnauthorizedAction

class CourseService:
    def __init__(self, repo, auth_client):
        self.repo = repo
        self.auth = auth_client

    def create_course(self, dto):
        # 1️⃣ Consultar AuthService
        user = self.auth.get_user(dto.instructor_id)

        if not user:
            raise UnauthorizedAction("Instructor no existe")

        if user["role"] != "teacher":
            raise UnauthorizedAction("Solo los profesores pueden crear cursos")

        # 2️⃣ Crear curso si el usuario es válido
        course = Course(
            title=dto.title,
            description=dto.description,
            instructor_id=dto.instructor_id
        )

        for m in dto.modules:
            module = Module(title=m.title, content=m.content, order=m.order)
            course.add_module(module)

        self.repo.save(course)
        return course
