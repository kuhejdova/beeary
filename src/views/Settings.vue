<template>

  <header>
    <MenuTop/>
    <section>
      
      <!-- <div class="col1">
      </div> -->
    </section>
  </header>
</template>


<script>
import MenuTop from '../components/MenuTop.vue'

export default {
  components: {
    MenuTop,
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
  color: #5e5b64;
  text-align:left;
}
</style>