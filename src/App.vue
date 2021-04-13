<template>
  <div id="app">
    <MenuTop v-show="isVisible()" />
    <router-view />
  </div>
</template>

<script>
import MenuTop from "./components/MenuTop.vue";

export default {
  name: "App",
  components: {
    MenuTop,
  },
  data() {
    return {
      root: null,
      gradientMain: [
        // [129, 172, 255], // #81acff
        [127, 217, 126], // #7fd97e
        [255, 199, 0], // #ffc700
        [255, 174, 99], // #ffae63
        [129, 172, 255], // #81acff
        [127, 217, 126], // #7fd97e
      ],
      gradientLight: [
        // [255, 202, 173], // #ffd4ad
        // [173, 201, 255], // #adc9ff
        [193, 236, 191], // #c0ecbf
        [255, 237, 173], // #ffedad
        [255, 202, 173], // #ffd4ad
        [173, 201, 255], // #adc9ff
        [193, 236, 191], // #c0ecbf
      ],
    };
  },

  methods: {
    isVisible() {
      const sites = ["/", "/login", ""];
      console.log(window.location.href);
      console.log(sites.includes(window.location.pathname));
      return !sites.includes(window.location.pathname);
    },
    getColorSchema(gradient, name) {
      var oneDay = 1000 * 60 * 60 * 24;
      var presentDate = new Date(2021, 11, 21);
      // var presentDate = new Date();
      console.log(presentDate)
      var spring = new Date(presentDate.getFullYear(), 3, 20);
      var summer = new Date(presentDate.getFullYear(), 6, 21);
      var autumn = new Date(presentDate.getFullYear(), 9, 22);
      var winter = new Date(presentDate.getFullYear(), 12, 21);
      
      // var dates = [spring, summer, autumn, winter]
      var resultDays;
      var colorRange;
      var seasonDays;

      if (spring < presentDate  && presentDate <= summer) {
        resultDays = (
          Math.round(summer.getTime() - presentDate.getTime()) / oneDay
        ).toFixed(0);

        seasonDays = (
          Math.round(summer.getTime() - spring.getTime()) / oneDay
        ).toFixed(0);
        colorRange = [gradient[0], gradient[1]];

      } else if (summer < presentDate && presentDate <= autumn) {
        console.log("here")
        resultDays = (
          Math.round(autumn.getTime() - presentDate.getTime()) / oneDay
        ).toFixed(0);
        seasonDays = (
          Math.round(autumn.getTime() - summer.getTime()) / oneDay
        ).toFixed(0);
        colorRange = [gradient[1], gradient[2]];

      } else if (autumn < presentDate && presentDate  <= winter) {
        resultDays = (
          Math.round(winter.getTime() - presentDate.getTime()) / oneDay
        ).toFixed(0);
        seasonDays = (
          Math.round(winter.getTime() - autumn.getTime()) / oneDay
        ).toFixed(0);
        colorRange = [gradient[2], gradient[3]];

      } else {
        spring.setFullYear(spring.getFullYear() + 1);
        resultDays = (
          Math.round(spring.getTime() - presentDate.getTime()) / oneDay
        ).toFixed(0);
        seasonDays = (
          Math.round(spring.getTime() - winter.getTime()) / oneDay
        ).toFixed(0);
        colorRange = [gradient[3], gradient[4]];
      }

      //Get the two closest colors
      var firstcolor = colorRange[0];
      var secondcolor = colorRange[1];

      //Calculate ratio between the two closest colors
      var ratio = resultDays / seasonDays;

      console.log(seasonDays);
      console.log(resultDays);
      console.log(ratio);
      // console.log(secondcolor);
      //Get the color with pickHex(thx, less.js's mix function!)
      var result = this.pickHex(secondcolor, firstcolor, ratio);

      this.root.style.setProperty(name, result);
    },

    pickHex(color1, color2, weight) {
      var p = weight;
      var w = p * 2 - 1;
      var w1 = (w / 1 + 1) / 2;
      var w2 = 1 - w1;
      var rgb = [
        Math.round(color1[0] * w1 + color2[0] * w2),
        Math.round(color1[1] * w1 + color2[1] * w2),
        Math.round(color1[2] * w1 + color2[2] * w2),
      ];

      function componentToHex(c) {
        var hex = c.toString(16);
        return hex.length == 1 ? "0" + hex : hex;
      }

      function rgbToHex(r, g, b) {
        return "#" + componentToHex(r) + componentToHex(g) + componentToHex(b);
      }
      return rgbToHex(rgb[0], rgb[1], rgb[2]);
    },
  },
  mounted() {
    this.root = document.documentElement;
    this.getColorSchema(this.gradientMain, "--main_color");
    this.getColorSchema(this.gradientLight, "--light_color");
  },
};
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
  --main_color: #7fd97e;
  --light_color: #abdfaa;
  --additional_color: #d3f4d3;
}
</style>
