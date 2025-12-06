"""
Tasks App URL Configuration

Defines URL patterns for task-related API endpoints.
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tasks.views import TaskViewSet, StatsView

# Create router and register viewsets
router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

app_name = 'tasks'

urlpatterns = [
    # Stats endpoint (before router to avoid conflicts)
    path('stats/', StatsView.as_view(), name='stats'),
    
    # Task CRUD endpoints via router
    path('', include(router.urls)),
]