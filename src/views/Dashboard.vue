<template>
  <div>

    <main>
      <section>
        <div class="wrapper">
          <div class="left">
            <div class="col1">
              <h1>Vítejte zpět</h1>
              <br />
              <h3>Dnes je: {{ getDate() }}</h3>
            </div>

            <br /><br />
            <div class="col2">
              <Sites />
            </div>
          </div>
          <div class="right">
            <Timeline/>
          </div>
        </div>
      </section>
    </main>
  </div>
</template>

<script>
import moment from "moment";

import Sites from "../components/Sites.vue";
import Timeline from "../components/Timeline.vue"

export default {
  methods: {
    getDate() {
      return moment(new Date()).format("DD. MM. YYYY");
    },
  },
  components: {

    Sites,
    Timeline,
  },
};
</script>

<style scoped>
* {
  margin: 0;

  padding: 0;
}

.wrapper{
  display: grid;
  grid-template-columns: 59% 39%;
  column-gap: 40px;
  row-gap: 10px;

  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
}

div {
  /* font:15px/1.3 'Open Sans', sans-serif; */
  font-weight: bold;
  color: #5e5b64;
  text-align: left;
}

.right {
  margin-left: auto;
  margin-right: auto;
  /* padding: 10px;  */
}

/* .left {
  padding-left: 20px;
} */

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
