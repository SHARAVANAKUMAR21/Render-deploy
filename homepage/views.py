from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def hello_user(request):
    return render(request, 'homepage/hello_user.html')
