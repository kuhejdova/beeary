<template>
  <div id="app">
    <!-- <MenuTop /> -->
    <!-- <MenuTop v-if="userstate"/> -->
    <!-- <SiteNav v-if="showNav"></SiteNav> -->
    <!-- <div>{{userstate}}</div> -->
    <router-view/>
  </div>
</template>

<script>
// import { mapState } from 'vuex'
// import MenuTop from './components/MenuTop.vue'
// import SiteNav from './components/SiteNav.vue'
// import firebase from './firebase'
// import "firebase/auth";


export default {
  name: 'App',
  // data() {
  //   return{
  //     // userstate: (firebase.auth().onAuthStateChanged() && firebase.auth().currentUser ? false : true)
  //     userstate: firebase.auth().currentUser
  //     // userstate: true
  //   }
    
  // },
  // // components: {
  // //   // SiteNav,
  // //   MenuTop,
  // // },
  // methods: {
  //   // ...mapState(['userProfile']),
  //   // showNav() {
  //   //   console.log(this.userProfile)
  //   //   console.log(Object.keys(this.userProfile).length)
  //   //   return Object.keys(this.userProfile).length > 0
  //   // },
  //   change_userstate(){
  //     this.userstate = firebase.auth().currentUser; 
  //     // return this.$userstate;
  //   }
  // }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  /* margin-top: 60px; */
}
</style>
