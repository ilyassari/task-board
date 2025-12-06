# Use official Python base image
FROM python:3.11-alpine

# Set working directory
WORKDIR /usr/src/app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies for PostgreSQL and Python packages
RUN apk update && apk add --no-cache \
    gcc \
    g++ \
    libc-dev \
    musl-dev \
    python3-dev \
    libffi-dev \
    postgresql-dev \
    curl

# Copy requirements and install Python dependencies
COPY ./requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy project files
COPY . .

# Make entrypoint script executable
RUN chmod +x /usr/src/app/entrypoint.sh

# Set entrypoint
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]