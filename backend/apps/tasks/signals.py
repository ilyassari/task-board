"""
Tasks App Signals

Handles automatic cache invalidation when Task instances are modified.

Note: Cache invalidation is already handled in the ViewSet methods.
These signals provide a backup mechanism and ensure cache invalidation
even when tasks are modified outside the API (e.g., Django admin, shell).
"""

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from tasks.models import Task
from core.cache import invalidate_task_stats_cache


@receiver(post_save, sender=Task)
def task_saved_handler(sender, instance, created, **kwargs):
    """
    Invalidate task stats cache when a task is created or updated.
    
    Args:
        sender: The model class (Task)
        instance: The actual task instance being saved
        created: Boolean indicating if this is a new task
        **kwargs: Additional keyword arguments
    """
    invalidate_task_stats_cache()


@receiver(post_delete, sender=Task)
def task_deleted_handler(sender, instance, **kwargs):
    """
    Invalidate task stats cache when a task is deleted.
    
    Args:
        sender: The model class (Task)
        instance: The task instance being deleted
        **kwargs: Additional keyword arguments
    """
    invalidate_task_stats_cache()