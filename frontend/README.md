# Task Board - Frontend

Vue 3 + Vite based frontend application for Task Board.

## 🏗️ Project Structure
```bash
frontend/
├── public/            # Static assets
├── src/
│   ├── assets/        # Images, fonts, etc.
│   ├── components/    # Reusable Vue components
│   ├── router/        # Vue Router configuration
│   ├── services/      # API service layer
│   ├── views/         # Page components
│   ├── App.vue        # Root component
│   ├── main.js        # Application entry point
│   └── style.css      # Global styles
├── Dockerfile
├── index.html
├── package.json
└── vite.config.js
```

## 🔧 Tech Stack

- **Framework:** Vue 3 (Composition API)
- **Build Tool:** Vite
- **HTTP Client:** Axios
- **Routing:** Vue Router
- **Node Version:** 20.x

## 📱 Features

### Task List (`/tasks`)
- Display all tasks
- Create new tasks
- Update task status (todo → doing → done)
- Delete tasks
- Auto-refresh every 5 seconds

### Dashboard (`/dashboard`)
- Real-time statistics display
- Task counts by status
- Auto-refresh every 5 seconds

## 🚀 Local Development

### Prerequisites
- Node.js 20.x+
- npm

### Setup
```bash
# Install dependencies
npm install

# Start development server
npm run dev
```

Application will be available at: `http://localhost:5173`

## 🐳 Docker Development
```bash
# From project root
docker-compose --env-file .env.dev up frontend
```

## 🏗️ Build for Production
```bash
# Create production build
npm run build

# Preview production build
npm run preview
```

## 🔌 API Integration

Backend API base URL is configured via environment variable:
```bash
VITE_API_BASE_URL=http://localhost:8000
```

API service handles all HTTP requests through Axios with automatic error handling.

## 📦 Key Dependencies

- `vue`: ^3.5.13
- `vue-router`: ^4.4.5
- `axios`: ^1.7.9
- `vite`: ^6.0.1

## 🎨 UI Components

- **TaskList.vue**: Main task management interface
- **Dashboard.vue**: Statistics and metrics view
- **Navigation**: Router-based navigation between views

## 🔄 Auto-Refresh Strategy

Both views implement polling mechanism:
- Silent background updates (no loading spinner)
- Preserves user interaction state
- Configurable refresh intervals