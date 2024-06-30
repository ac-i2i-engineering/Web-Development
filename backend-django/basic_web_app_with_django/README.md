# Basic Web App with Django

### Django Project Structure
After you run, 
```bash
django-admin startproject myproject
```
you will see the project folder. In this repo, it would be the 'basic_web_app_with_django' folder. The files here manage settings and configurations for the entire project. But to do anything with django, you have to create an app. An app controls individual components in the project that serve specific functionalities. Most projects will only have one app, but larger apps like Instagram or Spotify will have several. To create an app, run 

```bash
python manage.py startapp myapp
```

Be sure to replace 'myapp' with a proper name. You should see a 'myapp' folder with a file structure that looks like this. 
```bash
myapp/
│
├── migrations/
│   ├── __init__.py
│   └── ...
│
├── __init__.py
├── admin.py
├── apps.py
├── models.py
├── tests.py
├── urls.py
└── views.py

```

### Connecting apps to the project
These two steps are very important, so do not skip them. Files across this repo are well commented to show exactly what to do.

1. In [settings.py](basic_web_app_with_django/settings.py) in the project folder, add your app to the INSTALLED_APPS list.
2. In the project level [urls.py](basic_web_app_with_django/urls.py), add your app urls.py to the project urls.py.r

### Wrapping Django with HTML/CSS
In your app directory, make a templates directory with a 'myapp' subdirectory. Be sure to replace 'myapp' with the name of your app. In this repo, there is an example html file [index.html](myapp/templates/myapp/index.html). To connect the html file the project, first, go to [views.py](myapp/views.py) and register the html form as a view. Then, go to the app level [urls.py](myapp/urls.py) and add give the view a url. 

### Running the web app
To run the app, in bash, run 

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

The app will run on your local host. Visit the other repositories to learn how to use databases, build sophisticated web apps, and much more!