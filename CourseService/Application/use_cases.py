from CourseService.Domain.exceptions import UnauthorizedAction
from CourseService.Domain.entities import Course, Module

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

    def list_courses(self, only_published=True):
        return self.repo.list_all(only_published=only_published)

    def get_course(self, course_id):
        from CourseService.Domain.exceptions import CourseNotFound
        course = self.repo.get_by_id(course_id)
        if not course:
            raise CourseNotFound(f"Curso {course_id} no encontrado")
        return course

    def update_course(self, course_id, dto, actor_id):
        from CourseService.Domain.exceptions import CourseNotFound
        course = self.repo.get_by_id(course_id)
        if not course:
            raise CourseNotFound(f"Curso {course_id} no encontrado")
        
        # Verificar que el actor sea el instructor del curso
        if course.instructor_id != actor_id:
            raise UnauthorizedAction("Solo el instructor puede actualizar el curso")
        
        # Actualizar campos si se proporcionan
        if dto.title is not None:
            course.title = dto.title
        if dto.description is not None:
            course.description = dto.description
        if dto.modules is not None:
            course.modules = []
            for m in dto.modules:
                module = Module(title=m.title, content=m.content, order=m.order)
                course.add_module(module)
        
        self.repo.save(course)
        return course

    def publish_course(self, course_id, actor_id):
        from CourseService.Domain.exceptions import CourseNotFound
        course = self.repo.get_by_id(course_id)
        if not course:
            raise CourseNotFound(f"Curso {course_id} no encontrado")
        
        # Verificar que el actor sea el instructor del curso
        if course.instructor_id != actor_id:
            raise UnauthorizedAction("Solo el instructor puede publicar el curso")
        
        course.publish()
        self.repo.save(course)
        return course
