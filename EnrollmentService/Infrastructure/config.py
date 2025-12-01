import os

# Crear la carpeta instance dentro de EnrollmentService si no existe
INSTANCE_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'instance')
os.makedirs(INSTANCE_PATH, exist_ok=True)

# Configurar la ruta de la base de datos
DB_PATH = os.path.join(INSTANCE_PATH, 'enrollment.db')
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', f'sqlite:///{DB_PATH}')