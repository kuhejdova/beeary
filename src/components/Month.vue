<template>
  <div class="col1">
    <h2>{{ getDate() }}</h2>
    <br />
    <div v-for="(activity, index) in activities" :key="index" class="wrapper">
      <!-- <img :src="displayPictogram(activity.pictogram)" alt="Beeary" /> -->
      <object
            id="svgSetColor"
            type="image/svg+xml"
            :data="displayPictogram(activity.pictogram)"
            v-on:load="loadSetColor"
          >
            <img src="displayPictogram(activity.pictogram)" alt="Beeary" />
          </object>
      <!-- <div id="inner">{{ displayPictogram(activity.pictogram)}}</div> -->
      <div id="inner">{{ activity.description }}</div>
      <br />
    </div>
    <br />
    <p>Poznámky</p>
    <br /><br />
    <button @click="showForm" class="button" v-show="!show">Přidat</button>
    <form @submit="onSubmit" v-show="show">
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
</template>

<script>
import moment from "moment";
import axios from "axios";

export default {
  props: { selectedDate: String },
  data() {
    return {
      noteToSave: [],
      show: false,
      urlDate: moment(new Date()).format("M/YYYY"),
      loaded: false,
      activities: [],
    };
  },
  methods: {
    getDate() {
      this.showActivities();
      moment.locale("cs");
      var dateCapitalized = moment(this.selectedDate, "MM-YYYY").format(
        "MMMM YYYY"
      );
      return dateCapitalized.charAt(0).toUpperCase() + dateCapitalized.slice(1);
    },
    onSubmit() {
      const payload = {
        noteToSave: this.noteToSave,
      };
      return payload;
    },
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
  },
  mounted() {
    if (this.$route.query.date) {
      this.urlDate = this.$route.query.date.replace("-", "/");
    }
    this.showActivities();
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

.wrapper{
  display: flex;
    align-items:center;
}

#inner{
  /* display: inline-block; */
  margin-left: 20px;
}

object{
  height:50px;
  /* vertical-align: middle; */
}

</style>
