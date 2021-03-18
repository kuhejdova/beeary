import Vue from 'vue'
import VueRouter from 'vue-router'
import Dashboard from '../views/Dashboard.vue'
import Landing from '../views/Landing.vue'
import Hives from '../views/MyHives.vue'

import Ping from '../components/Ping.vue';
// import App from '../App.vue'
import { auth } from '../firebase'

Vue.use(VueRouter)

const routes = [
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
    {
      path: '/home',
      name: 'Dashboard',
      component: Dashboard,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/',
      name: 'Landing',
      component: Landing,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/hives',
      name: 'Hives',
      component: Hives,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/login',
      name: 'Login',
      component: () => import( /* webpackChunkName: "login" */ '../views/Login.vue')
    },
    {
      path: '/settings',
      name: 'settings',
      component: () => import( /* webpackChunkName: "settings" */ '../views/Settings.vue'),
      meta: {
        requiresAuth: true
      }
    }
  ]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
    const requiresAuth = to.matched.some(x => x.meta.requiresAuth)
    if (window.location.href == 'http://0.0.0.0:8080/'){
      next()
    }
    else if (requiresAuth && !auth.currentUser ) {
      next('/login')
    } else {
      next()
    }
  })

export default router