<template>
  <div class="wrapper">
    <div class="left">
      <Hives v-on:event_child="onChange" v-if="show" />
      <HiveDetail :currentHive="currentHive" v-if="!show" />
    </div>
    <div class="right">
      <Hexagons />
    </div>
  </div>
</template>

<script>
import Hives from "../components/Hives.vue";
import HiveDetail from "../components/HiveDetail";
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
      if (parseInt(this.$route.query.hid) == 0 || !this.$route.query.hid) {
        this.show = true;
      } else {
        this.show = false;
      }
    },
  },
  methods: {
    onChange(current) {
      this.currentHive = current;

      if (parseInt(this.$route.query.hid) == 0) {
        this.show = true;
      } else {
        this.show = false;
      }
    },
  },
  mounted() {
    if (this.$route.query.hid) {
      this.currentHive = parseInt(this.$route.query.hid);
      if (this.currentHive == 0) {
        this.show = true;
      } else {
        this.show = false;
      }
    }
  },
};
</script>

<style scoped>
* {
  margin: 0;

  padding: 0;
}

div {
  font-weight: bold;
  color: #5e5b64;
  text-align: left;
}

.wrapper {
  width: 100%;
  height: 100%;
  display: flex;
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

.right {
  max-width: 300px;
  flex: 1 0 auto;
  display: flex;
  justify-content: left;
  /* padding: 10px;  */
}

.left {
  flex: 1 1 auto;
}

@media (max-width: 1000px) {
  .right {
    display: none;
  }
  .left {
    padding: 0px;
    widows: 100%;
  }
}
</style>
