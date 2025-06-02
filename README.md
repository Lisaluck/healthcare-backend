

create a readme for my django project which contain healthcare backend to be run on postman api
Healthcare Backend System (Django REST Framework)
A Django-based backend for a healthcare application that manages patients, doctors, and their mappings using JWT authentication. Built with Django REST Framework (DRF) and PostgreSQL.

🚀 Features
✅ JWT Authentication (Register, Login)
✅ Patient Management (CRUD Operations)
✅ Doctor Management (CRUD Operations)
✅ Patient-Doctor Mapping (Assign/Remove Doctors)
✅ PostgreSQL Database
✅ Protected API Endpoints

⚙️ Setup & Installation
1. Clone the Repository
2. git clone https://github.com/Lisaluck/healthcare-backend.git
cd healthcare-backend
3. Create & Activate Virtual Environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows
4. Install Dependencies
pip install -r requirements.txt
5. Configure PostgreSQL
Install PostgreSQL and create a database.

Update settings.py with your DB credentials:

python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'healthcare_db',
        'USER': 'your_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
5. Apply Migrations
python manage.py migrate
6. Create Superuser (Admin Access)
python manage.py createsuperuser
7. Run the Server
python manage.py runserver
➡️ API will run at: http://127.0.0.1:8000/

🔑 API Endpoints (Postman Collection)
🔐 Authentication
Method	Endpoint	Description
POST	/api/auth/register/	Register a new user
POST	/api/auth/login/	Log in & get JWT token
👨‍⚕️ Doctor Management
Method	Endpoint	Description
POST	/api/doctors/	Add a new doctor
GET	/api/doctors/	List all doctors
GET	/api/doctors/<id>/	Get doctor details
PUT	/api/doctors/<id>/	Update doctor
DELETE	/api/doctors/<id>/	Delete doctor
👨‍⚕️ Patient Management
Method	Endpoint	Description
POST	/api/patients/	Add a new patient
GET	/api/patients/	List all patients
GET	/api/patients/<id>/	Get patient details
PUT	/api/patients/<id>/	Update patient
DELETE	/api/patients/<id>/	Delete patient
📌 Patient-Doctor Mapping
Method	Endpoint	Description
POST	/api/mappings/	Assign doctor to patient
GET	/api/mappings/	List all mappings
GET	/api/mappings/<patient_id>/	Get doctors for a patient
DELETE	/api/mappings/<id>/	Remove mapping
🔧 Environment Variables
Create a .env file:

env
SECRET_KEY=your_django_secret_key
DB_NAME=healthcare_db
DB_USER=postgres_user
DB_PASSWORD=postgres_password
DB_HOST=localhost
DB_PORT=5432
📦 Dependencies
Django

Django REST Framework

djangorestframework-simplejwt (JWT Auth)

psycopg2 (PostgreSQL)

python-dotenv (Environment Variables)


📞 Contact
📧 Email: leelimahajan@gmail.com
🔗 GitHub: Lisaluck

Happy Coding! 🚀
Test all endpoints in Postman and ensure JWT tokens are included in Authorization Header (Bearer <token>).
