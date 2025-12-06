# Task Board - Backend API

Django REST Framework based backend for Task Board application.

## 🏗️ Architecture
```bash
backend/
├── apps/
│   ├── core/          # Core utilities and helpers
│   └── tasks/         # Task management app
├── config/            # Django settings and configuration
├── staticfiles/       # Static files (collected)
├── Dockerfile
├── entrypoint.sh
├── manage.py
└── requirements.txt
```

## 🔧 Tech Stack

- **Framework:** Django 5.2 + Django REST Framework
- **Database:** PostgreSQL
- **Cache:** Redis
- **CORS:** django-cors-headers

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/tasks/` | List all tasks |
| POST | `/api/tasks/` | Create a new task |
| PATCH | `/api/tasks/<id>/` | Update a task status |
| DELETE | `/api/tasks/<id>/` | Delete a task |
| GET | `/api/stats/` | Get task statistics (cached) |

## 🗄️ Models

### Task Model
```python
class Task(models.Model):
    title = models.CharField(max_length=150)
    status = models.CharField(max_length=20, choices=[
        ('todo', 'To Do'),
        ('doing', 'Doing'),
        ('done', 'Done')
    ])
    created_at = models.DateTimeField(auto_now_add=True)
```

## 💾 Redis Cache Strategy

- **Stats endpoint** results are cached for 30 seconds
- Cache key: `task_stats`
- **Auto-invalidation** on task create/update/delete
- Improves performance by reducing database queries

## 🚀 Local Development

### Prerequisites
- Python 3.11+
- PostgreSQL
- Redis

### Setup
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

## 🐳 Docker Development
```bash
# From project root
docker-compose --env-file .env.dev up backend
```

## 🧪 Running Tests
```bash
python manage.py test
```

## 🔐 Environment Variables

See `.env.example` in project root for required variables.

Key variables:
- `DEBUG`
- `SECRET_KEY`
- `SQL_DATABASE`, `SQL_USER`, `SQL_PASSWORD`
- `REDIS_URL`

## 📝 Admin Panel

Access Django admin at: `http://localhost:8000/admin`

Default credentials (development):
- Username: `admin`
- Password: `admin123`