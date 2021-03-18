<template>

  <header>
    <div class="col0">
      <MenuTop/>
    </div>
    <section>
      <div class="col2">
        <Hives/>
      </div>
    </section>
  </header>
</template>


<script>
import MenuTop from '../components/MenuTop.vue'
import Hives from '../components/Hives.vue'

export default {
  components: {
    MenuTop,
    Hives
  }
}



</script>

<style scoped>
*{
  margin:0;

  padding:0;
}

section{
    margin-left: 20px;
}

div{
  /* font:15px/1.3 'Open Sans', sans-serif; */
  font-weight: bold;
  color: #5e5b64;
  text-align:left;
}

.col1 {
  background: #f4f4f4;
  margin-top: 10px;
  padding: 20px;
}
</style>