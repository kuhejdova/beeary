<template>
  <div class="container">
    <div class="rowaa">
      <table>
        <tbody>
        <tr v-for="(site, index) in sites" :key="index">
            <td>
                <div id="inner">
                {{ site.name }} <br>
                - {{ site.location }} <br><br>
                {{ site.event }}
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

export default {
  data() {
    return {
      sites: [],
    };
  },
  methods: {
    getSites() {
      const path = 'http://localhost:5000/sites';
      axios.get(path)
        .then((res) => {
          this.sites = res.data.sites;
          console.log(res.data.sites)
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
    margin-bottom: 10px;
}

</style>
