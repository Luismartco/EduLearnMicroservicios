import requests
import os

class AuthClient:
    BASE_URL = os.environ.get('AUTH_SERVICE_URL', 'http://localhost:5001/api')

    def get_user(self, user_id):
        resp = requests.get(f"{self.BASE_URL}/users/{user_id}")
        if resp.status_code != 200:
            return None
        return resp.json()
