from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'user', 'status', 'created_at']
    list_filter = ['status', 'created_at', 'user']
    search_fields = ['title', 'description', 'user__username']
    list_editable = ['status']
    fieldsets = (
        ('Основная информация', {
            'fields': ('user', 'title', 'description')
        }),
        ('Статус и даты', {
            'fields': ('status', ('created_at', 'updated_at'))
        }),
    )
    readonly_fields = ['created_at', 'updated_at']