import { createApp } from 'vue'
import App from './App.vue'
import Notifications from 'notiwind'
import './index.css'
import router from './router'

createApp(App)
  .use(router)
  .use(Notifications)
  .mount('#app')
