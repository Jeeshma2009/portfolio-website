from django.shortcuts import render
from .models import Project, Profile
from django.http import FileResponse, Http404
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from decouple import config

def index(request):
    profile = Profile.objects.first()
    projects = Project.objects.all()
    print("---------------",profile)
    return render(request, 'portfolio/index.html', {
        'profile': profile,
        'projects': projects
    })

def home(request):
    profile = Profile.objects.first()
    projects = Project.objects.all()
    return render(request, 'portfolio/index.html', {
        'profile': profile,
        'projects': projects
    })

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/project_list.html', {'projects': projects})


def view_resume(request):
    profile = Profile.objects.first()
    if profile and profile.resume:
        return FileResponse(profile.resume.open('rb'), content_type='application/pdf')
    raise Http404("Resume not found")

def skills_certificates(request):
    profile = Profile.objects.first()
    return render(request, 'portfolio/skills.html', {'profile': profile})

def create_admin_user(request):
    User = get_user_model()
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', config('EMAIL'), config('PASSWORD'))
        return HttpResponse("Superuser created successfully.")
    else:
        return HttpResponse("Superuser already exists.")