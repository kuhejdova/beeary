<template>
  <div class="main-wrapper" v-if="isOpened">
    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"
    />
    <form class="form-sites" @submit="onSubmit">
      <div id="dynamicSelect" class="demo">
        <span class="site-label"
          ><label>Stanoviště</label>
          <SelectSite v-on:event_child="onChangeSite" />
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
        <i
          class="fa fa-times"
          id="close"
          type="button"
          v-if="isOpened"
          @click="displayClose"
        ></i>
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
              <li  class="my-li" v-if="displayNoteDate(note.note_date)">
                <div class="wrap-note">
                  <div class="wrap-note-text">
                    {{ note.note_date }} - {{ note.note_text }}
                  </div>
                  <i class="fa fa-times" @click="deleteNote(note.note_id)"></i>
                </div>
              </li>
            </div>
          </div>
          <div class="add-note-wrapper" v-if="hives.length !== 0">
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
            <br /><span id="displayError" ref="displayError"></span><br />
            <button @click="onSubmitNote" class="button">Uložit</button>
            <button @click="showForm" class="button" type="button">
              Zrušit
            </button>
          </form>
          </div>
        </div>

        <div class="right">
          <h3>Upozornění ze senzorů</h3>
          <div class="warnings">
            <br />
            <div v-if="warnings.length === 0">
              Žádné nové upozornění.
            </div>
            <div
              v-for="(warning, index) in warnings"
              :key="index"
              class="warning"
            >
              <li class="my-li">
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
import SelectSite from "./selectSite.vue";

export default {
  props: { selectedDate: String, isOpened: Boolean },
  components: {
    SelectSite,
  },
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
    },
  },
  methods: {
    displayClose() {
      this.$emit("event_open");
    },

    getDate() {
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
      axios.post(path, payload)
      .then(() => this.selectNotes())
      .catch((error) => {
        console.error(error);
      });
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
        })
        .catch((error) => {
          console.error(error);
        });
    },

    onSubmitNote(evt) {
      evt.preventDefault();
      if (this.hives == []) {
        alert("no hive selected");
      }

      var noteDateChecked = moment(this.noteDateToSave, "D.M.YYYY", true);
      if (!noteDateChecked.isValid()) {
        this.$refs.displayError.innerHTML =
          "Zadané datum je ve špatném formátu. Datum zadejte ve formátu D.M.YYYY";
        return;
      }

      this.$refs.displayError.innerHTML = "";

      const payload = {
        note_text: this.noteToSave,
        hid: this.selectedHive,
        note_date: this.noteDateToSave,
      };
      this.postNote(payload);

      this.noteToSave = "";
      this.note_date = this.todayDate();
    },

    deleteNote(nid) {
      const payload = {
        note_id: nid,
      };
      const path = baseUrl + "/delete_note";
      axios.post(path, payload)
      .then(() => this.selectNotes())
      .catch((error) => {
        console.error(error);
      });
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
      const path = baseUrl + "/hive_graph";
      axios
        .post(path, payload)
        .then((res) => {
          this.warnings = [];
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

    onChangeSite(childSite) {
      this.selected = childSite[0];
      this.hives = childSite[1];
      this.selectedHive = childSite?.[1]?.[0]?.id ?? 0;
      // console.log(this.selectedHive);
      this.selectNotes();
      this.showWarnings();
    },
    onSubmit(evt) {
      evt.preventDefault();
      if (this.hives != []) {
        this.selectNotes();
      }
    },
  },
  mounted() {
    if (this.$route.query.date) {
      this.urlDate = this.$route.query.date.replace("-", "/");
    }
    this.warnings = [];
    this.showActivities();
    this.displayDetail = window.screen.width > 1000;
  },
  created() {
    this.todayDate();
  },
};
</script>

<style scoped>
* {
  margin: 0;
}

.main-wrapper {
  font-weight: bold;
  color: #5e5b64;
  text-align: left;
}

.col1 {
  background: #f4f4f4;
  padding: 20px;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
}

.wrapper {
  display: flex;
  align-items: center;
}

#inner {
  margin-left: 20px;
}

object {
  height: 50px;
  width: 50px;
}

#dynamicSelect {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  /* flex-direction: column; */
}

span {
  margin-right: auto;
}

li {
  margin-left: 20px;
}

.my-li {
  display: flex;
  align-items: center;
}

.my-li::before {
    display: block;
    content: "";
    width: 5px;
    height: 5px;
    background: black;
    border-radius: 50%;
    margin-right: 10px;
    flex: 0 0 auto;
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
}

.left {
  display: flex;
  flex-direction: column;
  margin-right: auto;
  width: 0px;
  margin-bottom: 10px;
  min-width: 300px;
  flex: 1;
}

.right {
  flex: 1;
  display: flex;
  flex-direction: column;
  margin-right: auto;
  widows: 0px;
  min-width: 300px;
}

.warnings {
  max-height: 200px;
  overflow-y: auto;
  width: 100%;
}

.header-wrapper {
  display: flex;
}

#close {
  display: none;
  margin-left: auto;
  font-size: 25px;
}

.warning {
  width: 100%;
}

.button {
  max-height: 50px;
}

.wrap-note {
  display: flex;
  justify-content: space-between;
  padding-right: 20px;
}

.wrap-note-text {
  overflow: hidden;
  text-overflow: ellipsis;
}

i {
  font-family: "FontAwesome";
}

i:hover {
  cursor: pointer;
}

.site-label {
  display: flex;
  justify-content: center;
}

label {
  margin-right: 10px;
  align-self: center;
}

#displayError {
  color: red;
}

@media (max-width: 1200px) {
  #close {
    display: unset;
  }

  .wrap-note {
    max-width: calc(100% - 15px);
  }

  .left, .right {
    width: 100%;
    min-width: auto;
  }

  /* #dynamicSelect {
  display: flex;
  flex-direction: column;
} */
}
</style>
