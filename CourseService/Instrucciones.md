export FLASK_APP=Infrastructure.flask_app:app && flask run --port 5001
```
curl -X POST http://localhost:5100/api/courses \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Curso de DDD",
    "description": "Aprende DDD desde cero",
    "instructor_id": "<ID_DEL_PROFESOR>",
    "modules": [
      {"title":"Intro","content":"Bienvenida","order":1}
    ]
  }'
```