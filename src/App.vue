<template>
  <div id="app">
    <MenuTop/>
    <SiteNav v-if="showNav"></SiteNav>
    <router-view/>
    <!-- <img alt="Forsage" src="./assets/forsage_logo.png" width="250" height="250"> -->
    <!-- <HelloWorld msg="Hello World!"/> -->
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import { mapState } from 'vuex'
import MenuTop from './components/MenuTop.vue'
import SiteNav from './components/SiteNav.vue'

export default {
  name: 'App',
  components: {
    SiteNav,
    MenuTop,
  },
  computed: {
    ...mapState(['userProfile']),
    showNav() {
      return Object.keys(this.userProfile).length > 1
    }
  }
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
