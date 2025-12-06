# Task Board - Task Management System

A lightweight task management system built with Django REST Framework, Vue 3, Redis cache, and PostgreSQL.

## 🚀 Features

- Task CRUD operations (Create, Read, Update, Delete)
- Real-time task statistics dashboard
- Redis caching for improved performance
- RESTful API architecture
- Responsive Vue 3 frontend

## 🛠️ Tech Stack

**Backend:**
- Django REST Framework
- PostgreSQL
- Redis

**Frontend:**
- Vue 3
- Vite
- Axios

**DevOps:**
- Docker
- Docker Compose

## 📦 Quick Start
```bash
# Clone the repository
git clone https://github.com/ilyassari/task-board.git
cd task-board

# Start all services
docker-compose --env-file .env.dev up --build
```

**Access the application:**
- Frontend: http://localhost:5173
- Backend API: http://localhost:8000
- Admin Panel: http://localhost:8000/admin

## 📚 Documentation

- [Backend Documentation](./backend/README.md)
- [Frontend Documentation](./frontend/README.md)
- [Study Case](./study_case.md)

## 📝 License

This project is a study case for learning modern web development practices.