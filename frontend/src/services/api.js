import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Task operations
export const getTasks = () => api.get('/api/tasks/');
export const createTask = (data) => api.post('/api/tasks/', data);
export const updateTask = (id, data) => api.patch(`/api/tasks/${id}/`, data);
export const deleteTask = (id) => api.delete(`/api/tasks/${id}/`);

// Stats operations
export const getStats = () => api.get('/api/stats/');

export default api;