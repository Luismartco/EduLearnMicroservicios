from flask import Blueprint, request, jsonify
from CourseService.Application.dtos import CreateCourseDTO, ModuleDTO, UpdateCourseDTO
from CourseService.Application.use_cases import CourseService
from CourseService.Infrastructure.repositories import CourseRepository
from CourseService.Domain.exceptions import CourseNotFound, UnauthorizedAction

bp = Blueprint('courses', __name__, url_prefix='/api/courses')

repo = None
service = None

@bp.route('', methods=['POST'])
def create_course():
    global repo, service
    data = request.get_json() or {}
    modules = [ModuleDTO(title=m.get('title',''), content=m.get('content',''), order=m.get('order',0)) for m in data.get('modules',[])]
    dto = CreateCourseDTO(title=data.get('title',''), description=data.get('description',''), instructor_id=data.get('instructor_id',''), modules=modules)
    try:
        course = service.create_course(dto)
        return jsonify({'id': course.id, 'title': course.title, 'description': course.description, 'instructor_id': course.instructor_id, 'published': course.published}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@bp.route('', methods=['GET'])
def list_courses():
    global repo, service
    only_published = request.args.get('published','true').lower() == 'true'
    courses = service.list_courses(only_published=only_published)
    out = []
    for c in courses:
        out.append({'id': c.id, 'title': c.title, 'description': c.description, 'instructor_id': c.instructor_id, 'published': c.published})
    return jsonify(out), 200

@bp.route('/<course_id>', methods=['GET'])
def get_course(course_id):
    global repo, service
    try:
        c = service.get_course(course_id)
        return jsonify({'id': c.id, 'title': c.title, 'description': c.description, 'instructor_id': c.instructor_id, 'published': c.published, 'modules': [{'id': m.id, 'title': m.title, 'content': m.content, 'order': m.order} for m in c.modules]}), 200
    except CourseNotFound as e:
        return jsonify({'error': str(e)}), 404

@bp.route('/<course_id>', methods=['PUT'])
def update_course(course_id):
    global repo, service
    data = request.get_json() or {}
    modules = None
    if 'modules' in data:
        modules = [ModuleDTO(title=m.get('title',''), content=m.get('content',''), order=m.get('order',0)) for m in data.get('modules',[])]
    dto = UpdateCourseDTO(title=data.get('title'), description=data.get('description'), modules=modules)
    actor_id = request.headers.get('X-Actor-Id','')  # simple actor check header for demo
    try:
        c = service.update_course(course_id, dto, actor_id)
        return jsonify({'id': c.id, 'title': c.title, 'description': c.description, 'published': c.published}), 200
    except CourseNotFound as e:
        return jsonify({'error': str(e)}), 404
    except UnauthorizedAction as e:
        return jsonify({'error': str(e)}), 403

@bp.route('/<course_id>/publish', methods=['POST'])
def publish_course(course_id):
    global repo, service
    actor_id = request.headers.get('X-Actor-Id','')
    try:
        c = service.publish_course(course_id, actor_id)
        return jsonify({'id': c.id, 'published': c.published}), 200
    except CourseNotFound as e:
        return jsonify({'error': str(e)}), 404
    except UnauthorizedAction as e:
        return jsonify({'error': str(e)}), 403
