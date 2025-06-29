from django.urls import path
from .api_views import ProfileAPIView, SkillAPIView, ProjectAPIView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.project_list, name='project_list'),
    path('api/profile/', ProfileAPIView.as_view()),
    path('api/skills/', SkillAPIView.as_view()),
    path('api/projects/', ProjectAPIView.as_view()),
    path('resume/', views.view_resume, name='resume'),
    path('skills/', views.skills_certificates, name='skills'),
]