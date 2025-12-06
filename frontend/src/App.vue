<script setup>
  import { RouterLink, RouterView } from 'vue-router'
  </script>
  
  <template>
    <div id="app">
      <header>
        <nav class="navbar">
          <div class="container">
            <h1 class="logo">📋 TaskBoard</h1>
            <div class="nav-links">
              <RouterLink to="/tasks" class="nav-link">Tasks</RouterLink>
              <RouterLink to="/dashboard" class="nav-link">Dashboard</RouterLink>
            </div>
          </div>
        </nav>
      </header>
      
      <main class="main-content">
        <RouterView />
      </main>
    </div>
  </template>
  
  <style scoped>
  .navbar {
    background-color: #2c3e50;
    padding: 1rem 0;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  }
  
  .container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 2rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  
  .logo {
    color: white;
    margin: 0;
    font-size: 1.5rem;
  }
  
  .nav-links {
    display: flex;
    gap: 2rem;
  }
  
  .nav-link {
    color: #ecf0f1;
    text-decoration: none;
    font-weight: 500;
    transition: color 0.3s;
  }
  
  .nav-link:hover,
  .nav-link.router-link-active {
    color: #3498db;
  }
  
  .main-content {
    max-width: 1200px;
    margin: 2rem auto;
    padding: 0 2rem;
  }
  </style>