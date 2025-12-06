"""
Task Views

Handles CRUD operations for Task model through REST API endpoints.
Automatically invalidates cache when tasks are modified.
"""

from rest_framework import viewsets
from rest_framework.response import Response
from tasks.models import Task
from tasks.serializers import TaskSerializer
from core.cache import invalidate_task_stats_cache


class TaskViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Task model providing CRUD operations.
    
    Endpoints:
        GET    /api/tasks/          - List all tasks
        POST   /api/tasks/          - Create a new task
        GET    /api/tasks/<id>/     - Retrieve a specific task
        PUT    /api/tasks/<id>/     - Update a task (full)
        PATCH  /api/tasks/<id>/     - Update a task (partial)
        DELETE /api/tasks/<id>/     - Delete a task
    
    Cache invalidation occurs automatically on create, update, and delete.
    """
    
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
    def create(self, request, *args, **kwargs):
        """Create a new task and invalidate stats cache."""
        response = super().create(request, *args, **kwargs)
        invalidate_task_stats_cache()
        return response
    
    def update(self, request, *args, **kwargs):
        """Update an existing task and invalidate stats cache."""
        response = super().update(request, *args, **kwargs)
        invalidate_task_stats_cache()
        return response
    
    def partial_update(self, request, *args, **kwargs):
        """Partially update a task (PATCH) and invalidate stats cache."""
        response = super().partial_update(request, *args, **kwargs)
        invalidate_task_stats_cache()
        return response
    
    def destroy(self, request, *args, **kwargs):
        """Delete a task and invalidate stats cache."""
        response = super().destroy(request, *args, **kwargs)
        invalidate_task_stats_cache()
        return response