<template>
  <div class="landing-wrapper">
    <div class="container">
      <div>
        <div class="logo-wrapper">
          <img
            src="../../public/images/logo_text.svg"
            alt="Beeary"
            class="logo"
          />
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
    </div>
  </div>
</template>

<script>
// import { auth } from "../firebase";
import store from "@/store";

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
      if (!store.getters.isAuthenticated) {
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
/* * {
  margin: 0;
} */

.landing-wrapper {
  height: calc(100% + 60px);
  background-image: url(../../public/images/background_pattern_missing.svg);
  background-size: cover;
  background-repeat: space;
  background-position: center;
}

.pictograms {
  display: flex;
  justify-content: space-between;
  overflow-x: scroll;
  flex: 0 0 auto;
  widows: 100%;
}
.pictograms > div {
  width: 100%;
  flex: 0 0 auto;
}

/* Hide scrollbar for Chrome, Safari and Opera */
.pictograms::-webkit-scrollbar {
  display: none;
}

/* Hide scrollbar for IE, Edge and Firefox */
.pictograms {
  -ms-overflow-style: none; /* IE and Edge */
  scrollbar-width: none; /* Firefox */
}

.pictograms > div > object {
  height: 200px;
}

.buttonwrapper {
  display: flex;
  justify-content: center;
  margin-bottom: 10px;
}

/* .container,
section {
} */

.container {
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
  /* justify-content: flex-start; */
  height: 100%;
  position: relative;
  left: 0px;
  right: 0px;
  margin: auto;
  top: 0px;
  bottom: 0px;
  height: 100%;
  /* background-image: url(../../public/images/background_pattern_missing.svg) ;
  background-size: cover;
  background-repeat: space;
  background-position: center; */
  /* margin-bottom: 10px; */
}

.container > div > div {
  /* background-color: rgba(255, 255, 255, 0.8); */
  align-self: center;
  min-width: 250px;
}
.container > div > div:not(:first-child) {
  margin-top: 10px;
}

.logo {
  height: 125px;
  width: 250px;
  /* margin-top: 0px; */
  /* height: min(30vw, 100%);
    width: 90vw; */
}

#svgSetColor {
  height: 30vh;
}

object {
  height: 100%;
  width: 100%;
  /* height: min(30vw, 100%);
    width: 50vw; */
}

body {
  font: max(8px, 10vw) "Open Sans", sans-serif;
  color: #5e5b64;
  text-align: left;
}

/* #login {
  margin-top: 200px; 
} */

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
  font-size: 20px;
  font-weight: bold;
  color: #7d9098;
}

@media (min-width: 690px) {
  .container {
    width: 80%;
  }
  /* img {
    height: 100%;
    width: 70%;
    /* height: min(30vw, 100%);
    width: min(30vw, 100%); 
  } */
  .pictograms {
    width: 100%;
    overflow-x: auto;
    justify-content: space-evenly;
  }

  .pictograms > div {
    width: auto;
    flex: 0 1 auto;
  }
  .pictograms > div > object {
    height: 300px;
  }

  .logo {
    min-height: 200px;
    min-width: 400px;
    height: 20vh;
    width: 25vw;
    /* height: min(30vw, 100%);
    width: 90vw; */
  }

  p {
    font-size: 1.8em;
  }
}
</style>
