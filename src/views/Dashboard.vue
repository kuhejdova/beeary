<template>
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
      <Timeline />
    </div>
  </div>
</template>

<script>
import moment from "moment";

import Sites from "../components/Sites.vue";
import Timeline from "../components/Timeline.vue";

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

.wrapper {
  width: 100%;
  height: 100%;
  display: flex;

  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
}

div {
  font-weight: bold;
  color: #5e5b64;
  text-align: left;
}

.left,
.right {
  height: 100%;
  overflow: auto;
  -ms-overflow-style: none; /* IE and Edge */
  scrollbar-width: none;
}

/* Hide scrollbar for Chrome, Safari and Opera */
.left::-webkit-scrollbar,
.right::-webkit-scrollbar {
  display: none;
}

.col1 {
  background: #f4f4f4;
  margin-top: 10px;
  padding: 20px;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
}

.right {
  max-width: 500px;
  flex: 1 0 auto;
  display: flex;
  justify-content: center;
}

.left {
  flex: 1 1 auto;
}

@media (max-width: 800px) {
  .right {
    display: none;
  }
}
</style>
