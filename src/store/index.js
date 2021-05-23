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
        context.commit("setJwtToken", { jwt: response.data.token });
        axios.defaults.headers.common["Authorization"] = localStorage.token;
        EventBus.$emit("successfullAuth");
      })
      .catch((error) => {
        EventBus.$emit("failedAuthentication", error);
      });
  },
  register(context, userData) {
    context.commit("setUserData", { userData });
    return register(userData)
      .then(() => context.dispatch("login", userData))
      .catch((error) => {
        EventBus.$emit("failedRegistering: ", error);
        throw error;
      });
  },
  logout() {
    localStorage.removeItem("token");
    delete axios.defaults.headers.common["Authorization"];
  },
};

const mutations = {
  setUserData(state, payload) {
    localStorage.userEmail = payload.userData.email;
    state.userData = payload.userData;
  },
  setJwtToken(state, payload) {
    localStorage.token = payload.jwt;
    state.jwt = payload.jwt;
  },
};

const getters = {
  // reusable data accessors
  isAuthenticated(state) {
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
