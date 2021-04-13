<template>
  <header>

    <section>
      <div class="col1">
        <h1>Profil</h1>
      </div>
      <div class="col1">
        <br />
        <button @click="showFormSite" class="button" v-show="!showSite">
          Přidat stanoviště
        </button>
        <form @submit="onSubmitSite" v-show="showSite">
          Název stanoviště
          <input
            v-model="site_name"
            id="form-title-input"
            type="text"
            required
            placeholder="Název"
          /><br /><br />
          Lokace
          <input
            v-model="location"
            id="form-title-input"
            type="text"
            required
            placeholder="Lokace"
          />
          <br /><br />
          <button @click="onSubmitSite" class="button">Uložit</button>
          <button @click="showFormSite" class="button">Zrušit</button>
        </form>
        <br /><br />
      </div>

      <div class="col1">
        <button @click="showFormHive" class="button" v-show="!showHive">
          Přidat úl
        </button>
        <form @submit="onSubmitHive" v-show="showHive">
          Stanoviště
          <select v-model="selected" @change="onChange">
            <option
              v-for="(site, index) in sites"
              :key="index"
              v-bind:value="site.id"
            >
              {{ site.name }}
            </option>
          </select>
          <br /><br />
          <!-- <div>{{ selected }}</div> -->
          Název úlu
          <input
            v-model="hive_name"
            id="form-title-input"
            type="text"
            required
            placeholder="Název"
          /><br /><br />
          <br /><br />
          <button @click="onSubmitHive" class="button">Uložit</button>
          <button @click="showFormHive" class="button">Zrušit</button>
        </form>
      </div>
    </section>
  </header>
</template>

<script>
import axios from "axios";


export default {
  data() {
    return {
      showSite: false,
      showHive: false,
      site_name: "",
      hive_name: "",
      location: "",
      selected: 1,
      sites: [],
      active: "profile"
    };
  },

  methods: {

    showFormSite() {
      this.showSite = !this.showSite;
    },
    showFormHive() {
      this.showHive = !this.showHive;
    },

    onChange() {
      // evt.preventDefault();
      const payload = {
        sid: this.selected,
      };
      this.onSubmitSite(payload);
    },
    getSites() {
      const path = "http://localhost:5000/sites";
      axios
        .get(path)
        .then((res) => {
          this.sites = res.data.sites;
          this.selected = res.data.sites[0].id;
          // console.log(res.data.sites[0]);
        })
        .catch((error) => {
          console.error(error);
        });
    },
    postSid(payload) {
      const path = "http://localhost:5000/add_site";
      axios
        .post(path, payload)
        .catch((error) => {
          console.error(error);
        });
      this.getSites();
    },
    postHid(payload) {
      const path = "http://localhost:5000/add_hive";
      axios
        .post(path, payload)
        .catch((error) => {
          console.error(error);
        });
      this.getSites();
    },
    onSubmitSite(evt) {
      evt.preventDefault();
      const payload = {
        uid: "gXifKfOg06XvU9NewGfqiFwasE12",
        site_name: this.site_name,
        location: this.location,
      };
      // console.log(this.selected)
      console.log(payload)
      this.postSid(payload);

      this.site_name = "";
      this.location = "";
    },
    onSubmitHive(evt) {
      evt.preventDefault();
      const payload = {
        sid: this.selected,
        hive_name: this.hive_name,
      };
      // console.log(this.selected)
      // console.log(payload)
      this.postHid(payload);

      this.hive_name = "";
      this.selected = 0;
    },
  },
  created() {

    this.getSites();
  },
};
</script>

<style scoped>
* {
  margin: 0;

  padding: 0;
}

div {
  /* font:15px/1.3 'Open Sans', sans-serif; */
  color: #5e5b64;
  text-align: left;
}

.col1 {
  background: #f4f4f4;
  margin-top: 10px;
  padding: 20px;
  /* width: 50%; */
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
}
</style>
