<template>
  <div class="container">
    <div class="wrapper">
      <div v-for="(site, index) in sites" :key="index">
        <div id="inner">
          {{ site.name }} <br />
          - {{ site.location }} <br /><br />
          {{ site.event }}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      sites: [],
    };
  },
  methods: {
    getSites() {
      const path = "http://localhost:5000/sites";
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
  grid-template-columns: 25% 25%;
  column-gap: 10px;
  row-gap: 10px;

  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
}
</style>
