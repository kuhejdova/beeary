<template>
  <div class="container">
    <br /><br />
    <!-- <line-chart
            v-if="loaded"
            :chartdata="hive.graph"
            :chartdata2="hive.temperature"
            :onChange="onSubmit"
            :options="options"/>
          <br>
          <line-chart
            v-if="loaded"
            :chartdata="hive.graph"
            :chartdata2="hive.temperature"
            :onChange="onSubmit"
            :options="options"/>
          <br>
          <line-chart
            v-if="loaded"
            :chartdata="hive.graph"
            :chartdata2="hive.temperature"
            :onChange="onSubmit"
            :options="options"/>
          <br>
          <line-chart
            v-if="loaded"
            :chartdata="hive.graph"
            :chartdata2="hive.temperature"
            :onChange="onSubmit"
            :options="options"/>
          <br> -->
    <button class="button" v-on:click="changeUrl()" >Zpět</button>
    <!-- </div>  -->

    <!-- </div> -->
    <!-- </div> -->
  </div>
</template>

<script>
// import axios from "axios";
// import LineChart from './Chart.vue'

export default {
  props: { currentHive: Number },
  // components: { LineChart },
  data() {
    return {
      hid: 1,

      loaded: false,
      chartdata: null,
      options: null,
    };
  },
  
  methods: {
    getHiveData() {},

    changeUrl() {

      this.$router.push({
        path: "/hives",
        query: { hid: 0 },
      });
      
    },
  },
  created() {},
};
</script>

<style scoped>
#inner {
  background: #f4f4f4;
  padding: 20px;
}

.wrapper {
  display: grid;
  grid-template-columns: 50% 50%;
  column-gap: 10px;
  row-gap: 10px;

  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
}
</style>
