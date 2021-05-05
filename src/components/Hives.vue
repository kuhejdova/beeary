<template>
  <div class="container">
    <br /><br />
    <form @submit="onSubmit" class="w-100">
      <div id="v-model-select-dynamic" class="demo">
        <select v-model="selected" @change="onSubmit">
          <option
            v-for="(site, index) in sites"
            :key="index"
            v-bind:value="site.id"
          >
            {{ site.name }}
          </option>
        </select>
        <!-- <div>{{ selected }}</div> -->
      </div>
    </form>
    <br /><br />
    <div class="wrapper">
      <div v-for="(hive, index) in hives" :key="index">
        <div id="inner">
          {{ hive.name }} <br />
          <br /><br />
          <line-chart
            v-if="loaded"
            :chartdata="hive.humidity"
            :chartdata2="hive.temperature"
            :chartdata3="hive.weight"
            :onChange="onSubmit"
            :options="options"/>
          <br>
          <button class="button" @click="changeUrl(hive.id)">Detail</button>
        </div>
        
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import LineChart from './MultilineChart.vue'
import { baseUrl } from "../variables.js"

export default {
  components: { LineChart },
  data() {
    return {
       hid: 1,
      selected: 1,
      hives: [],
      sites: [],
      loaded: false,
      chartdata: null,
      options: null,
    };
  },
  methods: {
changeUrl(selectedHid) {
      this.hid = selectedHid;
      // console.log(selectedHid);
      this.$router.push({
        path: "/hives",
        query: { hid: this.hid },
      });
      this.$emit('event_child', selectedHid);
    },


    postSid(payload) {
      const path = baseUrl + "/hives";
      axios
        .post(path, payload)
        .then((res) => {
          this.hives = res.data.hives;
          this.chartdata = res.data.hives
      
          this.loaded = true
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
         
        });
    },
    onSubmit(evt) {
      evt.preventDefault();
      const payload = {
        sid: this.selected,
      };
      // console.log(this.selected)
      // console.log(payload)
      this.postSid(payload);
      
    },
    getSites() {
      const path = baseUrl + "/sites";
      axios
        .get(path)
        .then((res) => {
          this.sites = res.data.sites;
          this.selected = res.data.sites[0].id;
          //   console.log(res.data.sites[0])
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  mounted() {
    this.postSid();
    this.getSites();
  },
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
  height: 50vh;

  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
}

</style>
