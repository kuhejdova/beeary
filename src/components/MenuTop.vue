<template>
  <nav v-bind:class="active" v-on:click.prevent>
    <router-link to="/" class="logo"
      ><img src="../../public/images/logo_text.svg" alt="Beeary"
    /></router-link>

    <router-link to="/home" class="home"
      >Hlavní stránka</router-link
    >
    <router-link
      to="/timeline"
      class="timeline"
      >Časová osa</router-link
    >
    <router-link
      to="/hives"
      class="my_hives"
      >Moje úly</router-link
    >
    <router-link
      to="/settings"
      class="profile"
      >Profil</router-link
    >
    <a @click="logout()">Odhlásit se</a>
    <!-- <li><a @click="logout()">Odhlásit se</a></li> -->
  </nav>
  <!-- <p> Toto bude stránka <b>{{ active }}</b></p> -->
</template>

<script>
const routeMap = {
  "/hives": "my_hives",
  "/timeline": "timeline",
  "/settings": "profile",
  "/home": "home"
}

export default {
  name: "MenuTop",
  data() {
    return { active: "home" };
  },
  methods: {
    logout() {
      this.$store.dispatch("logout");
    },
  },
  watch:{
    $route (to){
      console.log(routeMap[to.path])
      this.active = routeMap[to.path]??'home';
    }
  },
mounted(){
  this.active = routeMap[this.$route.path]??'home';
  
}
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
a,
a:visited {
  outline: none;
  color: #389dc1;
}

a:hover {
  text-decoration: none;
}

nav {
  display: block;
}

.push {
  margin-left: auto;
}
/*-------------------------
  The menu
--------------------------*/

nav {
  /* display:inline-block; */
  /* margin:60px auto 45px; */
  background-color: var(--main_color);
  box-shadow: 0 1px 1px #ccc;
  border-radius: 2px;
  display: flex;
  justify-content: flex-end;
  height: 60px;
}

nav a {
  display: inline-block;
  padding: 18px 30px;
  color: rgb(0, 0, 0) !important;
  font-weight: bold;
  font-size: 16px;
  text-decoration: none !important;
  line-height: 1;
  text-transform: uppercase;
  background-color: transparent;

  -webkit-transition: background-color 0.25s;
  -moz-transition: background-color 0.25s;
  transition: background-color 0.25s;
}

nav a:hover {
  background-color: var(--light_color); /* #fadb6a nice light yellow */
  cursor: pointer;
}

nav a:first-child {
  border-radius: 2px 0 0 2px;
}

nav a:last-child {
  border-radius: 0 2px 2px 0;
}

nav.home .home,
nav.timeline .timeline,
nav.my_hives .my_hives,
nav.profile .profile {
  background-color: var(--light_color);
  /* margin-left: auto; */
}

.logo:hover {
  background-color: var(--main_color);
}

.logo {
  margin-right: auto;
  height: auto;
}

p {
  font-size: 22px;
  font-weight: bold;
  color: #7d9098;
}

p b {
  color: #ffffff;
  display: inline-block;
  padding: 5px 10px;
  background-color: #c4d7e0;
  border-radius: 2px;
  text-transform: uppercase;
  font-size: 18px;
}

a.logoImg {
  display: inline-block;
  padding: 4px 20px;
  color: rgb(0, 0, 0) !important;
  font-weight: bold;
  font-size: 16px;
  text-decoration: none !important;
  line-height: 1;
  text-transform: uppercase;
  background-color: transparent;
  vertical-align: middle;
  margin-right: auto;

  -webkit-transition: background-color 0.25s;
  -moz-transition: background-color 0.25s;
  transition: background-color 0.25s;
}

a.logoImg:hover {
  background-color: var(--main_color); /* #fadb6a nice light yellow */
}

img {
  height: 40px;
  padding: 0px;
  margin: -15px;
}

/* .resource {
  margin: 20px 0;
} */
</style>
