<template>
  <section>
    <div class="grid-container">
      <div class="logo">
        <img src="../../public/images/logo_text.svg" alt="Beeary" />
      </div>

      <div class="logo-subtitle">
        <p>Webová aplikace pro všechny včelaře. Ovládněte včelařství.</p>
      </div>

      <div class="pictogram1">
        <object id="svgSetColor" type="image/svg+xml" :data="svgHives">
          <img src="../../public/images/hives.svg" alt="Beeary" />
        </object>
      </div>
      <div class="pictogram2">
        <object id="svgSetColor" type="image/svg+xml" :data="svgTimeline">
          <img src="../../public/images/timeline.svg" alt="Beeary" />
        </object>
        <!-- <img src="../../public/images/timeline.svg" alt="Beeary" /> -->
      </div>
      <div class="pictogram3">
        <object id="svgSetColor" type="image/svg+xml" :data="svgMonitoring">
          <img src="../../public/images/monitoring.svg" alt="Beeary" />
        </object>
        <!-- <img src="../../public/images/monitoring.svg" alt="Beeary" /> -->
      </div>

      <div class="description1">
        <p>Přehled všech úlů</p>
      </div>
      <div class="description2">
        <p>Časová osa s poznámkami</p>
      </div>
      <div class="description3">
        <p>Celoroční monitoring</p>
      </div>

      <div class="button">
        <button @click="redirectHome" class="button">Pojď začít</button>
      </div>
    </div>
  </section>
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
    setPictogramsColor() {
      var documentStyle = getComputedStyle(document.body);
      var all = document.querySelectorAll("[id=svgSetColor]");

      all.forEach((element) => {
        element
          .getSVGDocument()
          .querySelector("#backgroundHex")
          .setAttribute(
            "fill",
            documentStyle.getPropertyValue("--light_color")
          );
      });
    },
  },
  // mounted() {
  //   this.setPictogramsColor();
  // },
  // created() {
  //   this.setPictogramsColor();
  // },
  ready() {
    this.setPictogramsColor();
  },
};
</script>

<style scoped>
* {
  margin: 0;
}

.logo {
  grid-area: logo;
  height: 100%;
}
.logo-subtitle {
  grid-area: logo-subtitle;
  height: 100%;
}
.pictogram1 {
  grid-area: pictogram1;
  height: 100%;
}
.pictogram2 {
  grid-area: pictogram2;
  height: 100%;
}
.pictogram3 {
  grid-area: pictogram3;
  height: 100%;
}
.description1 {
  grid-area: description1;
  height: 100%;
}
.description2 {
  grid-area: description2;
  height: 100%;
}
.description3 {
  grid-area: description3;
  height: 100%;
}
.button {
  grid-area: button;
  height: 100%;
}

@media (min-width: 0px) {
  .grid-container {
    display: grid;
    grid-template-areas:
      "logo"
      "logo-subtitle"
      "pictogram1"
      "description1"
      "button";
    grid-template-rows: 30% 10% 40% 6% 10%;
    /* grid-gap: 20px; */
    justify-items: center;
    align-items: center;

    height: calc(100vh - 100px);
    padding-right: 5%;
    padding-left: 5%;
    /* padding-bottom: 3%; */
    min-height: 620px;
    min-width: 250px;
  }
  .grid-container > div {
    background-color: rgba(255, 255, 255, 0.8);
    width: 90vw;
    align-self: center;
    min-width: 250px;
  }

  .pictogram2 {
    grid-area: pictogram2;
    display: none;
  }
  .pictogram3 {
    grid-area: pictogram3;
    display: none;
  }

  .description2 {
    grid-area: description2;
    display: none;
  }
  .description3 {
    grid-area: description3;
    display: none;
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
}

@media (min-width: 690px) {
  .grid-container {
    display: grid;
    grid-template-areas:
      "logo logo logo"
      "logo-subtitle logo-subtitle logo-subtitle"
      "pictogram1 pictogram2 pictogram3"
      "description1 description2 description3"
      "button button button";
    grid-template-rows: 30% 10% 35% 6% 10%;
    grid-gap: 20px;
    justify-items: center;
    align-items: center;

    height: calc(100vh - 100px);
    padding-right: 5%;
    padding-left: 5%;
    /* padding-bottom: 3%; */
    min-height: 620px;
  }
  .grid-container > div {
    background-color: rgba(255, 255, 255, 0.8);
    width: auto;
    align-self: center;
  }

  .pictogram2 {
    grid-area: pictogram2;
    display: unset;
  }
  .pictogram3 {
    grid-area: pictogram3;
    display: unset;
  }

  .description2 {
    grid-area: description2;
    display: unset;
  }
  .description3 {
    grid-area: description3;
    display: unset;
  }
  img {
    height: min(30vw, 100%);
    width: min(30vw, 100%);
  }

  object {
    height: min(30vw, 100%);
    width: min(30vw, 100%);
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
