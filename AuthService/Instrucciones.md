### Registrar estudiante
```
curl -X POST http://localhost:5000/api/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "estudiante@correo.com",
    "password": "123456",
    "name": "Juan Estudiante"
  }'

```

### Registrar Docente
```
curl -X POST http://localhost:5000/api/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "profesor@correo.com",
    "password": "123456",
    "name": "María Profesora",
    "role": "teacher"
  }'
```

### Login
```
curl -X POST http://localhost:5000/api/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "profesor@correo.com",
    "password": "123456"
  }'
```flask run --port 5000