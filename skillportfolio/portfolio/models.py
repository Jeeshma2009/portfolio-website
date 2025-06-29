from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField()
    photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)  # e.g., Backend, Frontend

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=255)
    domain = models.CharField(max_length=255)
    tech_stack = models.TextField()
    description = models.TextField()
    key_contributions = models.TextField()
    role = models.CharField(max_length=100)
    team_size = models.PositiveIntegerField()


    def __str__(self):
        return self.title
