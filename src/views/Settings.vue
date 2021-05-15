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
          <SelectSite v-on:event_child="onChangeSite" :key="redraw" />
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
          <SelectSite v-on:event_child="onChangeSite2" :key="redraw" />
          <button @click="onSubmitDeleteSite" class="button">Uložit</button>
        </form>
      </div>
    </section>
  </header>
</template>

<script>
import axios from "axios";
import { baseUrl } from "../variables.js";
import SelectSite from "../components/selectSite.vue";

export default {
  components: {
    SelectSite,
  },
  data() {
    return {
      site_name: "",
      hive_name: "",
      location: "",
      selected: 1,
      hives: [],
      selected2: 1,
      hives2: [],
      sites: [],
      redraw: 0,
    };
  },

  methods: {
    onChangeSite(childSite) {
      this.selected = childSite[0];
      this.hives = childSite[1];

      this.site_name = "";
      this.location = "";
    },

    onChangeSite2(childSite) {
      this.selected2 = childSite[0];
      this.hives2 = childSite[1];

      this.site_name = "";
      this.location = "";
    },

    onChange() {
      const payload = {
        sid: this.selected,
      };
      this.onSubmitSite(payload);
    },
    postSid(payload) {
      const path = baseUrl + "/add_site";
      axios
        .post(path, payload)
        .then(() => {
          this.redraw += 1;
        })
        .catch((error) => {
          console.error(error);
        });
      // this.getSites();
    },
    postHid(payload) {
      const path = baseUrl + "/add_hive";
      axios.post(path, payload).catch((error) => {
        console.error(error);
      });
      // this.getSites();
    },
    postDeleteSid(payload) {
      const path = baseUrl + "/delete_site";
      axios.post(path, payload).catch((error) => {
        console.error(error);
      });
    },
    onSubmitSite(evt) {
      evt.preventDefault();
      const payload = {
        uid: localStorage.userEmail,
        site_name: this.site_name,
        location: this.location,
      };
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
      this.postHid(payload);

      this.hive_name = "";
      this.selected = 0;
    },

    onSubmitDeleteSite(evt) {
      evt.preventDefault();
      const payload = {
        sid: this.selected2,
      };
      this.postDeleteSid(payload);
    },
  },
};
</script>

<style scoped>
* {
  margin: 0;
}

div {
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
