<template>
  <div class="main-wrapper">
    <br />
    <form @submit="onSubmit" class="w-100">
      <div id="dynamicSelect" class="demo">
        <span
          >Stanoviště
          <select v-model="selected" @change="onSubmit">
            <option
              v-for="(site, index) in sites"
              :key="index"
              v-bind:value="site.id"
            >
              {{ site.name }}
            </option>
          </select>
        </span>

        <span>
          Úl
          <select v-model="selectedHive" @change="onSubmit">
            <option
              v-for="(hive, index) in hives"
              :key="index"
              v-bind:value="hive.id"
            >
              {{ hive.name }}
            </option>
          </select>
        </span>
      </div>
    </form>
    <div class="col1">
      <h2>{{ getDate() }}</h2>
      <br />
      <div v-for="(activity, index) in activities" :key="index" class="wrapper">
        <object
          id="svgSetColor"
          type="image/svg+xml"
          :data="displayPictogram(activity.pictogram)"
          v-on:load="loadSetColor"
        >
          <img src="displayPictogram(activity.pictogram)" alt="Beeary" />
        </object>
        <div id="inner">{{ activity.description }}</div>
        <br />
      </div>
      <br />
      <p>Poznámky</p>
      <br />
      <div v-for="(note, index) in notes" :key="index">
        <li>
          <div>{{ note.note_text }}</div>
        </li>
      </div>
      <br /><br />
      <button @click="showForm" class="button" v-show="!show">Přidat</button>
      <form @submit="onSubmitNote" v-show="show">
        <input
          id="form-title-input"
          type="text"
          required
          placeholder="Přitejte poznámku"
        />
        <br /><br />
        <button @click="onSubmit" class="button">Uložit</button>
        <button @click="showForm" class="button">Zrušit</button>
      </form>
    </div>
  </div>
</template>

<script>
import moment from "moment";
import axios from "axios";

export default {
  props: { selectedDate: String },
  data() {
    return {
      noteToSave: [],
      notes: [],
      show: false,
      urlDate: moment(new Date()).format("M/YYYY"),
      loaded: false,
      loadedNotes: false,
      activities: [],
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
    getDate() {
      // this.showActivities();
      moment.locale("cs");
      var dateCapitalized = moment(this.selectedDate, "MM-YYYY").format(
        "MMMM YYYY"
      );
      return dateCapitalized.charAt(0).toUpperCase() + dateCapitalized.slice(1);
    },
    onSubmitNote() {
      const payload = {
        note_text: this.noteToSave,
      };
      return payload;
    },

    postNote(payload) {
      const path = "http://localhost:5000/add_note";
      axios.post(path, payload).catch((error) => {
        console.error(error);
      });
      this.getSites();
    },

    selectNotes() {
      const payload = {
        hid: this.selectedHive,
      };
      const path = "http://localhost:5000/notes";
      axios
        .post(path, payload)
        .then((res) => {
          this.notes = res.data.notes;

          this.loadedNotes = true;
        })
        .catch((error) => {
          console.error(error);
        });

      console.log(this.notes);
    },

    // onSubmitNote(evt) {
    //   evt.preventDefault();
    //   const payload = {
    //     sid: this.selected,
    //     hive_name: this.hive_name,
    //   };
    //   // console.log(this.selected)
    //   // console.log(payload)
    //   this.postHid(payload);

    //   this.hive_name = "";
    //   this.selected = 0;
    // },

    showForm() {
      this.show = !this.show;
    },
    postMonth(payload) {
      const path = "http://localhost:5000/activities";
      axios
        .post(path, payload)
        .then((res) => {
          this.activities = res.data.activities;
          this.loaded = true;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    showActivities() {
      const payload = {
        month: moment(this.selectedDate, "MM-YYYY").month() + 1,
      };
      this.postMonth(payload);
    },
    displayPictogram(pictogramId) {
      switch (pictogramId) {
        case 1:
          return require("../../public/images/bee_queen.svg");
        case 2:
          return require("../../public/images/honey.svg");
        case 3:
          return require("../../public/images/queen_cells.svg");
        case 4:
          return require("../../public/images/check.svg");
        case 5:
          return require("../../public/images/feeding.svg");
        case 6:
          return require("../../public/images/swarming.svg");
        case 7:
          return require("../../public/images/hives.svg");
        case 8:
          return require("../../public/images/timeline.svg");
        case 9:
          return require("../../public/images/monitoring.svg");
        case 10:
          return require("../../public/images/blooming.svg");
        default:
          alert("something is wrong");
          return require("../../public/images/logo.svg");
      }
    },
    loadSetColor(event) {
      var documentStyle = getComputedStyle(document.body);
      event.currentTarget
        .getSVGDocument()
        .querySelector("#backgroundHex")
        .setAttribute("fill", documentStyle.getPropertyValue("--main_color"));
    },

    postSid(payload) {
      const path = "http://localhost:5000/hives";
      axios
        .post(path, payload)
        .then((res) => {
          this.hives = res.data.hives;
          this.chartdata = res.data.hives;

          this.loaded = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
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
      this.selectNotes();
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
  mounted() {
    if (this.$route.query.date) {
      this.urlDate = this.$route.query.date.replace("-", "/");
    }
    this.showActivities();
    console.log(this.selectedDate);
  },
  created() {
    this.postSid();
    this.getSites();
    this.selectNotes();
  },
};
</script>

<style scoped>
* {
  margin: 0;
}

div {
  /* font:15px/1.3 'Open Sans', sans-serif; */
  font-weight: bold;
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

.wrapper {
  display: flex;
  align-items: center;
}

#inner {
  /* display: inline-block; */
  margin-left: 20px;
}

object {
  height: 50px;
  /* vertical-align: middle; */
}

#dynamicSelect {
  display: flex;
  /* justify-content: space-evenly;
  margin-right: auto; */
}

span {
  margin-right: auto;
}

li {
  margin-left: 10px;
}
</style>
