import Vue from 'vue'
import VueRouter from 'vue-router'
import Dashboard from '../views/Dashboard.vue'
import Landing from '../views/Landing.vue'
import Hives from '../views/MyHives.vue'
import NotFound from '../views/NotFound.vue'

import Ping from '../components/Ping.vue';

import TimelineDetail from '../views/TimelineDetail.vue'

// import App from '../App.vue'
// import { auth } from '../firebase'
import store from '@/store'

import moment from "moment";

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
      },
      props: function (route) {
        return { query: route.query.hid != null ? route.query.hid : ""}
      }, 
    },
    {
      path: '/timeline',
      name: 'TimelineDetail',
      component: TimelineDetail,
      meta: {
        requiresAuth: true
      },
      props: function (route) {
        return { query: route.query.date != null ? route.query.date :  moment(new Date()).format("M-YYYY")}
      },     
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
    },
    {
      path: '*',
      name: 'notFound',
      component: NotFound
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
    else if (requiresAuth && !store.getters.isAuthenticated ) {
      next('/login')
    } else {
      next()
    }
  })

export default router