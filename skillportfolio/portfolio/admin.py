from django.contrib import admin
from .models import Profile, Skill, Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'domain', 'role', 'team_size']
    search_fields = ['title', 'tech_stack', 'description']

admin.site.register(Profile)
admin.site.register(Skill)
# admin.site.register(Project)