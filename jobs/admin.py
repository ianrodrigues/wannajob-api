from django.contrib import admin

from .models import Job


class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'seniority_level', 'salary', 'city', 'country')

admin.site.register(Job, JobAdmin)
