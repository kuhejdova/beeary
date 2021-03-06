<template>
  <header>
    <section>
      <div class="grid-container">

        <div class="logo">
        <img src="../../public/beeary_logo_v1.png" alt="Beeary">
        </div>

        <div class="logo-subtitle">
        <p>Webová aplikace pro všechny včelaře. Ovládněte včelařství.</p>
        </div>
      
        <div class="pictogram1">
          <img src="../../public/p1.png" alt="Beeary">
        </div>
        <div class="pictogram2">
          <img src="../../public/p1.png" alt="Beeary">
        </div>
        <div class="pictogram3">
          <img src="../../public/p1.png" alt="Beeary">
        </div>

        <div class="description1">
          <p>Přehled všech úlů</p>
        </div>
        <div class="description2">
          <p>Ćasová osa s poznámkami</p>
        </div>
        <div class="description3">
          <p>Celoroční monitoring</p>
        </div>

        <div class="button">
          <button @click="redirectHome" class="button">Pojď začít</button>
        </div>
      </div>
    </section>
  </header>
</template>

<script>
import { auth } from '../firebase'

export default {
  methods: {
    redirectHome(){
      if (!auth.currentUser ) {
      // next('/login')
        this.$router.push('/login')
      }
      else {
        this.$router.push('/home')
      }
    }
  }
}
</script>

<style scoped>
*{
  margin:0;
  padding:0;

}

.logo { grid-area: logo; }
.logo-subtitle { grid-area: logo-subtitle; }
.pictogram1 { grid-area: pictogram1; }
.pictogram2  { grid-area: pictogram2; }
.pictogram3  { grid-area: pictogram3; }
.description1 { grid-area: description1; }
.description2 { grid-area: description2; }
.description3 { grid-area: description3; }
.button { grid-area: button; }

.grid-container {
  display: grid;
  grid-template-areas:
    'logo logo logo'
    'logo-subtitle logo-subtitle logo-subtitle'
    'pictogram1 pictogram2 pictogram3'
    'description1 description2 description3'
    'button button button';
  grid-template-rows: 30% 10% 40% 10% 5%;
  grid-gap: 20px;
  /* background-color: #2196F3;
  padding: 10px; */
  height: calc(100vh - 100px);
  padding-right: 5%;
  padding-left: 5%;
  padding-bottom: 3%
}


/* .grid-container{
  display: grid;
  grid-row-gap: 20px;
  grid-template-columns: auto;
  grid-template-rows: 30% 10% 50% 5%;
  height: calc(100vh - 80px);
} */
.grid-container > div {
  background-color: rgba(255, 255, 255, 0.8);
}

body{
  font:15px/1.3 'Open Sans', sans-serif;
  color: #5e5b64;
  text-align:left;
}

#login{
  margin-top: 200px;
}

div{
  margin-bottom: 10px;
}
h1 {
  margin-bottom: 20px;
}

img {
  height: 100%
}


section, footer, header, aside, nav{
  display: block;
}

/*-------------------------
  The menu
--------------------------*/

button{
  display:inline-block;
  padding: 10px 22px;
  color:rgb(0, 0, 0) !important;
  font-weight:bold;
  font-size:14px;
  text-decoration:none !important;
  line-height:1;
  text-transform: uppercase;
  background-color:#FF8181;

  -webkit-transition:background-color 0.25s;
  -moz-transition:background-color 0.25s;
  transition:background-color 0.25s;
}

button:hover {
  background-color: #FFCACA; /* #fadb6a nice light yellow */
  cursor: pointer;
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