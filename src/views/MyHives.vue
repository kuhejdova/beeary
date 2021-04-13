<template>
  <div>

    <main>
      <section>
        <div class="wrapper">
          <div class="left">
            <Hives />
          </div>
          <div class="right">
            <Hexagons />
          </div>
        </div>
      </section>
    </main>
  </div>
</template>

<script>

import Hives from "../components/Hives.vue";
import Hexagons from "../components/Hexagons.vue";

export default {
  components: {

    Hives,
    Hexagons,
  },
};
</script>

<style scoped>
* {
  margin: 0;

  padding: 0;
}

section {
  margin-left: 20px;
}

div {
  /* font:15px/1.3 'Open Sans', sans-serif; */
  font-weight: bold;
  color: #5e5b64;
  text-align: left;
}

.wrapper{
  display: grid;
  grid-template-columns: 70% 27%;
  column-gap: 40px;
  row-gap: 10px;

  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
}

/* .right {
  margin-top: -40px;
} */

.left {
  padding-left: 20px;
}

</style>
