from flask import Blueprint, request, jsonify
from Application.dtos import EnrollDTO
from Domain.exceptions import (
    EnrollmentAlreadyExists, UserNotFound,
    CourseNotFound, UserIsNotStudent
)

bp = Blueprint("enrollments", __name__, url_prefix="/api/enrollments")

repo = None
service = None

@bp.route("", methods=["POST"])
def enroll():
    global service
    data = request.get_json() or {}

    dto = EnrollDTO(
        student_id=data.get("student_id", ""),
        course_id=data.get("course_id", "")
    )

    try:
        enrollment = service.enroll(dto)
        return jsonify({
            "id": enrollment.id,
            "student_id": enrollment.student_id,
            "course_id": enrollment.course_id
        }), 201
    except UserNotFound:
        return jsonify({"error": "Student not found"}), 404
    except CourseNotFound:
        return jsonify({"error": "Course not found"}), 404
    except UserIsNotStudent:
        return jsonify({"error": "User must be student"}), 400
    except EnrollmentAlreadyExists:
        return jsonify({"error": "Student already enrolled"}), 409
