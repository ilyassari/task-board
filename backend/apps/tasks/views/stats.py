"""
Stats Views

Provides aggregated task statistics with Redis caching.
Cache is automatically invalidated when tasks change.
"""

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count
from tasks.models import Task
from core.cache import (
    get_task_stats_from_cache,
    set_task_stats_to_cache
)


class StatsView(APIView):
    """
    API View for task statistics with Redis caching.
    
    Endpoint:
        GET /api/stats/ - Returns task counts by status
    
    Response format:
        {
            "todo": 7,
            "doing": 3,
            "done": 12
        }
    
    Caching behavior:
        - First request: Queries database and caches result for 30 seconds
        - Subsequent requests: Returns cached data (no database query)
        - Cache invalidation: Automatic on task create/update/delete
    """
    
    def get(self, request):
        """
        Retrieve task statistics with caching.
        
        Returns:
            Response: Dictionary with task counts by status
        """
        # Try to get from cache first
        cached_stats = get_task_stats_from_cache()
        
        if cached_stats is not None:
            # Cache hit - return cached data
            return Response(cached_stats, status=status.HTTP_200_OK)
        
        # Cache miss - query database
        stats = self._compute_stats()
        
        # Store in cache for next requests
        set_task_stats_to_cache(stats)
        
        return Response(stats, status=status.HTTP_200_OK)
    
    def _compute_stats(self):
        """
        Compute task statistics from database.
        
        Returns:
            dict: Task counts grouped by status
        """
        # Query task counts grouped by status
        stats_queryset = Task.objects.values('status').annotate(
            count=Count('id')
        )
        
        # Initialize with zero counts for all statuses
        stats = {
            'todo': 0,
            'doing': 0,
            'done': 0
        }
        
        # Update with actual counts from database
        for item in stats_queryset:
            stats[item['status']] = item['count']
        
        return stats