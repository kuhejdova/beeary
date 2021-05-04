<template>
  <main class="wrapper">
      <div class="left">
        <Timeline :selectedDate="date" v-on:event_child="onChange" />
      </div>
      <div class="right">
        <Month :selectedDate="date" />
      </div>
  </main>
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
      this.date = selectedDate;
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
  width: 100%;
  display: flex;

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
  max-width: 500px;
  flex: 1 1 auto;
  display: flex;
  justify-content: center;
  /* padding: 10px;  */
}

.right {
  flex: 1 0 auto;
}

@media (max-width: 1000px) {
  .wrapper {
    position: relative;
  }
  .left {
    left: 0px;
    top: 0px;
  }
  .right {
    position: absolute;
  }
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
