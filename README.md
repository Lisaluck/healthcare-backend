1. Prepare Your Project for GitHub
Ensure your project has a .gitignore file to exclude unnecessary files (e.g., __pycache__, IDE files, virtual environments).

If you don’t have a .gitignore, create one in your project root and add:

__pycache__/
.idea/
venv/
*.pyc
*.env
*.log
2. Initialize Git in PyCharm
Open your project in PyCharm.

Go to VCS → Enable Version Control Integration.

Select Git and click OK.

3. Commit Your Project Locally
Go to Git → Commit (or press Ctrl+K / Cmd+K on macOS).

Select the files you want to commit.

Enter a commit message (e.g., "Initial commit").

Click Commit.

4. Create a GitHub Repository
Go to GitHub and log in.

Click New repository.

Enter a Repository name (match your project name if possible).

Choose Public/Private.

Do not initialize with a README (since your project already exists).

Click Create repository.

5. Link PyCharm to GitHub
Option 1: Using PyCharm’s Built-in GitHub Integration
Go to File → Settings → Version Control → GitHub.

Click Add Account and log in with GitHub (or use a GitHub Token).

After linking, go to Git → Push.

PyCharm will prompt you to add a remote. Click Define remote.

Enter the GitHub repository URL (e.g., https://github.com/yourusername/yourrepo.git).

Click Push.

Option 2: Manually Add Remote and Push
Open the terminal in PyCharm (Alt+F12).

Run:

bash
git remote add origin https://github.com/yourusername/yourrepo.git
git branch -M main
git push -u origin main
(Replace yourusername/yourrepo with your actual GitHub repo URL.)

6. Verify on GitHub
Refresh your GitHub repository page—your files should now appear there.

Troubleshooting
Authentication Error? Use an SSH key or GitHub Token instead of password.

Permission Denied? Ensure the repository URL is correct and you have write access.

That’s it! Your PyCharm project is now on GitHub. 🚀

Would you like help with anything else? 😊

PS C:\Users\leeli\healthcare> git remote add origin https://github.com/Lisaluck/healthcare-backend
fatal: not a git repository (or any of the parent directories): .git
This error occurs because you haven't initialized a Git repository in your project folder. Let's fix this step by step.

Solution: Initialize Git and Push to GitHub
1. Open Terminal in Project Directory
Make sure you're in the correct folder (healthcare in your case):

powershell
cd C:\Users\leeli\healthcare
2. Initialize Git
Run:

powershell
git init
This creates a .git folder (hidden) in your project.

3. Check Files Status
powershell
git status
You should see your project files listed as "untracked."

4. Add Files to Staging
powershell
git add .
(or git add * to add all files)

5. Commit Changes
powershell
git commit -m "Initial commit"
6. Link to GitHub Repository
Now run the git remote command again:

powershell
git remote add origin https://github.com/Lisaluck/healthcare-backend.git
7. Push to GitHub
powershell
git push -u origin main
(If you get an error, try git push -u origin master for older repos.)

Still Having Issues? Try These Fixes:
Check GitHub URL:
Ensure the URL is correct:

powershell
git remote -v
If wrong, remove and re-add:

powershell
git remote remove origin
git remote add origin https://github.com/Lisaluck/healthcare-backend.git
Branch Name Conflict:
If GitHub uses main but your local uses master:

powershell
git branch -M main  # Renames your branch to "main"
git push -u origin main
Authentication Error:

Use a GitHub Personal Access Token (instead of password).

Or set up SSH keys (GitHub Guide).

Final Check
Refresh your GitHub repo—your files should appear!

If not, share the error message, and I’ll help debug. 🛠️

Let me know if you need further clarification! 😊

Django Assignment.pdf
PDF 79.49KB
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
bash
git clone https://github.com/Lisaluck/healthcare-backend.git
cd healthcare-backend
2. Create & Activate Virtual Environment
bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows
3. Install Dependencies
bash
pip install -r requirements.txt
4. Configure PostgreSQL
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
bash
python manage.py migrate
6. Create Superuser (Admin Access)
bash
python manage.py createsuperuser
7. Run the Server
bash
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
