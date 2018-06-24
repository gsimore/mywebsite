from django.contrib import admin
from .models import Person, Experience, Resume, ExperienceType, Location

admin.site.register(Person)
admin.site.register(Experience)
admin.site.register(Resume)
admin.site.register(ExperienceType)
admin.site.register(Location)