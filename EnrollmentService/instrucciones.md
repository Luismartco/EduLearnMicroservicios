$ curl -X POST http://localhost:5003/api/enrollments   -H "Content-Type: application/json"   -d '{
    "student_id": "d9843ce5-2e37-4454-9bf3-4da11838157c",
    "course_id": "ffec93c8-574a-4d4e-a38b-d468b49634ad"
  }'
{"course_id":"ffec93c8-574a-4d4e-a38b-d468b49634ad","id":"3ca50ae4-9e34-4440-8446-804a0a4a9f4f","student_id":"d9843ce5-2e37-4454-9bf3-4da11838157c"}