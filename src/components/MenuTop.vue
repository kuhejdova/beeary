<template>
    <div id="main">
      <div class="wrap">
        <nav v-bind:class="active" v-on:click.prevent>
            <a href="#" class="home" v-on:click="makeActive('home')">Hlavní stránka</a>
            <a href="#" class="timeline" v-on:click="makeActive('timeline')">Časová osa</a>
            <a href="#" class="my_hives" v-on:click="makeActive('my_hives')">Moje úly</a>
            <a href="#" class="profile" v-on:click="makeActive('profile')">Profil</a>
        </nav>
      </div>
    <p> Toto bude stránka <b>{{ active }}</b></p>
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
  background-color: #FFC700;
  float:right;
  margin-bottom: 20px;
}

nav{
  float: right;
  /* display:inline-block; */
  /* margin:60px auto 45px; */
  background-color:#FFC700;
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
  background-color: #fadb6a;
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
  background-color:#fadb6a;
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
