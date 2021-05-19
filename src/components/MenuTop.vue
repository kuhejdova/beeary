<template>
  <div class="wrap">
    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"
    />
    <nav v-bind:class="active" v-on:click.prevent id="myTopnav" class="topnav">
      <router-link to="/" class="logo"
        ><img src="../../public/images/logo_text.svg" alt="Beeary"
      /></router-link>

      <router-link to="/home" class="home">Hlavní stránka</router-link>
      <router-link to="/timeline" class="timeline">Časová osa</router-link>
      <router-link to="/hives" class="my_hives">Moje úly</router-link>
      <router-link to="/settings" class="profile">Nastavení</router-link>

      <a @click="logout()">Odhlásit se</a>

      <a href="javascript:void(0);" class="icon" @click="burgerMenu()">
        <i class="fa fa-bars"></i>
      </a>
    </nav>
  </div>
</template>

<script>
const routeMap = {
  "/hives": "my_hives",
  "/timeline": "timeline",
  "/settings": "profile",
  "/home": "home",
};

export default {
  name: "MenuTop",
  data() {
    return { active: "home" };
  },
  methods: {
    logout() {
      this.$store.dispatch("logout").then(() => this.$router.push("/login"));
    },

    burgerMenu() {
      var x = document.getElementById("myTopnav");
      if (x.className != "topnav responsive") {
        x.className = "topnav responsive";
      } else {
        x.className = "topnav";
      }
    },
  },
  watch: {
    $route(to) {
      this.active = routeMap[to.path] ?? "home";
    },
  },
  mounted() {
    this.active = routeMap[this.$route.path] ?? "home";
  },
};
</script>

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

.wrap {
  background-color: var(--main_color);
}

.topnav {
  background-color: var(--main_color);
  box-shadow: 0 1px 1px #ccc;
  border-radius: 2px;
  display: flex;
  justify-content: flex-end;
  height: 60px;
}

.topnav a {
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

.topnav a:hover {
  background-color: var(--light_color);
  cursor: pointer;
}

.topnav a:first-child {
  border-radius: 2px 0 0 2px;
}

.topnav a:last-child {
  border-radius: 0 2px 2px 0;
}

.topnav.home .home,
.topnav.timeline .timeline,
.topnav.my_hives .my_hives,
.topnav.profile .profile {
  background-color: var(--light_color);
}

.topnav .icon {
  display: none;
}

@media screen and (max-width: 700px) {
  .topnav a:not(:first-child) {
    display: none;
  }
  .topnav a.icon {
    float: right;
    padding: 0px;
    width: 60px;
    height: 60px;
    display: flex;
    justify-content: center;
    align-items: center;  }



  .topnav.responsive {
    position: relative;
  }
  .topnav.responsive a.icon {
    position: absolute;
    right: 0;
    top: 0;
  }
  .topnav.responsive a:not(.icon) {
    float: none;
    display: block;
    text-align: left;
  }

  .topnav {
    display: block;
    height: unset;
    background-color: var(--main_color);
    min-height: 60px;
    /* height: 60px; */
  }

  .logo {
    float: left;
  }
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
  background-color: var(--main_color);
}

img {
  height: 40px;
  padding: 0px;
  margin: -15px;
}
</style>
