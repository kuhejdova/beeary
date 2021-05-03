<template>
  <div class="container">
    <br /><br />
    <button class="button" v-on:click="changeUrl()">Zpět</button>
    <br /><br />
    <h1>{{ hiveName }}</h1>
    <div class="formWrapper">
      <label>Od
    <input
      v-model="dateFrom"
      id="form-date-input"
      type="text"
      required
      placeholder="Datum od"
    />
      </label>
      <label>Do
    <input
      v-model="dateTo"
      id="form-date-input"
      type="text"
      required
      placeholder="Datum do"
    />
      </label>
    <br /><br />
    <button @click="onSubmit" class="button">Zobrazit</button>
    </div>
    <br />
    <span id='displayError' ref="displayError"></span>
    <br /><br />
    <div class="chart">
      <line-chart
        v-if="loaded"
        :title="Teplota"
        :chartData="graphData.temperature"
        :onChange="onSubmit"
        :options="options"
      />
    </div>
    <br />
    <div class="chart">
      <line-chart
        v-if="loaded"
        :title="Hmotnost"
        :chartData="graphData.weight"
        :onChange="onSubmit"
        :options="options"
      />
    </div>
    <br />
    <div class="chart">
      <line-chart
        v-if="loaded"
        :title="Vlhkost"
        :chartData="graphData.humidity"
        :onChange="onSubmit"
        :options="options"
      />
    </div>
    <br />
    
  </div>
</template>

<script>
import axios from "axios";
import moment from "moment";
import LineChart from "./OnelineChart.vue";

export default {
  props: { currentHive: Number },
  components: { LineChart },

  data() {
    return {
      hid: 1,

      graphData: null,
      hiveName: "",

      loaded: false,
      chartData: null,
      options: null,

      dateFrom: moment(new Date(), "D.M.YYYY").subtract(7,'d').format("D.M.YYYY"),
      dateTo: moment(new Date(), "D.M.YYYY").format("D.M.YYYY"),
      

      Teplota: "Teplota",
      Vlhkost: "Vlhkost",
      Hmotnost: "Hmotnost",
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
        console.log(payload);
        this.postHid(payload);
      }
    },
  },
  methods: {

    postHid(payload) {
      const path = "http://localhost:5000/hive_graph";
      axios
        .post(path, payload)
        .then((res) => {
          this.hiveName = res.data.graphData[0].name;
          this.chartData = res.data.graphData[0];
          this.graphData = res.data.graphData[0];
          this.loaded = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    onSubmit(evt) {
      evt.preventDefault();
      var checkFrom = moment(this.dateFrom, "D.M.YYYY", true);
      var checkTo = moment(this.dateTo, "D.M.YYYY", true);
      if (!checkFrom.isValid() || !checkTo.isValid())
      {
        // console.error("wrong format");
        // alert("Zadané datum je ve špatném formátu. Datum zadejte ve formátu D.M.YYYY")
        this.$refs.displayError.innerHTML = "Zadané datum je ve špatném formátu. Datum zadejte ve formátu D.M.YYYY"
        return;
      }
      // console.log(checkFrom)
      // console.log(checkTo)
      if (checkTo.isSameOrBefore(checkFrom)){ 
        this.$refs.displayError.innerHTML = "Neplatný rozsah dat, datum OD musí být před datum DO"
        return;
      }
      var today = moment(new Date(), "D.M.YYYY");
      if (checkTo.isAfter(today)){
        this.$refs.displayError.innerHTML = "Data jsou dostupná pouze do dnešního dne"
        return;
      }

this.$refs.displayError.innerHTML = ''
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
      // console.log(payload);
      this.postHid(payload);
    }
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

.chart {
  background: #f4f4f4;
  padding: 10px;
  height: auto;
}

.formWrapper {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
}

#displayError {
  color: red;
}
</style>
