This is a practice project developed for college purposes using Django and SQLite.
The application provides a simple web-based system where passengers can register, log in, submit railway-related complaints using details like PNR number, urgency level, and service ratings, and track the status of their complaints.

Railway employees (admin users) can securely log in to a separate dashboard to view all complaints and update their status (Pending, Reviewing, Action Taken, Resolved).
The project focuses on understanding Django fundamentals, user authentication, role-based access, and basic UI design without using advanced frameworks.


Commands to use:(Use Py terminal)

Create venv --> python -m venv venv

Activate venv --> venv\Scripts\activate

downloading required modules --> pip install -r requirements.txt

Read migrating files --> python manage.py makemigrations

Create migration(DB creation) --> python manage.py migrate

Superuser(Admin creation) --> python manage.py createsuperuser

Login to server --> python manage.py runserver (copy the url  http://127.0.0.1:8000/login/) 

Registering new user: http://127.0.0.1:8000/register
