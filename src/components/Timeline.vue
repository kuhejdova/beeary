<template>
  <section>
    <div class="container">
      <div class="grid" v-for="(hex, index) in hexagons" :key="index" >
        <div class='block' :style="{visibility: randomShow() ? 'visible' : 'hidden'}"></div>
        <div class='block'></div>
        <div class='block'></div>
        <div class='block' :style="{visibility: randomShow() ? 'visible' : 'hidden'}"></div>
        <div class='block' ></div>
        <div v-bind:class="isActive(hex) ? 'block-highlight' : 'block'">{{ hex.date}}</div>
        <div class='block' ></div>
      </div>
    </div>
  </section>
</template>

<script>
import moment from "moment";

export default {
  data() {
    return {
      hexagons: [],
      active: false,
      show: true,
    };
  },
  methods: {
    randomShow(){
      var min = 2;
      var max = 4;
      var rand = Math.floor(Math.random() * (max - min + 1)) + min;
      if (rand === 3){
        return false;
      }
      else{
        return true;
      }
    },

    fillHexagons() {
      var startyear = 2017;
      var startmonth = 1;
      for (var i = 0; i < 100; i++) {
        var monthyear = startmonth + "/" + startyear;
        this.hexagons.push({ id: i, date: monthyear });
        if (startmonth == 12){
          startmonth = 1;
          startyear++;
        } else {
          startmonth++;
        }
      }
    },
    isActive(hex){
      moment.locale("cs");
      var now_date = moment(new Date()).format("M/YYYY").toString();
      
      if (hex.date.toString() == now_date){
        this.active = true;
      } else {
        this.active = false;
      }
      return this.active;
    },
    scrollToElement() {
    const el = document.getElementsByClassName('block-highlight')[0];

    if (el) {
      // Use el.scrollIntoView() to instantly scroll to the element
      el.scrollIntoView({behavior: 'smooth'});
    }
  },
  },
  created() {
    this.fillHexagons();
    this.scrollToElement();
  },
  mounted() {
  this.scrollToElement();
},
};
</script>

<style scoped>
.container {
  width: 400px;
  margin-top: 10px;
  height: 88vh;
  overflow: auto;
}

 /* Hide scrollbar for Chrome, Safari and Opera */
.container::-webkit-scrollbar {
  display: none;
}

/* Hide scrollbar for IE, Edge and Firefox */
.container {
  -ms-overflow-style: none;  /* IE and Edge */
  scrollbar-width: none;  /* Firefox */
} 

body {
  background-color: var(--main_color) 24;
}

.grid {
  display: grid;
  width: auto;
  justify-content: center;
  grid-auto-flow: dense;
  grid-template-columns: repeat(auto-fit, 50px);
  grid-template-rows: repeat(auto-fit, minmax(78px, 78px));
  grid-auto-rows: 78px;
  /* margin-bottom: 42px; */
}
.grid > * {
  -webkit-clip-path: polygon(50% 0, 95% 25%, 95% 75%, 50% 100%, 5% 75%, 5% 25%);
  clip-path: polygon(50% 0, 95% 25%, 95% 75%, 50% 100%, 5% 75%, 5% 25%);
}
.block {
  position: relative;
  height: 95px;
  background-color: var(--light_color);
  grid-column: 2 span;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 20px;
  box-shadow: inset 0 0 70px 35px var(--main_color) 73;
  transition: clip-path 300ms, background-color 300ms;
}
.block:hover {
  background-color: var(--main_color);
}

.block-highlight {
  position: relative;
  height: 95px;
  background-color: var(--main_color);
  grid-column: 2 span;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 20px;
  box-shadow: inset 0 0 70px 35px var(--main_color) 73;
  transition: clip-path 300ms, background-color 300ms;
}

@media screen {
  /* .block:nth-child(4),
  .block:nth-child(5n + 9) {
    grid-column: 2 / span 2;
  } */
  .block:nth-child(5), 
  .block:nth-child(7n + 12) {
    grid-column: 2 / span 2;
    }
}
</style>
