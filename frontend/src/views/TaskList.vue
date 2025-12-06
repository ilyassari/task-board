<script setup>
    import { ref, onMounted, onUnmounted } from 'vue' 
    import { getTasks, createTask, updateTask, deleteTask } from '../services/api'
    
    const tasks = ref([])
    const newTaskTitle = ref('')
    const loading = ref(false)
    const error = ref(null)
    let intervalId = null  

    const fetchTasks = async (silent = false) => {
      if (!silent) {
        loading.value = true
      }
      
      error.value = null
      try {
        const response = await getTasks()
        tasks.value = response.data
      } catch (err) {
        error.value = 'Failed to fetch tasks'
        console.error(err)
      } finally {
        if (!silent) {
          loading.value = false
        }
      }
    }
    
    const addTask = async () => {
      if (!newTaskTitle.value.trim()) return
      
      try {
        await createTask({ title: newTaskTitle.value, status: 'todo' })
        newTaskTitle.value = ''
        await fetchTasks()
      } catch (err) {
        error.value = 'Failed to create task'
        console.error(err)
      }
    }
    
    const changeStatus = async (task) => {
      const statuses = ['todo', 'doing', 'done']
      const currentIndex = statuses.indexOf(task.status)
      const nextStatus = statuses[(currentIndex + 1) % statuses.length]
      
      const oldStatus = task.status
      task.status = nextStatus
      
      try {
        await updateTask(task.id, { status: nextStatus })
        task.status_display = nextStatus.charAt(0).toUpperCase() + nextStatus.slice(1)
      } catch (err) {
        task.status = oldStatus
        error.value = 'Failed to update task'
        console.error(err)
      }
    }
    
    const removeTask = async (id) => {
      if (!confirm('Are you sure you want to delete this task?')) return
      
      try {
        await deleteTask(id)
        await fetchTasks()
      } catch (err) {
        error.value = 'Failed to delete task'
        console.error(err)
      }
    }
    
    const getStatusClass = (status) => {
      return `status-${status}`
    }
    
    onMounted(() => {
      fetchTasks()
      intervalId = setInterval(() => fetchTasks(true), 5000)
    })

    onUnmounted(() => {  // ← EKLE
      if (intervalId) {
        clearInterval(intervalId)
      }
    })
    </script>
    
    <template>
      <div class="task-list">
        <h2>Task Management</h2>
        
        <!-- Error Message -->
        <div v-if="error" class="error-message">
          {{ error }}
        </div>
        
        <!-- Add Task Form -->
        <div class="add-task-form">
          <input
            v-model="newTaskTitle"
            @keyup.enter="addTask"
            type="text"
            placeholder="Enter new task..."
            class="task-input"
          />
          <button @click="addTask" class="btn btn-primary">Add Task</button>
        </div>
        
        <!-- Loading -->
        <div v-if="loading" class="loading">Loading tasks...</div>
        
        <!-- Tasks List -->
        <div v-else class="tasks">
          <div v-if="tasks.length === 0" class="no-tasks">
            No tasks yet. Create your first task!
          </div>
          
          <div
            v-for="task in tasks"
            :key="task.id"
            class="task-item"
            :class="getStatusClass(task.status)"
          >
            <div class="task-content">
              <h3>{{ task.title }}</h3>
              <span class="task-status">{{ task.status_display }}</span>
            </div>
            
            <div class="task-actions">
              <button @click="changeStatus(task)" class="btn btn-status">
                Change Status
              </button>
              <button @click="removeTask(task.id)" class="btn btn-danger">
                Delete
              </button>
            </div>
          </div>
        </div>
      </div>
    </template>
    
    <style scoped>
    .task-list {
      padding: 2rem 0;
    }
    
    h2 {
      margin-bottom: 2rem;
      color: #2c3e50;
    }
    
    .error-message {
      background-color: #fee;
      color: #c33;
      padding: 1rem;
      border-radius: 4px;
      margin-bottom: 1rem;
    }
    
    .add-task-form {
      display: flex;
      gap: 1rem;
      margin-bottom: 2rem;
    }
    
    .task-input {
      flex: 1;
      padding: 0.75rem;
      border: 2px solid #ddd;
      border-radius: 4px;
      font-size: 1rem;
    }
    
    .task-input:focus {
      outline: none;
      border-color: #3498db;
    }
    
    .btn {
      padding: 0.75rem 1.5rem;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      font-weight: 500;
      transition: all 0.3s;
    }
    
    .btn-primary {
      background-color: #3498db;
      color: white;
    }
    
    .btn-primary:hover {
      background-color: #2980b9;
    }
    
    .btn-status {
      background-color: #95a5a6;
      color: white;
    }
    
    .btn-status:hover {
      background-color: #7f8c8d;
    }
    
    .btn-danger {
      background-color: #e74c3c;
      color: white;
    }
    
    .btn-danger:hover {
      background-color: #c0392b;
    }
    
    .loading {
      text-align: center;
      padding: 2rem;
      color: #7f8c8d;
    }
    
    .no-tasks {
      text-align: center;
      padding: 3rem;
      color: #95a5a6;
      font-size: 1.1rem;
    }
    
    .tasks {
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }
    
    .task-item {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 1.5rem;
      border-radius: 8px;
      background-color: #fff;
      border-left: 4px solid #3498db;
      box-shadow: 0 2px 4px rgba(0,0,0,0.1);
      transition: transform 0.2s;
    }
    
    .task-item:hover {
      transform: translateY(-2px);
      box-shadow: 0 4px 8px rgba(0,0,0,0.15);
    }
    
    .task-item.status-todo {
      border-left-color: #3498db;
    }
    
    .task-item.status-doing {
      border-left-color: #f39c12;
    }
    
    .task-item.status-done {
      border-left-color: #2ecc71;
    }
    
    .task-content h3 {
      margin: 0 0 0.5rem 0;
      color: #2c3e50;
    }
    
    .task-status {
      display: inline-block;
      padding: 0.25rem 0.75rem;
      border-radius: 12px;
      font-size: 0.85rem;
      font-weight: 600;
      text-transform: uppercase;
    }
    
    .status-todo .task-status {
      background-color: #e3f2fd;
      color: #1976d2;
    }
    
    .status-doing .task-status {
      background-color: #fff3e0;
      color: #f57c00;
    }
    
    .status-done .task-status {
      background-color: #e8f5e9;
      color: #388e3c;
    }
    
    .task-actions {
      display: flex;
      gap: 0.5rem;
    }
    </style>