import requests

class AuthClient:
    BASE_URL = "http://http://127.0.0.1:5000/api"  # Cambia esto según tu deploy

    def get_user(self, user_id):
        resp = requests.get(f"{self.BASE_URL}/users/{user_id}")
        if resp.status_code != 200:
            return None
        return resp.json()
