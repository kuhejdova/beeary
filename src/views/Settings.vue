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
          <button @click="onSubmitSite" class="button">Uložit</button>
        </form>
      </div>

      <div class="col1">
        <h2>Přidat úl</h2>
        <form @submit="onSubmitHive">
          <div class="label-wrapper">
            <label>Stanoviště</label>
            <SelectSite v-on:event_child="onChangeSite" :key="redraw" />
          </div>
          <br />
          Název úlu
          <input
            v-model="hive_name"
            id="form-title-input"
            type="text"
            required
            placeholder="Název"
          />
          <button @click="onSubmitHive" class="button">Uložit</button>
        </form>
      </div>

      <div class="col1">
        <h2>Odebrat stanoviště</h2>
        <form @submit="onSubmitDeleteSite">
          <div class="label-wrapper">
            <label>Stanoviště</label>
            <SelectSite v-on:event_child="onChangeSite2" :key="redraw" />
          </div>
          <button @click="onSubmitDeleteSite" class="button">Uložit</button>
        </form>
      </div>

      <div class="col1">
        <h2>Odebrat úl</h2>
        <form @submit="onSubmitDeleteHive">
          <div class="label-wrapper">
            <label>Stanoviště</label>
            <SelectSite v-on:event_child="onChangeSite3" :key="redraw" />
          </div>
          <div class="label-wrapper"  >
            <label>Úl</label>
            <select v-model="selectedHive3" :key="redraw">
            <option
              v-for="(hive, index) in hives3"
              :key="index"
              v-bind:value="hive.id"
            >
              {{ hive.name }}
            </option>
          </select>
          </div>
          <button @click="onSubmitDeleteHive" class="button">Uložit</button>
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
      selected3: 1,
      hives3: [],
      selectedHive3: 1,
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

    onChangeSite3(childSite) {
      this.selected3 = childSite[0];
      this.hives3 = childSite[1];
      this.selectedHive3 = childSite?.[1]?.[0]?.id ?? 0;
      console.log(this.selectedHive3);

      this.site_name = "";
      this.location = "";
    },

    onChange(hid) {
      this.selectedHive3 = hid;
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
      const path = baseUrl + "/add_hive";
      axios.post(path, payload)
      .then(() => {
          this.redraw += 1;
        })
        .catch((error) => {
        console.error(error);
      });

      this.hive_name = "";
    },

    onSubmitDeleteSite(evt) {
      evt.preventDefault();
      const payload = {
        sid: this.selected2,
      };
      const path = baseUrl + "/delete_site";
      axios.post(path, payload)
      .then(() => {
          this.redraw += 1;
        })
      .catch((error) => {
        console.error(error);
      });
    },

    onSubmitDeleteHive(evt) {
      evt.preventDefault();
      const payload = {
        hid: this.selectedHive3,
      };
      const path = baseUrl + "/delete_hive";
      axios.post(path, payload)
      .then(() => {
          this.redraw += 1;
          console.log(this.redraw);
        })
        .catch((error) => {
        console.error(error);
      });
    },

    // onSubmit(evt) {
    //   evt.preventDefault();
    //   this.selectedHive3 = 
    // },
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

.label-wrapper {
  display: flex;
  align-items: center;
}

label {
  margin-right: 20px;
}

button {
  margin-top: 10px;
}
</style>
