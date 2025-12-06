# 🧩 Study Case: **Task Board — Task Management & Metrics System**
*(Django REST + Redis Cache + Vue 3 + Docker Compose)*

## 🎯 Scenario
A software team needs a lightweight task management system to track their work items.  
Users should be able to create tasks, update them, delete them, and track task statuses in real time.

Your goal is to build a **Task Management API** and a **Stats Dashboard** that shows aggregated task metrics.  
The dashboard will not require WebSockets — instead, it will fetch updated data periodically. Redis will be used to improve performance by caching aggregated statistics.

---

# 🧱 Requirements

## 1) Backend — Django REST Framework

### 📌 Model: `Task`
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

### 📌 API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/tasks/` | List all tasks |
| POST | `/api/tasks/` | Create a new task |
| PATCH | `/api/tasks/<id>/` | Update a task status |
| DELETE | `/api/tasks/<id>/` | Delete a task |
| GET | `/api/stats/` | Return task statistics |

Example stats output:
```json
{
  "todo": 7,
  "doing": 3,
  "done": 12
}
```

### 📌 Redis Cache Usage

#### Stats Endpoint Behavior:
- Computes aggregated task counts.
- Stores results in Redis for **30 seconds** under the key `task_stats`.
- If cached data exists, returns it without querying the DB.

#### Cache Invalidation:
Redis key `task_stats` must be deleted when:
- A task is created  
- A task is updated  
- A task is deleted  

---

## 2) Frontend — Vue 3 + Vite

### 📄 Pages

#### **`/tasks`**
- Display list of tasks
- Create new tasks
- Update task status
- Delete tasks

#### **`/dashboard`**
- Shows counts for “todo”, “doing”, and “done”
- Fetches `/api/stats/` every **5 seconds**
- Displays data using cards or a simple chart

---

## 3) Docker Compose

### Required Services
- `backend` → Django REST API  
- `frontend` → Vue (Vite Dev Server)  
- `redis` → Redis cache instance  
- `db` → PostgreSQL  

### Command to Run
```
docker-compose up --build
```

### Expected URLs
- Backend → http://localhost:8000  
- Frontend → http://localhost:5173  
- Task Dashboard → http://localhost:5173/dashboard  
- Redis → localhost:6379  

---

## 4) Delivery Expectations

### Backend
- Clean DRF views/serializers
- Clear Redis usage
- Proper cache invalidation on task changes

### Frontend
- Uses Vue 3 Composition API
- Axios for API communication
- Dashboard refreshes stats every 5 seconds

### Docker
- All services run together
- `.env` files supported

---

# 🧠 Optional Extra Challenges
- Use Chart.js or Recharts for visualization  
- Add Celery periodic tasks  
- Add NGINX reverse proxy for production builds  
- Use Pinia for frontend state management  

---

## ✔️ Summary
**Task Board** is a study case combining Django REST API, Redis caching, a Vue frontend, and Docker-based deployment.  
The project is designed to test modern web application fundamentals and practical caching strategies.

