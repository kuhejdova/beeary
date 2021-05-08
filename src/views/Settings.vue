<template>
  <header>

    <section>
      <div class="col1">
        <h1>Nastavení</h1>
      </div>
      <div class="col1">
        <h2>Přidat stanoviště</h2>
        <form @submit="onSubmitSite">
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
        </form>
      </div>

      <div class="col1">
        <h2>Přidat úl</h2>
        <form @submit="onSubmitHive">
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
          Název úlu
          <input
            v-model="hive_name"
            id="form-title-input"
            type="text"
            required
            placeholder="Název"
          /><br /><br />
          <button @click="onSubmitHive" class="button">Uložit</button>
        </form>
      </div>

      <div class="col1">
        <h2>Odebrat stanoviště</h2>
        <form @submit="onSubmitDeleteSite">
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
          <button @click="onSubmitDeleteSite" class="button">Uložit</button>
        </form>
      </div>
    </section>
  </header>
</template>

<script>
import axios from "axios";
import { baseUrl } from "../variables.js";


export default {
  data() {
    return {
      // showSite: false,
      // showHive: false,
      site_name: "",
      hive_name: "",
      location: "",
      selected: 1,
      sites: [],
      active: "profile"
    };
  },

  methods: {

    // showFormSite() {
    //   this.showSite = !this.showSite;
    // },
    // showFormHive() {
    //   this.showHive = !this.showHive;
    // },

    onChange() {
      // evt.preventDefault();
      const payload = {
        sid: this.selected,
      };
      this.onSubmitSite(payload);
    },
    getSites() {
      const path = baseUrl + "/sites";
      const payload = {
        "email": localStorage.userEmail,
      }
      axios
        .post(path, payload)
        .then((res) => {
          this.sites = res.data.sites;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    postSid(payload) {
      const path = baseUrl + "/add_site";
      axios
        .post(path, payload)
        .catch((error) => {
          console.error(error);
        });
      this.getSites();
    },
    postHid(payload) {
      const path = baseUrl + "/add_hive";
      axios
        .post(path, payload)
        .catch((error) => {
          console.error(error);
        });
      this.getSites();
    },
    postDeleteSid(payload) {
      const path = baseUrl + "/delete_site";
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
        uid: localStorage.userEmail,
        site_name: this.site_name,
        location: this.location,
      };
      // console.log(this.selected)
      // console.log(payload)
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

    onSubmitDeleteSite(evt) {
      evt.preventDefault();
      const payload = {
        sid: this.selected
      };
      // console.log(this.selected)
      // console.log(payload)
      this.postDeleteSid(payload);
    }
  },
  created() {

    this.getSites();
  },
};
</script>

<style scoped>
* {
  margin: 0;

  /* padding: 0; */
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
