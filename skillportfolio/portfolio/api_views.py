from rest_framework import generics
from .models import Profile, Skill, Project
from .serializers import ProfileSerializer, SkillSerializer, ProjectSerializer

class ProfileAPIView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class SkillAPIView(generics.ListAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class ProjectAPIView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer