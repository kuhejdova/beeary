<template>
  <select v-model="selected" @change="onSubmit">
    <option v-for="(site, index) in sites" :key="index" v-bind:value="site.id">
      {{ site.name }}
    </option>
  </select>
</template>

<script>
import axios from "axios";
import { baseUrl } from "../variables.js"

export default {
  props: { selectedDate: String },
  data() {
    return {
      loaded: false,
      selected: 1,
      selectedHive: 1,
      hives: [],
      sites: [],
    };
  },
  watch: {
    selectedDate: function() {
      this.showActivities();
    },
  },
  methods: {
    postSid(payload) {
      const path = baseUrl + "/hives";
      axios
        .post(path, payload)
        .then((res) => {
          this.hives = res.data.hives;
          this.chartdata = res.data.hives;

          this.loaded = true;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    onSubmit(evt) {
      evt.preventDefault();
      const payload = {
        sid: this.selected,
      };
      this.postSid(payload);
    },
  },
  created() {
    this.postSid();
    // this.getSites();
  },
};
</script>
