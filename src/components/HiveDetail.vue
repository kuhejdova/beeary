<template>
  <div class="container">
    
    <div class="header-wrapper"><h1>{{ hiveName }}</h1><button class="button" id="back-button" v-on:click="changeUrl()">Zpět</button></div>
    
    <div class="formWrapper">
      <label
        >Od
        <input
          v-model="dateFrom"
          id="form-date-input"
          type="text"
          required
          placeholder="Datum od"
        />
      </label>
      <label
        >Do
        <input
          v-model="dateTo"
          id="form-date-input"
          type="text"
          required
          placeholder="Datum do"
        />
      </label>
      <br />
      <button @click="onSubmit" class="button">Zobrazit</button>
    </div>
    <span id="displayError" ref="displayError"></span>


    <div class="chart">
      <line-chart
        v-if="loaded"
        :title="Teplota"
        :description="descriptionT"
        :chartData="chartData.temperature"
        :onChange="onSubmit"
        :options="options"
      />
      <h3>Upozornění</h3>
      <div class="chart-warnings">
    <div class="warnings" v-for="(warning, index) in chartData.warnings_temperature" :key="index">
        {{ formatDate(warning.date) }} {{'– '}}{{ warning.value }}
    </div>
      </div>
    </div>
    <br />


    <div class="chart">
      <line-chart
        v-if="loaded"
        :title="Hmotnost"
        :description="descriptionH"
        :chartData="chartData.weight"
        :onChange="onSubmit"
        :options="options"
      />
      <h3>Upozornění</h3>
      <div class="chart-warnings">
    <div class="warnings" v-for="(warning, index) in chartData.warnings_weight" :key="index">
        {{ formatDate(warning.date) }} {{'– '}}{{ warning.value }}
    </div>
      </div>
    </div>
    <br />


    <div class="chart">
      <line-chart
        v-if="loaded"
        :title="Vlhkost"
        :description="descriptionV"
        :chartData="chartData.humidity"
        :onChange="onSubmit"
        :options="options"
      />
      <h3>Upozornění</h3>
      <div class="chart-warnings">
    <div class="warnings" v-for="(warning, index) in chartData.warnings" :key="index">
        {{ formatDate(warning.date) }} {{'– '}}{{ warning.value }}
    </div>
      </div>
    </div>
    <br />
    

  </div>
</template>

<script>
import axios from "axios";
import moment from "moment";
import LineChart from "./OnelineChart.vue";
import { baseUrl } from "../variables.js"

export default {
  props: { currentHive: Number },
  components: { LineChart },

  data() {
    return {
      hid: 1,

      hiveName: "",

      loaded: false,
      chartData: null,
      options: null,

      dateFrom: moment(new Date(), "D.M.YYYY")
        .subtract(7, "d")
        .format("D.M.YYYY"),
      dateTo: moment(new Date(), "D.M.YYYY").format("D.M.YYYY"),

      Teplota: "Teplota",
      Vlhkost: "Vlhkost",
      Hmotnost: "Hmotnost",

      descriptionT: "Teplota ve °C",
      descriptionV: "Vlkhost v %",
      descriptionH: "Hmotnost v kg",
    };
  },
  watch: {
    currentHive: function() {
      if (this.$route.query.hid && parseInt(this.$route.query.hid) != 0) {
        this.hid = parseInt(this.$route.query.hid);
        const payload = {
          hid: this.hid,
          dateFrom: this.dateFrom,
          dateTo: this.dateTo,
        };
        // console.log(payload);
        this.postHid(payload);
      }
    },
  },
  methods: {
    postHid(payload) {
      const path = baseUrl + "/hive_graph";
      axios
        .post(path, payload)
        .then((res) => {
          this.hiveName = res.data.graphData[0].name;
          this.chartData = res.data.graphData[0];
          // this.graphData = res.data.graphData[0];
          this.loaded = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },

    formatDate(dateToFormat){
        return moment(dateToFormat, "YYYY-MM-DD").format("D. M. YYYY");
    },

    onSubmit(evt) {
      evt.preventDefault();
      var checkFrom = moment(this.dateFrom, "D.M.YYYY", true);
      var checkTo = moment(this.dateTo, "D.M.YYYY", true);
      if (!checkFrom.isValid() || !checkTo.isValid()) {
        this.$refs.displayError.innerHTML =
          "Zadané datum je ve špatném formátu. Datum zadejte ve formátu D.M.YYYY";
        return;
      }
      if (checkTo.isSameOrBefore(checkFrom)) {
        this.$refs.displayError.innerHTML =
          "Neplatný rozsah dat, datum OD musí být před datum DO";
        return;
      }
      var today = moment(new Date(), "D.M.YYYY");
      if (checkTo.isAfter(today)) {
        this.$refs.displayError.innerHTML =
          "Data jsou dostupná pouze do dnešního dne";
        return;
      }

      this.$refs.displayError.innerHTML = "";
      const payload = {
        hid: this.hid,
        dateFrom: this.dateFrom,
        dateTo: this.dateTo,
      };

      this.postHid(payload);
    },

    changeUrl() {
      this.$router.push({
        path: "/hives",
        query: { hid: 0 },
      });
    },
  },
  mounted() {
    if (this.$route.query.hid && parseInt(this.$route.query.hid) != 0) {
      this.hid = parseInt(this.$route.query.hid);
      const payload = {
        hid: this.hid,
        dateFrom: this.dateFrom,
        dateTo: this.dateTo,
      };
      this.postHid(payload);
    }
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

.chart, .warnings {
  background: #f4f4f4;
  /* padding: 10px auto; */
  height: auto;
  margin-bottom: 10px;
}
h3 {
  margin-left: 10px;
}

.chart-warnings {
  max-height: 200px;
  overflow-y: auto;
  margin-left: 10px;
}

.formWrapper {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
}

@media (max-width: 570px) {
  .formWrapper{
    flex-direction: column;
  }
}

#displayError {
  color: red;
}

.header-wrapper {
  margin: 10px auto;
  background: #f4f4f4;
  padding: 10px;
  /* height: auto; */
  display: flex;
  justify-content: space-between ;
}

#back-button {
  margin: auto 0px auto 0px;
}

/* #line-chart {
  padding: 20px;
} */
</style>
