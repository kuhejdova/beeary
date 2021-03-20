<template>
  <section>
    <!-- <MenuTop /> -->
    <div class="container">
      <div class="grid">
        <div v-for="(hex, index) in hexagons" :key="index" class="block">{{ hex.id }}</div>
      </div>
    </div>
  </section>
</template>

<script>
// import MenuTop from "../components/MenuTop.vue";

export default {
  data() {
    return {
      hexagons: [],
    };
  },
//   components: {
//     MenuTop,
//   },
  methods: {
    fillHexagons() {
      for (var i = 0; i < 30; i++) {
        this.hexagons.push({ id: i });
      }
      console.log(this.hexagons);
    },
  },
  created() {
    this.fillHexagons();
  },
};
</script>

<style scoped>
.container {
  width: 450px;
  margin-top: 10px;
  height: 88vh;
  overflow: auto;
}

body {
  background-color: var(--main_color) 24;
}
/* body::-webkit-scrollbar {
  width: 13px;
  background: var(--main_color) 24;
} */
/* body::-webkit-scrollbar-thumb {
  background-color: gold;
  border-radius: 10px;
  box-shadow: inset 0 0 100px 50px #ff9a00;
} */
.grid {
  display: grid;
  width: auto;
  justify-content: center;
  grid-auto-flow: dense;
  grid-template-columns: repeat(auto-fit, 70px);
  grid-template-rows: repeat(auto-fit, minmax(112px, 112px));
  grid-auto-rows: 112px;
  margin-bottom: 42px;
}
.grid > * {
  -webkit-clip-path: polygon(50% 0, 95% 25%, 95% 75%, 50% 100%, 5% 75%, 5% 25%);
  clip-path: polygon(50% 0, 95% 25%, 95% 75%, 50% 100%, 5% 75%, 5% 25%);
}
.block {
  position: relative;
  height: 140px;
  background-color: var(--main_color);
  grid-column: 2 span;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  font-style: italic;
  font-size: 35px;
  box-shadow: inset 0 0 70px 35px #ff9a00 73;
  transition: clip-path 300ms, background-color 300ms;
}
.block:hover {
  background-color: var(--light_color);
}

@media screen {
  .block:nth-child(4),
  .block:nth-child(5n + 9) {
    grid-column: 2 / span 2;
  }
}
</style>
