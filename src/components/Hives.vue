<template>
  <div class="container">
    <br /><br />
    <form @submit="onSubmit" class="w-100">
      <div id="v-model-select-dynamic" class="demo">
        <select v-model="selected" @change="onSubmit">
          <option
            v-for="(site, index) in sites"
            :key="index"
            v-bind:value="site.id"
          >
            {{ site.name }}
          </option>
        </select>
        <!-- <div>{{ selected }}</div> -->
      </div>
    </form>
    <br /><br />
    <div class="rowaa">
      <table>
        <tbody>
          <tr v-for="(hive, index) in hives" :key="index">
            <td>
              <div id="inner">
                {{ hive.name }} <br />
                <br /><br />
                {{ hive.graph }}
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      selected: 1,
      hives: [],
      sites: [],
    };
  },
  methods: {
    postSid(payload) {
      const path = "http://localhost:5000/hives";
      axios
        .post(path, payload)
        .then((res) => {
          this.hives = res.data.hives;
          console.log(this.hives);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getHives();
        });
    },
    onSubmit(evt) {
      evt.preventDefault();
      const payload = {
        sid: this.selected,
      };
      // console.log(this.selected)
      // console.log(payload)
      this.postSid(payload);
      this.getHives();
    },
    getSites() {
      const path = "http://localhost:5000/sites";
      axios
        .get(path)
        .then((res) => {
          this.sites = res.data.sites;
          this.selected = res.data.sites[0].id;
          //   console.log(res.data.sites[0])
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.postSid();
    this.getSites();
  },
};
</script>

<style scoped>
#inner {
  background: #f4f4f4;
  padding: 20px;
  margin-bottom: 10px;
}
</style>
