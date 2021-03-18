<template>
  <div class="container">
      <br><br>
        <form @submit="postSid" class="w-100">
            <div id="v-model-select-dynamic" class="demo">
                <select v-model="selected">
                    <option v-for="(site, index) in sites" :key="index">
                    {{ site.name }}
                    </option>
                </select>
                <div>{{selected}}</div>
            </div>
            <button @click="onSubmit" class="button" >Submit</button>
        </form>
        <br><br>
    <div class="rowaa">
      <table>
        <tbody>
        <tr v-for="(hive, index) in hives" :key="index">
            <td>
                <div id="inner">
                {{  hive.name }} <br>
                 <br><br>
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
import axios from 'axios';

axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*';

export default {
  data() {
    return {
        selected: 3,
      hives: [],
      sites: [],
    };
  },
  methods: {
    getHives() {
      const path = 'http://localhost:5000/hives';
      axios.get(path)
        .then((res) => {
          this.hives = res.data.hives;
        //   console.log(res.data.hives)
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    postSid(payload) {
      const path = 'http://localhost:5000/hives';
      axios.post(path, payload)
        .then((res) => {
          this.hives = res.data.hives;
          console.log(this.hives)
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getHives();
        });
    },
    onSubmit(evt){
        evt.preventDefault();
        const payload = {
            sid: this.selected
            }
        // console.log(this.selected)
        // console.log(payload)
        this.postSid(payload);
        this.getHives();
    },
    getSites() {
      const path = 'http://localhost:5000/sites';
      axios.get(path)
        .then((res) => {
          this.sites = res.data.sites;
          this.selected = res.data.sites[0].name
        //   console.log(res.data.sites[0])
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getHives();
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
