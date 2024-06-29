from django.shortcuts import render

# Create your views here.
def index(request):
    '''
    add your html file as a view here
    '''
    return render(request, 'myapp/index.html')