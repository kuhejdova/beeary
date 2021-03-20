<template>
  <nav v-bind:class="active" v-on:click.prevent>
    <router-link to="/home" class="home" @click.native="makeActive('home')"
      >Hlavní stránka</router-link
    >
    <router-link to="/timeline" class="timeline" @click.native="makeActive('timeline')"
      >Časová osa</router-link
    >
    <router-link
      to="/hives"
      class="my_hives"
      @click.native="makeActive('my_hives')"
      >Moje úly</router-link
    >
    <router-link
      to="/settings"
      class="profile"
      @click.native="makeActive('profile')"
      >Profil</router-link
    >
    <a @click="logout()">Odhlásit se</a>
    <!-- <li><a @click="logout()">Odhlásit se</a></li> -->
  </nav>
  <!-- <p> Toto bude stránka <b>{{ active }}</b></p> -->
</template>

<script>
export default {
  name: "MenuTop",
  data() {
    return { active: "home" };
  },
  methods: {
    makeActive: function(item) {
      this.active = item;
    },
    logout() {
      this.$store.dispatch("logout");
    },
  },
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
/* .resource {
  margin: 20px 0;
} */
</style>
