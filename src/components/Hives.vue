<template>
  <div class="container">
    <br /><br />
    <SelectSite v-on:event_child="onChangeSite" />
    <br /><br />
    <div class="wrapper">
      <div id="inner" v-if="hives.length === 0">
        Žádné úly ke zobrazení, přidejte k tomuto stanovišti úl v nastavení.
      </div>
      <div class="outter" v-for="(hive, index) in hives" :key="index">
        <div id="inner">
          <h3>{{ hive.name }}</h3>
          <div class="chart-wrapper">
            <line-chart
              v-if="loaded"
              :chartdata="hive.humidity"
              :chartdata2="hive.temperature"
              :chartdata3="hive.weight"
              :onChange="onChangeSite"
              :options="options"
            />
          </div>
          <br />
          <button class="button" @click="changeUrl(hive.id)">Detail</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import LineChart from "./MultilineChart.vue";
import SelectSite from "./selectSite.vue";

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
  methods: {
    changeUrl(selectedHid) {
      this.hid = selectedHid;
      this.$router.push({
        path: "/hives",
        query: { hid: this.hid },
      });
      this.$emit("event_child", selectedHid);
    },
    onChangeSite(childSite) {
      this.selected = childSite[0];
      this.hives = childSite[1];
      this.chartdata = childSite[1];
      this.loaded = true;
    },
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
</style>
