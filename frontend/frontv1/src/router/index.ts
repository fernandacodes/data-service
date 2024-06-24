// routes/index.ts

import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router';
import Login from '../components/Login.vue';
import Submission from '../components/Submission.vue';
import Students from '../components/Students.vue';
import Home from '../components/Home.vue';
import { isAuthenticated, isAdm } from '../utils/auth';
import Profile from '../components/Profile.vue';
import StudentDetail from '../components/StudentDetail.vue';
const routes: Array<RouteRecordRaw> = [
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
    path: '/profile',
    name: 'Profile',
    component: Profile,
    meta: { requiresAuth: true }
  },
  {
    path: '/student/:cpf',
    name: 'StudentDetails',
    component: StudentDetail,
    meta: { requiresAuth: true, requiresAdmin: true}
  },
  {
    path: '/submission',
    name: 'Submission',
    component: Submission,
    meta: { requiresAuth: true }
  },
  {
    path: '/students',
    name: 'Students',
    component: Students,
    meta: { requiresAuth: true, requiresAdmin: true }
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

router.beforeEach(async (to, from, next) => {
  // Verifica se a rota requer autenticação
  if (to.meta.requiresAuth) {
    const authenticated = await isAuthenticated();
    if (!authenticated) {
      return next('/login');
    }
  }

  // Verifica se a rota requer administrador
  if (to.meta.requiresAdmin) {
    try {
      const isAdmin = await isAdm();
      if (!isAdmin) {
        return next('/');
      }
    } catch (error) {
      console.error('Erro ao verificar permissões de administrador:', error);
      return next('/');
    }
  }

  next();
});

export default router;
