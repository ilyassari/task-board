"""
Task Serializers

Handles serialization and deserialization of Task model instances
for API requests and responses.
"""

from rest_framework import serializers
from tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for Task model.
    
    Handles conversion between Task model instances and JSON format.
    Validates task data on creation and updates.
    """
    
    status_display = serializers.CharField(
        source='get_status_display',
        read_only=True
    )
    
    class Meta:
        model = Task
        fields = ['id', 'title', 'status', 'status_display', 'created_at']
        read_only_fields = ['id', 'created_at', 'status_display']
    
    def validate_title(self, value):
        """
        Validate that title is not empty or only whitespace.
        """
        if not value or not value.strip():
            raise serializers.ValidationError("Title cannot be empty.")
        return value.strip()
    
    def validate_status(self, value):
        """
        Validate that status is one of the allowed choices.
        """
        valid_statuses = [choice[0] for choice in Task.Status.choices]
        if value not in valid_statuses:
            raise serializers.ValidationError(
                f"Status must be one of: {', '.join(valid_statuses)}"
            )
        return value