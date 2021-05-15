<template>
  <div class="container">
    <div class="wrapper">
      <div class="outter" v-for="(site, index) in sites" :key="index">
        <div id="inner">
          <h2>{{ site.name }}</h2>
          Lokalita: {{ site.location }}
          <h3>Upozornění ze senzorů</h3>
          <div class="warnings" v-if="site.have_hive != 0">
            <div v-if="chartData.warnings.length === 0">
              Žádné nové upozornění.
            </div>
            <div v-for="(warning, index) in chartData.warnings" :key="index">
              {{ chartData.name }} {{ "– " }} {{ formatDate(warning.date) }}
              {{ "– " }}{{ warning.value }}
            </div>
          </div>
          <div class="warnings" v-else>
            Žádný úl se senzory.
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import moment from "moment";
import { baseUrl } from "../variables.js";

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
    formatDate(dateToFormat) {
      return moment(dateToFormat, "YYYY-MM-DD").format("D. M. YYYY");
    },

    getSites() {
      const path = baseUrl + "/sites";
      const payload = {
        email: localStorage.userEmail,
      };
      axios
        .post(path, payload)
        .then((res) => {
          this.sites = res.data.sites;
        })
        .catch((error) => {
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
  padding: 10px 20px;
}

h2 {
  margin: 0px;
}

h3 {
  margin-bottom: 0px;
}

.wrapper {
  display: grid;
  grid-template-columns: repeat(2, 50%);
  column-gap: 10px;
  row-gap: 10px;

  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
}

@media (max-width: 950px) {
  .wrapper {
    grid-template-columns: unset;
  }
}

@media (max-width: 800px) {
  .wrapper {
    grid-template-columns: unset;
  }
}

.warnings {
  max-height: 200px;
  overflow-y: auto;
}
</style>
