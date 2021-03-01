import Vue from 'vue'
import App from './App.vue'
import router from './router'
// import store from './store'
import { auth } from './firebase'
// import './assets/scss/app.scss'

Vue.config.productionTip = false

let app
auth.onAuthStateChanged(() => {
  if (!app) {
    app = new Vue({
      router,
      render: h => h(App)
    }).$mount('#app')
  }
})

// takto to spustim
// cd bee_diary
// npm run serve

// https://code.visualstudio.com/docs/nodejs/vuejs-tutorial