# API-Developement using Dgango Rest Framework & Django JWT Auth 
This is a project that demonstrates how you could implement json web token authentication 

In order to test out this project, follow these steps:

clone the repository

in the employee folder, run: python3 -m venv venv
then activate the virtual environment: source venv/bin/activate (MacOS) or venv\Scripts\activate (Windows)
in the employee folder, run: pip install -r requirements.txt
in the employee folder, run: python manage.py migrate
in the employee folder, run: python manage.py runserver
Then under employee/auth_system/settings.py:

under DATABASES, set the PASSWORD field to your database password
