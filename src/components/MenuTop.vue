<template>
    <div id="main">
      <div class="wrap">
        <nav v-bind:class="active" v-on:click.prevent>
            <router-link to="/" class="home" @click.native="makeActive('home')">Hlavní stránka</router-link>
            <router-link to="/" class="timeline" @click.native="makeActive('timeline')">Časová osa</router-link>
            <router-link to="/" class="my_hives" @click.native="makeActive('my_hives')">Moje úly</router-link>
            <router-link to="/settings" class="profile" @click.native="makeActive('profile')">Profil</router-link>
            <a @click="logout()">Odhlásit se</a>
            <!-- <li><a @click="logout()">Odhlásit se</a></li> -->
        </nav>
      </div>
    <!-- <p> Toto bude stránka <b>{{ active }}</b></p> -->
    </div>

</template>

<script>
export default {
  name: 'MenuTop',
  data() {
    return { active: 'home' }
  },
  methods: {
    makeActive: function(item){
      this.active = item;
    },
    logout() {
      this.$store.dispatch('logout')
    }
  }
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
*{
  margin:0;
  padding:0;
}

body{
  font:15px/1.3 'Open Sans', sans-serif;
  color: #5e5b64;
  text-align:left;
}

a, a:visited {
  outline:none;
  color:#389dc1;
}

a:hover{
  text-decoration:none;
}

section, footer, header, aside, nav{
  display: block;
}

/*-------------------------
  The menu
--------------------------*/

div.wrap{
  width: 100%;
  background-color: #FF8181; /* #FFC700 nice yellow*/
  float:right;
  margin-bottom: 20px;
}

nav{
  float: right;
  /* display:inline-block; */
  /* margin:60px auto 45px; */
  background-color:#FF8181;
  box-shadow:0 1px 1px #ccc;
  border-radius:2px;
}

nav a{
  display:inline-block;
  padding: 18px 30px;
  color:rgb(0, 0, 0) !important;
  font-weight:bold;
  font-size:16px;
  text-decoration:none !important;
  line-height:1;
  text-transform: uppercase;
  background-color:transparent;

  -webkit-transition:background-color 0.25s;
  -moz-transition:background-color 0.25s;
  transition:background-color 0.25s;
}

nav a:hover {
  background-color: #FFCACA; /* #fadb6a nice light yellow */
  cursor: pointer;
}

nav a:first-child{
  border-radius:2px 0 0 2px;
}

nav a:last-child{
  border-radius:0 2px 2px 0;
}

nav.home .home,
nav.timeline .timeline,
nav.my_hives .my_hives,
nav.profile .profile{
  background-color:#FFCACA;
}

p{
  font-size:22px;
  font-weight:bold;
  color:#7d9098;
}

p b{
  color:#ffffff;
  display:inline-block;
  padding:5px 10px;
  background-color:#c4d7e0;
  border-radius:2px;
  text-transform:uppercase;
  font-size:18px;
}
.resource {
  margin: 20px 0;
}
</style>
