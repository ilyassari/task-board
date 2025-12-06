"""
Tasks App Configuration

Configures the tasks application and registers signal handlers.
"""

from django.apps import AppConfig


class TasksConfig(AppConfig):
    """
    Configuration class for tasks application.
    
    Attributes:
        default_auto_field: Specifies the type of auto-created primary keys
        name: The full Python path to the application
    """
    
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tasks'
    verbose_name = 'Task Management'
    
    def ready(self):
        """
        Import signal handlers when the app is ready.
        
        This method is called when Django starts and ensures that
        signal handlers are registered properly.
        """
        import tasks.signals  # noqa: F401