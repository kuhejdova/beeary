<template>
  <form @submit="postSid" class="select-sites">
        <select v-model="selected" @change="postSid">
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
import { baseUrl } from "../variables.js"

export default {
  data() {
    return {
      selected: 1,
      hives: [],
      sites: [],
    };
  },
  methods: {
    postSid() {
      const payload = {
        sid: this.selected,
      };
      const path = baseUrl + "/hives";
      axios
        .post(path, payload)
        .then((res) => {
          this.hives = res.data.hives;
          // this.chartdata = res.data.hives
      console.log("it happend", res.data.hives);
          // this.loaded = true
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
         
        });
        this.$emit('event_child', [this.selected, this.hives]);
        
    },
    // onSubmit(evt) {
    //   evt.preventDefault();
    //   const payload = {
    //     sid: this.selected,
    //   };
    //   // console.log(this.selected)
    //   // console.log(payload)
    //   this.postSid(payload);
      
      
    // },
    getSites() {
      const path = baseUrl + "/sites";
      const payload = {
        "email": localStorage.userEmail,
      }
      axios
        .post(path, payload)
        .then((res) => {
          this.sites = res.data.sites;
          // console.log(res.data.sites)
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  mounted(){
    // this.onSubmit();
    this.postSid();
    this.getSites();
  },
  created() {
    this.postSid();
    this.getSites();
  },
};
</script>
