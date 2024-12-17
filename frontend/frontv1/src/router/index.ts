import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router';
import Login from '../components/Login.vue';
import Submission from '../components/Submission.vue';
import Students from '../components/Students.vue';
import Home from '../components/Home.vue';
import { isAuthenticated} from '../utils/auth';
import Profile from '../components/Profile.vue';
import StudentDetail from '../components/StudentDetail.vue';
import SubmissionDetail from '../components/SubmissionDetail.vue';

const routes: Array<RouteRecordRaw> = [
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/',
    name: 'Home',
    component: Home,
    meta: { requiresAuth: true, requiresAdmin: true }
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
    meta: { requiresAuth: true, requiresAdmin: true }
  },
  {
    path: '/submission/:cpf',
    name: 'SubmissionDetails',
    component: SubmissionDetail,
    meta: { requiresAuth: true, requiresAdmin: true }
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
  console.log(`Navegando de ${from.fullPath} para ${to.fullPath}`); 

  if (to.meta.requiresAuth) {
    const authenticated = await isAuthenticated();
    if (!authenticated) {
      return next('/login');
    }
  }

  if (to.meta.requiresAdmin) {
    try {
      const role = sessionStorage.getItem('role');
      const isAdmin = role === 'admin';

      if (!isAdmin) {
        return next('/submission');
      }
    } catch (error) {
      console.error('Erro ao verificar permissões de administrador:', error);
      return next('/submission');
    }
  }

  next();
});


export default router;
