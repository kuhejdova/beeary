<template>
  <div id="app">
    <MenuTop v-show="isVisible()"/>
    <router-view/>
  </div>
</template>

<script>

import MenuTop from './components/MenuTop.vue'

export default {
  name: 'App',
  components: {
    MenuTop
  },

  methods:{
    isVisible(){
      const sites = ['/', '/login', '']
      console.log(window.location.href)
      console.log(sites.includes(window.location.pathname) )
      return !sites.includes(window.location.pathname) 
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
}

:root {
    --main_color: #7FD97E;
    --light_color: #ABDFAA;
    --additional_color: #D3F4D3;
  }
</style>
