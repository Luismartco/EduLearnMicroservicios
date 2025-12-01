from flask import Blueprint, request, jsonify
from Application.dtos import RegisterDTO, LoginDTO
from Application.use_cases import AuthService
from Infrastructure.repositories import UserRepository
from Domain.exceptions import UserAlreadyExists, InvalidCredentials

bp = Blueprint('auth', __name__, url_prefix='/api')

# repo and service will be injected by the app factory
repo = None
service = None

@bp.route('/register', methods=['POST'])
def register():
    global repo, service
    data = request.get_json() or {}
    dto = RegisterDTO(
        email=data.get('email',''),
        password=data.get('password',''),
        name=data.get('name',''),
        role=data.get('role','student')
    )
    try:
        user = service.register(dto)
        return jsonify({'id': user.id, 'email': user.email, 'name': user.name}), 201
    except UserAlreadyExists as e:
        return jsonify({'error': str(e)}), 400
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@bp.route('/login', methods=['POST'])
def login():
    global repo, service
    data = request.get_json() or {}
    dto = LoginDTO(email=data.get('email',''), password=data.get('password',''))
    try:
        token = service.login(dto)
        return jsonify({'token': token}), 200
    except InvalidCredentials as e:
        return jsonify({'error': str(e)}), 401

@bp.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    global repo, service
    user = service.get_user(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify({
        'id': user.id,
        'email': user.email,
        'name': user.name,
        'role': user.role
    }), 200
