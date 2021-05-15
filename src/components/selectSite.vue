<template>
  <form @submit="postSid" class="select-sites">
    <select @change="postSid">
      <option
        v-for="(site, index) in sites"
        :key="index"
        v-bind:value="site.id"
      >
        {{ site.name }}
      </option>
    </select>
  </form>
</template>

<script>
import axios from "axios";
import { baseUrl } from "../variables.js";

const CancelToken = axios.CancelToken;
const source = CancelToken.source();

export default {
  data() {
    return {
      selected: 1,
      hives: [],
      sites: [],
    };
  },
  methods: {
    postSid(event) {
      if (typeof event !== "undefined") {
        this.selected = event.currentTarget.value;
      }
      const payload = {
        sid: this.selected,
      };
      const path = baseUrl + "/hives";
      axios
        .post(path, payload, {
          cancelToken: source.token,
        })
        .then((res) => {
          this.hives = res.data.hives;
          this.$emit("event_child", [this.selected, this.hives]);
        })
        .catch((error) => {
          if (axios.isCancel(error)) {
            console.log("Request canceled", error.message);
          } else {
            console.error(error);
          }
        });
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
          this.selected = this.sites[0].id;
          this.postSid();
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  mounted() {
    this.getSites();
  },
  created() {
    this.getSites();
  },
};
</script>
