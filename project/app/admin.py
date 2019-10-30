from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'expiry_date', 'expiry_alarm')
    search_fields = ('id', 'title')


admin.site.register(Task, TaskAdmin)
