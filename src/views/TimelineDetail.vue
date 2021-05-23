<template>
  <div class="wrapper">
    <div class="left">
      <Timeline :selectedDate="date" v-on:event_child="onChange" />
    </div>
    <div class="right" v-if="opened">
      <Month :selectedDate="date" :isOpened="opened" v-on:event_open="onOpen" />
    </div>
  </div>
</template>

<script>
import moment from "moment";

import Timeline from "../components/Timeline.vue";
import Month from "../components/Month.vue";

export default {
  data() {
    return {
      date: moment(new Date()).format("M-YYYY"),
      opened: true,
    };
  },
  methods: {
    onChange(selectedDate) {
      this.date = selectedDate;
      this.opened = true;
    },

    onOpen() {
      this.opened = false;
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
  overflow-y: auto;
  overflow-x: hidden;
  -ms-overflow-style: none; /* IE and Edge */
  scrollbar-width: none;
}

/* Hide scrollbar for Chrome, Safari and Opera */
.left::-webkit-scrollbar,
.right::-webkit-scrollbar {
  display: none;
}

.left {
  width: 500px;
  flex: 1 0 auto;
  display: flex;
  justify-content: center;
  max-width: 500px;
}

.right {
  flex: 1 0 auto;
}

@media (max-width: 1200px) {
  template {
    display: flex;
  }

  .wrapper {
    position: relative;
    justify-content: center;
  }

  .left {
    width: 100%;
    left: 0px;
    top: 0px;
    min-width: 0px;
    max-width: auto;
  }
  .right {
    position: absolute;
    width: 100%;
  }
}
</style>
