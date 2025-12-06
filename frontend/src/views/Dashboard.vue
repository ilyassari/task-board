<script setup>
    import { ref, onMounted, onUnmounted } from 'vue'
    import { getStats } from '../services/api'
    
    const stats = ref({
      todo: 0,
      doing: 0,
      done: 0
    })
    const loading = ref(false)
    const error = ref(null)
    let intervalId = null
    
    const fetchStats = async () => {
      loading.value = true
      error.value = null
      try {
        const response = await getStats()
        stats.value = response.data
      } catch (err) {
        error.value = 'Failed to fetch statistics'
        console.error(err)
      } finally {
        loading.value = false
      }
    }
    
    const getTotalTasks = () => {
      return stats.value.todo + stats.value.doing + stats.value.done
    }
    
    const getPercentage = (count) => {
      const total = getTotalTasks()
      return total > 0 ? Math.round((count / total) * 100) : 0
    }
    
    onMounted(() => {
      fetchStats()
      // Refresh stats every 5 seconds
      intervalId = setInterval(fetchStats, 5000)
    })
    
    onUnmounted(() => {
      if (intervalId) {
        clearInterval(intervalId)
      }
    })
    </script>
    
    <template>
      <div class="dashboard">
        <h2>Task Statistics Dashboard</h2>
        
        <!-- Error Message -->
        <div v-if="error" class="error-message">
          {{ error }}
        </div>
        
        <!-- Loading -->
        <div v-if="loading && getTotalTasks() === 0" class="loading">
          Loading statistics...
        </div>
        
        <!-- Stats Cards -->
        <div v-else class="stats-container">
          <!-- Total Tasks -->
          <div class="stat-card total">
            <div class="stat-icon">📊</div>
            <div class="stat-content">
              <h3>Total Tasks</h3>
              <p class="stat-number">{{ getTotalTasks() }}</p>
            </div>
          </div>
          
          <!-- To Do -->
          <div class="stat-card todo">
            <div class="stat-icon">📝</div>
            <div class="stat-content">
              <h3>To Do</h3>
              <p class="stat-number">{{ stats.todo }}</p>
              <p class="stat-percentage">{{ getPercentage(stats.todo) }}%</p>
            </div>
          </div>
          
          <!-- Doing -->
          <div class="stat-card doing">
            <div class="stat-icon">⚙️</div>
            <div class="stat-content">
              <h3>Doing</h3>
              <p class="stat-number">{{ stats.doing }}</p>
              <p class="stat-percentage">{{ getPercentage(stats.doing) }}%</p>
            </div>
          </div>
          
          <!-- Done -->
          <div class="stat-card done">
            <div class="stat-icon">✅</div>
            <div class="stat-content">
              <h3>Done</h3>
              <p class="stat-number">{{ stats.done }}</p>
              <p class="stat-percentage">{{ getPercentage(stats.done) }}%</p>
            </div>
          </div>
        </div>
        
        <!-- Auto-refresh indicator -->
        <div class="refresh-info">
          <span class="refresh-dot"></span>
          Auto-refreshing every 5 seconds
        </div>
      </div>
    </template>
    
    <style scoped>
    .dashboard {
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
    
    .loading {
      text-align: center;
      padding: 3rem;
      color: #7f8c8d;
      font-size: 1.1rem;
    }
    
    .stats-container {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 1.5rem;
      margin-bottom: 2rem;
    }
    
    .stat-card {
      display: flex;
      align-items: center;
      gap: 1.5rem;
      padding: 2rem;
      background-color: #fff;
      border-radius: 12px;
      box-shadow: 0 4px 6px rgba(0,0,0,0.1);
      transition: transform 0.3s, box-shadow 0.3s;
    }
    
    .stat-card:hover {
      transform: translateY(-4px);
      box-shadow: 0 8px 12px rgba(0,0,0,0.15);
    }
    
    .stat-card.total {
      border-left: 4px solid #9b59b6;
    }
    
    .stat-card.todo {
      border-left: 4px solid #3498db;
    }
    
    .stat-card.doing {
      border-left: 4px solid #f39c12;
    }
    
    .stat-card.done {
      border-left: 4px solid #2ecc71;
    }
    
    .stat-icon {
      font-size: 3rem;
    }
    
    .stat-content {
      flex: 1;
    }
    
    .stat-content h3 {
      margin: 0 0 0.5rem 0;
      color: #7f8c8d;
      font-size: 0.9rem;
      text-transform: uppercase;
      letter-spacing: 1px;
    }
    
    .stat-number {
      margin: 0;
      font-size: 2.5rem;
      font-weight: bold;
      color: #2c3e50;
    }
    
    .stat-percentage {
      margin: 0.5rem 0 0 0;
      color: #95a5a6;
      font-size: 0.9rem;
    }
    
    .refresh-info {
      text-align: center;
      color: #95a5a6;
      font-size: 0.9rem;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 0.5rem;
    }
    
    .refresh-dot {
      display: inline-block;
      width: 8px;
      height: 8px;
      background-color: #2ecc71;
      border-radius: 50%;
      animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
      0%, 100% {
        opacity: 1;
      }
      50% {
        opacity: 0.3;
      }
    }
    </style>