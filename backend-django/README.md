# Backend with Django
### **Importance of Backend**
With React, HTML, and CSS, you can create visually appealing user interfaces. But how do you implement user databases, handle server-side logic, and ensure data security? This is where backend development comes into play. Backend development focuses on managing the behind-the-scenes functionality of applications, that includes but is not limited to form submissions, user login databases, and much more.

### **What is Django?**
Django is a python-based backend framework that is used in many applications, including Instagram, Spotify, and Youtube. Django is a great framework because of its scalability, ease-of-use, and versatility. In this repository, you'll find resources on how to setup django applications, connect django backend to frontend applications, and templates for building web apps with django. Let's get started!

### **Setting up a django app**
##### Dependencies
Make sure you have python and pip installed on your machine. If not, go to https://www.python.org/downloads/ to install python. The first step to creating any python application is creating a virtual environment. To do this, you first have to install the venv module. Open a command line and run this command:

MacOS/Linux:
```bash
sudo apt-get install python3-venv
```

Windows:
```bash
pip install virtualenv
```

Next, open a new project, and in the command line, create a new virtual environment with these commands.

All Operating Systems:
```bash
python3 -m venv [name]
```

Be sure to replace [name] with the name of your environment. Activate the virtual environment.

MacOS/Linux:
```bash
source [name]/bin/activate
```

Windows:
```bash
[name]/Scripts/activate
```

##### Installing Django and creating a Django project
In your activated virtual environment, install django by running 

```bash
pip install django
```

Then, create a new django app by running 

```bash
django-admin startproject [name]
```

Be sure to replace [name] with the name of your project. Your directory should now look like this:

```bash
mysite/
├── manage.py
└── mysite/
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py

```

Now you're ready to code! Visit other parts of this folder to learn more about building django apps. 