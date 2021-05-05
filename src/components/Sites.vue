<template>
  <div class="container">
    <div class="wrapper">
      <div v-for="(site, index) in sites" :key="index">
        <div id="inner">
          {{ site.name }} <br />
          - {{ site.location }} <br /><br />
          <div v-for="(warning, index) in chartData.warnings" :key="index">
        {{chartData.name}} {{'– '}} {{ formatDate(warning.date) }} {{'– '}}{{ warning.value }}
    </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import moment from "moment";
import { baseUrl } from "../variables.js"

export default {
  data() {
    return {
      sites: [],
      chartData: [],
       dateFrom: moment(new Date(), "D.M.YYYY")
        .subtract(7, "d")
        .format("D.M.YYYY"),
      dateTo: moment(new Date(), "D.M.YYYY").format("D.M.YYYY"),
    };
  },
  methods: {
    getHiveData() {
      const payload = {
          hid: 1,
          dateFrom: this.dateFrom,
          dateTo: this.dateTo,
        };
      const path = baseUrl + "/hive_graph";
      axios
        .post(path, payload)
        .then((res) => {
          this.chartData = res.data.graphData[0];
        })
        .catch((error) => {
          console.error(error);
        });
    },
    formatDate(dateToFormat){
        return moment(dateToFormat, "YYYY-MM-DD").format("D. M. YYYY");
    },


    getSites() {
      const path = baseUrl + "/sites";
      axios
        .get(path)
        .then((res) => {
          this.sites = res.data.sites;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getSites();
    this.getHiveData();
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
