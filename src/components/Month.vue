<template>
  <div class="col1">
    <h2>{{ getDate() }}</h2>
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

export default {
  data() {
    return {
      noteToSave: [],
      show: false,
    };
  },
  methods: {
    getDate() {
      moment.locale("cs");
      var dateCapitalized = moment(new Date()).format("MMMM YYYY");
      return dateCapitalized.charAt(0).toUpperCase() + dateCapitalized.slice(1);
    },
    onSubmit() {
      const payload = {
        noteToSave: this.noteToSave,
      };
      return payload;
    },
    showForm(){
        this.show = !this.show;
    }
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

</style>
