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
          {{ hive.graph }}
          <line-chart
            v-if="loaded"
            :chartdata="chartdata"
            :options="options"/>
          <br>
          <button  class="button">Detail</button>
        </div>
        
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import LineChart from './Chart.vue'

export default {
  components: { LineChart },
  data() {
    return {
      selected: 1,
      hives: [],
      sites: [],
      loaded: false,
      chartdata: null,
      options: null,
    };
  },
  // async mounted () {
  //   this.loaded = false
  //   try {
  //     const { userlist } = await fetch('/api/userlist')
  //     this.chartdata = userlist
  //     this.loaded = true
  //   } catch (e) {
  //     console.error(e)
  //   }
  // },
  methods: {
    postSid(payload) {
      const path = "http://localhost:5000/hives";
      axios
        .post(path, payload)
        .then((res) => {
          this.hives = res.data.hives;
          this.chartdata = res.data.hives.graph
          this.loaded = true
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getHives();
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
      this.getHives();
    },
    getSites() {
      const path = "http://localhost:5000/sites";
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
  created() {
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

  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
}
</style>
