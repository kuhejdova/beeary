<template>
  <div>

    <main>
      <section>
        <div class="wrapper">
          <div class="left"> 
            <!-- Nejaky vif aby tu mohly byt dve komponenty, jedna pro detail a jedna pro vsechny -->
            <Hives v-on:event_child="onChange" v-show="show"/>
            <HiveDetail :currentHive="currentHive" v-show="!show"/>
          </div>
          <div class="right">
            <Hexagons />
          </div>
        </div>
      </section>
    </main>
  </div>
</template>

<script>

import Hives from "../components/Hives.vue";
import HiveDetail from "../components/HiveDetail"
import Hexagons from "../components/Hexagons.vue";

export default {
    components: {

    Hives,
    HiveDetail,
    Hexagons,
  },
  data() {
    return {
      currentHive: 0,
      show: true,
    };
  },
  watch: {
    $route: function() {
      if (parseInt(this.$route.query.hid) == 0 || !this.$route.query.hid){
        this.show = true
      }
      else {
        this.show = false
      }
    },
  },
  methods: {
    onChange(current) {
      this.currentHive = current
      console.log(parseInt(this.$route.query.hid))
      if (parseInt(this.$route.query.hid) == 0){
        this.show = true
        // console.log('here', parseInt(this.$route.query.hid))
      }
      else {
        this.show = false
      }
      console.log(this.show)

    },
    // onSubmit() {
    //   const payload = {
    //     noteToSave: this.noteToSave,
    //   };
    //   return payload;
    // },
  },
  mounted() {
    if (this.$route.query.hid) {
      this.currentHive = parseInt(this.$route.query.hid);
    }
  },

};
</script>

<style scoped>
* {
  margin: 0;

  padding: 0;
}

section {
  margin-left: 20px;
}

div {
  /* font:15px/1.3 'Open Sans', sans-serif; */
  font-weight: bold;
  color: #5e5b64;
  text-align: left;
}

.wrapper{
  display: grid;
  grid-template-columns: 70% 27%;
  column-gap: 40px;
  row-gap: 10px;

  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
}

.right {
  width: 26vw;
  overflow-x: hidden;
}

.left {
  padding-left: 20px;
}

</style>
