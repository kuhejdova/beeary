<template>
    <div class="grid-container">
      <div class="logo">
        <img src="../../public/images/logo_text.svg" alt="Beeary" />
      </div>

      <div class="logo-subtitle">
        <p>Webová aplikace pro všechny včelaře. Ovládněte včelařství.</p>
      </div>
      <div class="pictograms">
        <div class="pictogram1">
          <object
            id="svgSetColor"
            type="image/svg+xml"
            :data="svgHives"
            v-on:load="loadSetColor"
          >
            <img src="../../public/images/hives.svg" alt="Beeary" />
          </object>
          <p>Přehled všech úlů</p>
        </div>
        <div class="pictogram2">
          <object
            id="svgSetColor"
            type="image/svg+xml"
            :data="svgTimeline"
            v-on:load="loadSetColor"
          >
            <img src="../../public/images/timeline.svg" alt="Beeary" />
          </object>
          <p>Časová osa s poznámkami</p>
          <!-- <img src="../../public/images/timeline.svg" alt="Beeary" /> -->
        </div>
        <div class="pictogram3">
          <object
            id="svgSetColor"
            type="image/svg+xml"
            :data="svgMonitoring"
            v-on:load="loadSetColor"
          >
            <img src="../../public/images/monitoring.svg" alt="Beeary" />
          </object>
          <p>Celoroční monitoring</p>
          <!-- <img src="../../public/images/monitoring.svg" alt="Beeary" /> -->
        </div>
      </div>
      <div class="buttonwrapper">
        <button @click="redirectHome" class="button">Pojď začít</button>
      </div>
    </div>
</template>

<script>
import { auth } from "../firebase";

export default {
  data() {
    return {
      svgHives: require("../../public/images/hives.svg"),
      svgTimeline: require("../../public/images/timeline.svg"),
      svgMonitoring: require("../../public/images/monitoring.svg"),
    };
  },
  methods: {
    redirectHome() {
      if (!auth.currentUser) {
        this.$router.push("/login");
      } else {
        this.$router.push("/home");
      }
    },

    loadSetColor(event) {
      var documentStyle = getComputedStyle(document.body);
      event.currentTarget
        .getSVGDocument()
        .querySelector("#backgroundHex")
        .setAttribute("fill", documentStyle.getPropertyValue("--light_color"));
    },
  },
};
</script>

<style scoped>
* {
  margin: 0;
}


.pictograms {
  display: flex;
  justify-content: space-evenly;
  overflow-x: scroll;
  flex: 0 0 auto;
  widows: 100%;
}
.pictograms > div {
  width: 100%;
  flex: 0 0 auto;
}

.pictograms > div > object{
  height: 300px;
}

.buttonwrapper {
  display: flex;
  justify-content: center;
}

.grid-container, section{
  height: 100%;
}

.grid-container{
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  width: 100%;
}

.grid-container > div {
  background-color: rgba(255, 255, 255, 0.8);
  align-self: center;
  min-width: 250px;
 
}

img {
  height: 100%;
  width: 100%;
  /* height: min(30vw, 100%);
    width: 90vw; */
}

object {
  height: 100%;
  width: 100%;
  /* height: min(30vw, 100%);
    width: 50vw; */
}

@media (min-width: 690px) {
  img {
    height: min(30vw, 100%);
    width: min(30vw, 100%);
  }
  .pictograms {
    overflow-x: auto;
  }

  .pictograms > div {
    width: auto;
      flex: 0 1 auto;

  }
}

body {
  font: max(8px, 10vw) "Open Sans", sans-serif;
  color: #5e5b64;
  text-align: left;
}

#login {
  /* margin-top: 200px; */
}

svg {
  fill: #ff0000;
  height: 100%;
}

.backgroundHex {
  fill: #ff0000;
}

section,
footer,
header,
aside,
nav {
  display: block;
}

p {
  font-size: max(12px, min(3vh, 4vw));
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
.resource {
  margin: 20px 0;
}
</style>
