export FLASK_APP=Infrastructure.flask_app:app && flask run --port 5001
```
curl -X POST http://localhost:5002/api/courses \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Curso de DDD",
    "description": "Aprende DDD desde cero",
    "instructor_id": "242b8eb2-d655-47b9-8fe2-db4918af4f90",
    "modules": [
      {"title":"Intro","content":"Bienvenida","order":1}
    ]
  }'
```