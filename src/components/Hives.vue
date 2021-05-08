<template>
  <div class="container">
    <br /><br />
    <!-- <form @submit="onSubmit" class="select-sites">
        <select v-model="selected" @change="onSubmit">
          <option
            v-for="(site, index) in sites"
            :key="index"
            v-bind:value="site.id"
          >
            {{ site.name }}
          </option>
        </select>
    </form> -->
  <SelectSite v-on:event_child="onChangeSite" />
    <br /><br />
    <div class="wrapper">
      <div class="outter" v-for="(hive, index) in hives" :key="index">
        <div id="inner">
          <h3>{{ hive.name }} </h3> 
          <div class="chart-wrapper">
          <line-chart
            v-if="loaded"
            :chartdata="hive.humidity"
            :chartdata2="hive.temperature"
            :chartdata3="hive.weight"
            :onChange="onChangeSite"
            :options="options"/>
          </div>
          <br>
          <button class="button" @click="changeUrl(hive.id)">Detail</button>
        </div>
        
      </div>
    </div>
  </div>
</template>

<script>
// import axios from "axios";
import LineChart from './MultilineChart.vue'
// import { baseUrl } from "../variables.js"
// import SelectSite from "../selectSite.vue"
import SelectSite from './selectSite.vue';

export default {
  components: { LineChart, SelectSite },
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
  watch: {
    onChangeSite: function(){
      console.log('magic')
    }
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
    onChangeSite(childSite){
      this.selected = childSite[0];
      this.hives = childSite[1];
      this.chartdata = childSite[1];
      this.loaded = true;
      console.log("childsite", childSite);
      console.log("chartdata in parent", this.chartdata);
    },


    // postSid(payload) {
    //   const path = baseUrl + "/hives";
    //   axios
    //     .post(path, payload)
    //     .then((res) => {
    //       this.hives = res.data.hives;
    //       this.chartdata = res.data.hives
      
    //       this.loaded = true
    //     })
    //     .catch((error) => {
    //       // eslint-disable-next-line
    //       console.error(error);
         
    //     });
    // },
    // onSubmit(evt) {
    //   evt.preventDefault();
    //   const payload = {
    //     sid: this.selected,
    //   };
    //   // console.log(this.selected)
    //   // console.log(payload)
    //   this.postSid(payload);
      
    // },
    // getSites() {
    //   const path = baseUrl + "/sites";
    //   const payload = {
    //     "email": localStorage.userEmail,
    //   }
    //   axios
    //     .post(path, payload)
    //     .then((res) => {
    //       this.sites = res.data.sites;
    //       console.log(res.data.sites)
    //     })
    //     .catch((error) => {
    //       // eslint-disable-next-line
    //       console.error(error);
    //     });
    // },
  },
  mounted() {
    // this.onChangeSite;
    // this.postSid();
    // this.getSites();
  },
};
</script>

<style scoped>
#inner {
  background: #f4f4f4;
  padding: 20px;
}

.container {
  width: 100%;
}

/* .wrapper {
  display: grid;
  grid-template-columns: 50% 50%;
  column-gap: 10px;
  row-gap: 10px;
  height: 50vh;

  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
} */

.outter {
  width: 100%;
}
@media (min-width: 1000px) {
  .wrapper {
  display: grid;
  grid-template-columns: repeat(2, 50%);
  column-gap: 10px;
  row-gap: 10px;

  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
}
}

.select-sites {
  margin: auto 10px;
}

.chart-wrapper {
  width: 100%;
}

/* @media (max-width: 1000px) {
  
} */

</style>
