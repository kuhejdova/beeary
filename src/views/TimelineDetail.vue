<template>
  <div>
    <main>
      <section>
        <div class="wrapper">
          <div class="left">
            <Timeline :selectedDate="date" />
          </div>
          <div class="right">
            <Month :selectedDate="date" v-on:event_child="onChange" />
          </div>
        </div>
      </section>
    </main>
  </div>
</template>

<script>
import moment from "moment";

import Timeline from "../components/Timeline.vue";
import Month from "../components/Month.vue";


export default {
  data() {
    return {
      noteToSave: [],
      date: moment(new Date()).format("M-YYYY"),
    };
  },
  methods: {
    onChange(selectedDate) {
      console.log(selectedDate)
      if (this.$route.query.date) {
        this.date = this.$route.query.date;
      }
    },
    onSubmit() {
      const payload = {
        noteToSave: this.noteToSave,
      };
      return payload;
    },
  },
  components: {
    Timeline,
    Month,
  },
  mounted() {
    if (this.$route.query.date) {
      this.date = this.$route.query.date;
    }
  },
};
</script>

<style scoped>
* {
  margin: 0;

  padding: 0;
}

.wrapper {
  display: grid;
  grid-template-columns: 39% 58%;
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

.left {
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
