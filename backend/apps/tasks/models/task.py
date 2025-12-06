"""
Task Model

Represents a task in the task management system.
Each task has a title, status (todo/doing/done), and creation timestamp.
"""

from django.db import models


class Task(models.Model):
    """
    Task model for managing work items.
    
    Attributes:
        title: The task description or name
        status: Current status of the task (todo, doing, done)
        created_at: Timestamp when the task was created
    """
    
    class Status(models.TextChoices):
        """Available status choices for tasks"""
        TODO = 'todo', 'To Do'
        DOING = 'doing', 'Doing'
        DONE = 'done', 'Done'
    
    title = models.CharField(
        max_length=150,
        help_text="Task title or description"
    )
    
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.TODO,
        help_text="Current status of the task"
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Timestamp when the task was created"
    )
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
    
    def __str__(self):
        return f"{self.title} ({self.get_status_display()})"