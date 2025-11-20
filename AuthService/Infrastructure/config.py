import os
SECRET_KEY = os.environ.get('AUTH_SECRET', 'change_me_in_prod')
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///auth.db')
