<template>
  <header>
    <MenuTop />
    <section>
      <div class="col1">
      <button @click="showForm" class="button" v-show="!show">Přidat stanoviště</button>
    <form @submit="onSubmit" v-show="show">
      Název stanoviště <input v-model="name"
        id="form-title-input"
        type="text"
        required
        placeholder="Název"
      /><br><br>
      Lokace <input v-model="location"
        id="form-title-input"
        type="text"
        required
        placeholder="Lokace"
      />
      <br /><br />
      <button @click="onSubmit" class="button">Uložit</button>
      <button @click="showForm" class="button">Zrušit</button>
    </form>
    </div>
    </section>
  </header>
</template>

<script>
import axios from "axios";
import MenuTop from "../components/MenuTop.vue";

export default {
  data() {
    return {
      show: false,
      name: '',
      location: '',
    };
  },
  components: {
    MenuTop,
  },
  methods: {
    // onSubmit() {
    //   const payload = {
    //     noteToSave: this.noteToSave,
    //   };
    //   return payload;
    // },
    showForm(){
        this.show = !this.show;
    },
    postSid(payload) {
      const path = "http://localhost:5000/add_site";
      axios
        .post(path, payload)
        // .then((res) => {
        //   this.hives = res.data.hives;
        // })
        .catch((error) => {
          console.error(error);
        });
    },
    onSubmit(evt) {
      evt.preventDefault();
      const payload = {
        uid: "gXifKfOg06XvU9NewGfqiFwasE12",
        site_name: this.name,
        location: this.location,
      };
      // console.log(this.selected)
      // console.log(payload)
      this.postSid(payload);
    
      this.name= '';
      this.location= '';
    },
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
