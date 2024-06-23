import { createRouter, createWebHistory } from 'vue-router'
import Login from '../components/Login.vue'
import Submission from '../components/Submission.vue'
import Students from '../components/Students.vue'



const routes = [
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/submission',
    name: 'Submission',
    component: Submission
  },
  {
    path: '/students',
    name: 'Students',
    component: Students
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
