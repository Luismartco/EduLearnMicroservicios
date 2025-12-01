import requests

class CourseClient:
    BASE_URL = "http://localhost:5002/api/courses"

    def get_course(self, course_id):
        resp = requests.get(f"{self.BASE_URL}/{course_id}")
        if resp.status_code != 200:
            return None
        return resp.json()
