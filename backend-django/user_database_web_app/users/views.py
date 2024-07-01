from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

# Home Page View
def index(request):
    return render(request, 'users/index.html')

# Base User Registration View
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        # Check if a user with the submitted username already exists
        if User.objects.filter(username=username).exists():
            # If the user exists, you can return an error message
            return render(request, 'users/register.html', {'error': 'Username already exists'})
        
        # check if passwords match
        if password == password2:
            User.objects.create_user(username=username, password=password)
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Redirect to the URL name 'index'
    return render(request, 'users/register.html')

# Base User Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')  # Redirect to the URL name 'index'
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})
