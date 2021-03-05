<template>
  <header>
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

export default {
  methods: {
    getDate(){
      return moment(new Date()).format('DD. MM. YYYY');
    }
  }
}



</script>

<style scoped>
*{
  margin:0;
  margin-left: 20px;
  padding:0;
}

div{
  font:15px/1.3 'Open Sans', sans-serif;
  color: #5e5b64;
  text-align:left;
}
</style>