<template>
  <section>
    <div class="container">
      <div class="grid">
        <div v-for="(hex, index) in hexagons" :key="index" class="block">
          <img
            v-if="index % 5 == 0"
            src="../../public/images/hives.svg"
            alt="Beeary"
          />
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  data() {
    return {
      hexagons: [],
    };
  },
  methods: {
    fillHexagons() {
      for (var i = 0; i < 150; i++) {
        this.hexagons.push({ id: i });
      }
    },
  },
  created() {
    this.fillHexagons();
  },
};
</script>

<style scoped>
.container {
  width: 400px;
  margin-top: 10px;
  height: 88vh;
  overflow: hidden;
}

/* Hide scrollbar for Chrome, Safari and Opera */
.container::-webkit-scrollbar {
  display: none;
}

/* Hide scrollbar for IE, Edge and Firefox */
.container {
  -ms-overflow-style: none; /* IE and Edge */
  scrollbar-width: none; /* Firefox */
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

@media screen {
  .block:nth-child(5),
  .block:nth-child(7n + 12) {
    grid-column: 2 / span 2;
  }
}

img {
  height: 100%;
}
</style>
