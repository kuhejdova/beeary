<template>
  <div class="main-wrapper" v-if="displayDetail">
    <form class="form-sites" @submit="onSubmit">
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
      <div class="header-wrapper">
        <h2>{{ getDate() }}</h2>
        <button
          class="close"
          type="button"
          v-if="displayDetail"
          @click="displayClose"
        >
          x
        </button>
      </div>
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
      <div class="wrap-texts">
        <div class="left">
          <h3>Poznámky</h3>

          <div>
            <br />
            <div v-for="(note, index) in notes" :key="index">
              <li v-if="displayNoteDate(note.note_date)">
                <div>{{ note.note_date }} - {{ note.note_text }}</div>
              </li>
            </div>
          </div>
          <button @click="showForm" class="button" v-show="!show">
            Přidat
          </button>
          <form @submit="selectNotes" v-show="show">
            <label
              >Datum
              <input
                v-model="noteDateToSave"
                id="form-title-input"
                type="text"
                required
                placeholder="D.M.YYYY"
              />
            </label>
            <br />
            <label
              >Poznámka
              <input
                v-model="noteToSave"
                id="form-date-input"
                type="text"
                required
                placeholder="Přitejte poznámku"
              />
            </label>
            <br /><br />
            <button @click="onSubmitNote" class="button">Uložit</button>
            <button @click="showForm" class="button" type="button">
              Zrušit
            </button>
          </form>
        </div>

        <div class="right">
          <h3>Upozornění ze senzorů</h3>
          <div class="warnings">
            <br />
            <div
              v-for="(warning, index) in warnings"
              :key="index"
              class="warning"
            >
              <li>
                <div>{{ formatDate(warning.date) }} - {{ warning.value }}</div>
              </li>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import moment from "moment";
import axios from "axios";
import { baseUrl } from "../variables.js";

export default {
  props: { selectedDate: String },
  data() {
    return {
      noteToSave: "",
      noteDateToSave: this.todayDate(),
      notes: [],
      show: false,
      urlDate: moment(new Date()).format("M/YYYY"),
      activities: [],
      selected: 1,
      selectedHive: 1,
      hives: [],
      sites: [],
      displayDetail: false,
      warnings: [],
      dateFrom: moment()
        .clone()
        .startOf("month")
        .format("D.M.YYYY"),
      dateTo: moment()
        .clone()
        .endOf("month")
        .format("D.M.YYYY"),
    };
  },
  watch: {
    selectedDate: function() {
      this.showActivities();
      this.warnings = [];
      this.dateFrom = moment(this.selectedDate, "MM-YYYY")
        .clone()
        .startOf("month")
        .format("D.M.YYYY");
      this.dateTo = moment(this.selectedDate, "MM-YYYY")
        .clone()
        .endOf("month")
        .format("D.M.YYYY");
      this.showWarnings();
      this.displayDetail = true;
    },
  },
  methods: {
    displayClose() {
      this.displayDetail = false;
    },
    getDate() {
      // this.showActivities();
      moment.locale("cs");
      var dateCapitalized = moment(this.selectedDate, "MM-YYYY").format(
        "MMMM YYYY"
      );
      return dateCapitalized.charAt(0).toUpperCase() + dateCapitalized.slice(1);
    },
    todayDate() {
      return moment(new Date()).format("D.M.YYYY");
    },

    displayNoteDate(noteDate) {
      var dateToFormat = moment(noteDate, "D.M.YYYY").format("M-YYYY");
      return dateToFormat === this.selectedDate;
    },

    formatDate(inputDate) {
      return moment(inputDate).format("D.M.YYYY");
    },

    postNote(payload) {
      const path = baseUrl + "/add_note";
      axios.post(path, payload).catch((error) => {
        console.error(error);
      });
      this.getSites();
    },

    selectNotes() {
      const payload = {
        hid: this.selectedHive,
      };
      const path = baseUrl + "/notes";
      axios
        .post(path, payload)
        .then((res) => {
          this.notes = res.data.notes;

          // this.loadedNotes = true;
        })
        .catch((error) => {
          console.error(error);
        });

      // console.log(this.notes);
    },

    onSubmitNote(evt) {
      evt.preventDefault();
      const payload = {
        note_text: this.noteToSave,
        hid: this.selectedHive,
        note_date: this.noteDateToSave,
      };
      // console.log(this.selected)
      this.postNote(payload);

      this.note_text = "";
      this.note_date = this.todayDate();
      this.selectNotes();
      // this.show = !this.show;
      // this.selected = 0;
    },

    showForm() {
      this.show = !this.show;
    },

    showWarnings() {
      const payload = {
        hid: this.selectedHive,
        dateFrom: this.dateFrom,
        dateTo: this.dateTo,
      };
      // console.log(this.dateFrom);
      // console.log(this.dateTo);
      const path = baseUrl + "/hive_graph";
      axios
        .post(path, payload)
        .then((res) => {
          this.warnings.push.apply(
            this.warnings,
            res.data.graphData[0].warnings
          );
          this.warnings.push.apply(
            this.warnings,
            res.data.graphData[0].warnings_temperature
          );
          this.warnings.push.apply(
            this.warnings,
            res.data.graphData[0].warnings_weight
          );
          // this.loaded = true;
        })
        .catch((error) => {
          console.error(error);
        });
    },

    postMonth(payload) {
      const path = baseUrl + "/activities";
      axios
        .post(path, payload)
        .then((res) => {
          this.activities = res.data.activities;
          // this.loaded = true;
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
      const path = baseUrl + "/hives";
      axios
        .post(path, payload)
        .then((res) => {
          this.hives = res.data.hives;
          this.chartdata = res.data.hives;
          // console.log(this.hives)
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
      const path = baseUrl + "/sites";
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
    this.warnings = [];
    this.dateFrom = moment(this.selectedDate, "MM-YYYY")
      .clone()
      .startOf("month")
      .format("D.M.YYYY");
    this.dateTo = moment(this.selectedDate, "MM-YYYY")
      .clone()
      .endOf("month")
      .format("D.M.YYYY");
    this.showActivities();
    this.showWarnings();
    // console.log(this.selectedDate);

    this.displayDetail = window.screen.width > 1000;
  },
  created() {
    this.postSid();
    this.getSites();
    this.selectNotes();
    this.todayDate();
  },
};
</script>

<style scoped>
* {
  margin: 0;
}

.main-wrapper {
  /* font:15px/1.3 'Open Sans', sans-serif; */
  font-weight: bold;
  color: #5e5b64;
  text-align: left;
}

.col1 {
  background: #f4f4f4;
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
  width: 50px;
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
  margin-left: 20px;
}


div {
  overflow-wrap: break-word;
}

.form-sites {
  background: rgb(255, 255, 255);
  padding: 20px;
}

.wrap-texts {
  display: flex;
  width: 100%;
  height: 100%;
  flex-wrap: wrap;
  justify-content: space-evenly;

  /* margin-right: auto; */
}

.left {
  /* flex: 1 1 auto; */
  display: flex;
  flex-direction: column;
  margin-right: auto;
  flex-grow: 1;
  flex-basis: 0;
  max-width: 400px;
  margin-bottom: 10px;
  /* justify-content: center; */
}

.right {
  /* flex: 1 1; */
  display: flex;
  flex-direction: column;
  margin-right: auto;
  flex-grow: 1;
  flex-basis: 0;
  min-width: 300px;

  /* justify-content: center; */
}

.warnings {
  max-height: 200px;
  overflow-y: auto;
  width: 100%;
}

.header-wrapper {
  display: flex;
}

.close {
  display: none;
  margin-left: auto;
}

.warning {
  width: 100%;
}

.button {
  max-height: 50px;
}

@media (max-width: 1000px) {
  .close {
    display: unset;
  }
}
</style>
