"""
Redis Cache Helper Functions

This module provides utility functions for managing cached data,
specifically for task statistics caching and invalidation.
"""

from django.core.cache import cache
from django.conf import settings


def get_task_stats_cache_key():
    """
    Returns the cache key used for storing task statistics.
    
    Returns:
        str: The cache key for task stats
    """
    return getattr(settings, 'TASK_STATS_CACHE_KEY', 'task_stats')


def get_task_stats_from_cache():
    """
    Retrieves task statistics from Redis cache.
    
    Returns:
        dict or None: Cached statistics if available, None otherwise
    """
    cache_key = get_task_stats_cache_key()
    return cache.get(cache_key)


def set_task_stats_to_cache(stats_data):
    """
    Stores task statistics in Redis cache with configured timeout.
    
    Args:
        stats_data (dict): Dictionary containing task counts by status
                          Example: {'todo': 5, 'doing': 3, 'done': 10}
    
    Returns:
        bool: True if cache was set successfully
    """
    cache_key = get_task_stats_cache_key()
    timeout = getattr(settings, 'TASK_STATS_CACHE_TIMEOUT', 30)
    cache.set(cache_key, stats_data, timeout)
    return True


def invalidate_task_stats_cache():
    """
    Deletes task statistics from Redis cache.
    
    This should be called whenever tasks are created, updated, or deleted
    to ensure the cached statistics remain accurate.
    
    Returns:
        bool: True if cache was deleted successfully
    """
    cache_key = get_task_stats_cache_key()
    cache.delete(cache_key)
    return True


def clear_all_cache():
    """
    Clears all cached data (use with caution).
    
    Returns:
        bool: True if cache was cleared successfully
    """
    cache.clear()
    return True