"""
Tasks App Admin Configuration

Registers Task model in Django admin with custom display options.
"""

from django.contrib import admin
from tasks.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """
    Admin interface for Task model.
    
    Features:
        - List view shows title, status, and creation date
        - Filtering by status and creation date
        - Search by title
        - Read-only created_at field
    """
    
    list_display = ['id', 'title', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['title']
    readonly_fields = ['created_at']
    ordering = ['-created_at']
    
    fieldsets = (
        ('Task Information', {
            'fields': ('title', 'status')
        }),
        ('Metadata', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )