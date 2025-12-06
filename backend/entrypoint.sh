#!/bin/sh

# Exit immediately if a command exits with a non-zero status
set -e

echo "Waiting for PostgreSQL..."

# Wait for PostgreSQL to be ready
while ! nc -z $SQL_HOST $SQL_PORT; do
  sleep 0.1
done

echo "PostgreSQL started"

echo "Waiting for Redis..."

# Wait for Redis to be ready
while ! nc -z redis 6379; do
  sleep 0.1
done

echo "Redis started"

# Development/Test environment operations (DEBUG=1)
if [ "$DEBUG" = "1" ]; then
    echo "Running in DEBUG mode - Development environment"
    
    # Flush database (clear all data)
    echo "Flushing database..."
    python manage.py flush --no-input
    
    # Create migrations
    echo "Creating migrations..."
    python manage.py makemigrations
    
    # Apply migrations
    echo "Running migrations..."
    python manage.py migrate
    
    # Create cache table for database-based caching (if needed)
    echo "Creating cache table..."
    python manage.py createcachetable
    
    # Create superuser if credentials provided
    if [ "$DJANGO_SUPERUSER_USERNAME" ]; then
        echo "Creating superuser..."
        python manage.py createsuperuser \
            --noinput \
            --username $DJANGO_SUPERUSER_USERNAME \
            --email $DJANGO_SUPERUSER_EMAIL || true
    fi
    
    # Collect static files
    echo "Collecting static files..."
    python manage.py collectstatic --noinput --clear

# Production environment operations (DEBUG=0)
else
    echo "Running in PRODUCTION mode"
    
    # Only run migrations (no flush, no makemigrations)
    echo "Running migrations..."
    python manage.py migrate --noinput
    
    # Collect static files
    echo "Collecting static files..."
    python manage.py collectstatic --noinput --clear
fi

echo "Starting server..."

# Start Django development server
exec "$@"