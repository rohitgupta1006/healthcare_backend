# Healthcare Backend – Django REST Framework

Assignment implementation for the Full Stack Intern round.

## Stack
- Python / Django
- Django REST Framework
- PostgreSQL
- JWT authentication with `djangorestframework-simplejwt`
- Environment variables via `.env`

## Features
- User registration and JWT login
- Authenticated patient CRUD
- Authenticated doctor CRUD
- Patient-doctor assignment and removal
- Validation and useful API errors
- PostgreSQL configuration through environment variables

## 1. Create a PostgreSQL database

Create a database named `healthcare_db` in PostgreSQL.

Example using psql:

```sql
CREATE DATABASE healthcare_db;
```

## 2. Setup Python environment

Windows:

```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## 3. Environment variables

Copy `.env.example` to `.env` and set your PostgreSQL password and a strong Django secret key.

```text
SECRET_KEY=your-long-secret
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
DB_NAME=healthcare_db
DB_USER=postgres
DB_PASSWORD=your_postgres_password
DB_HOST=127.0.0.1
DB_PORT=5432
```

Never commit `.env`.

## 4. Migrate and run

```powershell
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

API base URL:
`http://127.0.0.1:8000/`

## Authentication

Register:
`POST /api/auth/register/`

```json
{
  "name": "Rohit Gupta",
  "email": "rohit@example.com",
  "password": "StrongPass123"
}
```

Login:
`POST /api/auth/login/`

```json
{
  "email": "rohit@example.com",
  "password": "StrongPass123"
}
```

Copy the `access` token and send it for protected requests:

```text
Authorization: Bearer <access-token>
```

## API endpoints

### Auth
- POST `/api/auth/register/`
- POST `/api/auth/login/`

### Patients
- POST `/api/patients/`
- GET `/api/patients/`
- GET `/api/patients/<id>/`
- PUT `/api/patients/<id>/`
- DELETE `/api/patients/<id>/`

### Doctors
- POST `/api/doctors/`
- GET `/api/doctors/`
- GET `/api/doctors/<id>/`
- PUT `/api/doctors/<id>/`
- DELETE `/api/doctors/<id>/`

### Patient-doctor mappings
- POST `/api/mappings/`
- GET `/api/mappings/`
- GET `/api/mappings/<patient_id>/` – doctors assigned to that patient
- DELETE `/api/mappings/<mapping_id>/` – removes that mapping

POST mapping body:
```json
{
  "patient": 1,
  "doctor": 1
}
```

> Note: the assignment uses the same URL shape for the patient lookup and mapping delete. Therefore, for GET the number means `patient_id`; for DELETE it means `mapping_id`, matching the supplied assignment specification.

## Postman
Import `postman_collection.json` from this repository. Set the collection variables after login:
- `base_url` = `http://127.0.0.1:8000`
- `access_token` = JWT access token from login
- `patient_id`, `doctor_id`, `mapping_id` as created during testing.

## Security notes
- Passwords are hashed by Django; plain passwords are never stored.
- JWT protects all patient, doctor and mapping endpoints.
- Secrets and database credentials are loaded from `.env`.
- `.env` is ignored by Git.
- Input validation is handled by DRF serializers.
