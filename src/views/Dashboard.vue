<template>

  <header>
    <MenuTop/>
    <section>
      
      <div class="col1">
        <h1>Vítejte zpět</h1>
        <br>
        <h3>Dnes je: {{getDate()}}</h3>
      </div>
    </section>
  </header>
</template>


<script>
import moment from 'moment'
import MenuTop from '../components/MenuTop.vue'

export default {
  methods: {
    getDate(){
      return moment(new Date()).format('DD. MM. YYYY');
    }
  },
  components: {
    MenuTop
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
</style>