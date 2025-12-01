import requests
import os

class AuthClient:
<<<<<<< HEAD
    # Usar variable de entorno o localhost por defecto para desarrollo
    BASE_URL = os.environ.get('AUTH_SERVICE_URL', 'http://localhost:5001/api')
=======
    BASE_URL = "http://127.0.0.1:5000/api"  # Cambia esto según tu deploy
>>>>>>> 66ad546f77ba7c7016ab860150bde84164e06244

    def get_user(self, user_id):
        try:
            resp = requests.get(f"{self.BASE_URL}/users/{user_id}", timeout=5)
            if resp.status_code != 200:
                return None
            return resp.json()
        except requests.exceptions.RequestException as e:
            print(f"Error connecting to AuthService: {e}")
            return None
