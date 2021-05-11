// import Vue from 'vue'
// import Vuex from 'vuex'
// import * as fb from '../firebase'
// import "firebase/auth";
// import router from '../router/index.js'

// Vue.use(Vuex)

// export default new Vuex.Store({
//   state: {
//     userProfile: {}
//   },
//   mutations: {
//     setUserProfile(state, val) {
//       state.userProfile = val
//     }
//   },
//   actions: {
//     async login({ dispatch }, form) {
//       // sign user in
//       const { user } = await fb.auth.signInWithEmailAndPassword(form.email, form.password)

//       // fetch user profile and set in state
//       dispatch('fetchUserProfile', user)
//     },
//     async signup({ dispatch }, form) {
//       // sign user up
//       const { user } = await fb.auth.createUserWithEmailAndPassword(form.email, form.password)

//       // create user object in userCollections
//       await fb.usersCollection.doc(user.uid).set({
//         name: form.name,
//         // title: form.title
//       })

//       // fetch user profile and set in state
//       dispatch('fetchUserProfile', user)
//     },
//     async fetchUserProfile({ commit }, user) {
//       // fetch user profile
//       const userProfile = await fb.usersCollection.doc(user.uid).get()

//       // set user profile in state
//       commit('setUserProfile', userProfile.data())

//       // change route to dashboard
//       if (router.currentRoute.path === '/login') {
//         router.push('/home')
//       }
//     },
//     async logout({ commit }) {
//       // log user out
//       await fb.auth.signOut()

//       // clear user data from state
//       commit('setUserProfile', {})

//       // redirect to login view
//       router.push('/login')
//     },
//   }
// })

import Vue from "vue";
import Vuex from "vuex";

import { authenticate, register } from "@/api";
import { isValidJwt, EventBus } from "@/utils";

import axios from "axios";

Vue.use(Vuex);

const state = {
  // single source of data
  user: {},
  jwt: localStorage.token || "",
};

const actions = {
  // asynchronous operations
  login(context, userData) {
    context.commit("setUserData", { userData });
    return authenticate(userData)
      .then((response) => {
        // console.log("reposnse: ", response.data);
        context.commit('setJwtToken', { jwt: response.data.token });
        axios.defaults.headers.common["Authorization"] = localStorage.token;
      })
      .catch((error) => {
        // console.log("Error Authenticating: ", error);
        EventBus.$emit("failedAuthentication", error);
        alert("Chybně zadaný email nebo heslo");
      });
  },
  register(context, userData) {
    context.commit("setUserData", { userData });
    return register(userData)
      .then(context.dispatch("login", userData))
      .catch((error) => {
        // console.log("Error Registering: ", error);
        EventBus.$emit("failedRegistering: ", error);
        alert("Zadaný email již existuje");
      });
  },
  logout() {
    localStorage.removeItem("token");
    delete axios.defaults.headers.common["Authorization"];
  },
};

const mutations = {
  setUserData(state, payload) {
    // console.log('setUserData payload = ', payload)
    localStorage.userEmail = payload.userData.email;
    state.userData = payload.userData;
  },
  setJwtToken(state, payload) {
    // console.log("setJwtToken payload = ", payload);
    localStorage.token = payload.jwt;
    state.jwt = payload.jwt;
  },
};

const getters = {
  // reusable data accessors
  isAuthenticated(state) {
    // console.log(state)
    // console.log(isValidJwt(state.jwt))
    return isValidJwt(state.jwt);
  },
};

const store = new Vuex.Store({
  state,
  actions,
  mutations,
  getters,
});

export default store;
