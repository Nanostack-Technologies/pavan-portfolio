from django.contrib import admin
from .models import Project, Skill, Service, ContactMessage

admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Service)
admin.site.register(ContactMessage)
