// routes/index.ts

import { createRouter, createWebHistory } from 'vue-router';
import Login from '../components/Login.vue';
import Submission from '../components/Submission.vue';
import Students from '../components/Students.vue';
import Home from '../components/Home.vue';
import { isAuthenticated } from '../utils/auth';

const routes = [
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/submission',
    name: 'Submission',
    component: Submission,
    beforeEnter: async (to : any, from : any, next : any) => {
      const authenticated = await isAuthenticated();
      if (authenticated) {
        next();
      } else {
        next('/login'); // Redirecionar para a página de login se não estiver autenticado
      }
    }
  },
  {
    path: '/students',
    name: 'Students',
    component: Students,
    beforeEnter: async (to : any, from : any, next : any) => {
      const authenticated = await isAuthenticated();
      if (authenticated) {
        next();
      } else {
        next('/login'); // Redirecionar para a página de login se não estiver autenticado
      }
    }
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
