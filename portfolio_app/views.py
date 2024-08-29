from django.shortcuts import render
from .models import Project  # Import the Project model

def home(request):
    projects = Project.objects.all()  # Query all projects from the database
    return render(request, 'portfolio_app/index.html', {'projects': projects})

def about(request):
    return render(request, 'portfolio_app/about.html')

def contact(request):
    return render(request, 'portfolio_app/contact.html')

