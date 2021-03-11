<template>
    <section>
        <header>
            <script id="bgl" type="text/template">
            <div>
                <span v-bgl-level="item.value"> {{ item.value }} </span> mmol
            </div>
            </script>

            <script id="bp" type="text/template">
            <div>
                <span v-systolic-level="item.systolic"> Systolic: {{item.systolic }} mmHg </span> /
                <span v-diastolic-level="item.diastolic"> Diastolic: {{item.diastolic}} mmHg </span> <br>
                <span v-diastolic-level="item.pulse"> Pulse: {{ item.pulse }} </span>
            </div>
            </script>

            <script id="food" type="text/template">
            <div>
                {{ item.value }}
            </div>
            </script>

            <script id="medicine" type="text/template">
            <div>
                {{ item.value }}
            </div>
        </script>
        </header>
        <div id="app">
        <h3> Daily Intake Timeline (Made with Vue Js) </h3>  
        <li v-for="(item, index) in items" :class="item.type" v-bind:key="item.type" >
            <div class="entry-time"> 
            {{ item.entryTime }} 
            </div>      
            <div class="reading-title"> 
            {{index + 1}}. {{ item.type }} 
            </div> 
            <div class="details">
            <blood-glucose-level v-if="item.type == 'bgl'" :item="item"> </blood-glucose-level>
            <blood-pressure v-if="item.type == 'bp'" :item="item"> </blood-pressure>
            <food v-if="item.type == 'food'" :item="item"> </food>
            <medicine v-if="item.type == 'medicine'" :item="item"> </medicine>
            </div>
        </li>
        </div>
    </section>
</template>


<script>
    Vue.directive('systolic-level', function(el, binding) {  
    return binding.value>120 ? el.style="color: #FF7043;" : el.style="color: #4CAF50;"
    })

    Vue.directive('diastolic-level', function(el, binding) {  
    return binding.value>80 ? el.style="color: #FF7043;" : el.style="color: #4CAF50;"
    })

    Vue.directive('bgl-level', function(el, binding) {  
    return binding.value>7 ? el.style="color: #FF7043;" : el.style="color: #4CAF50;"
    })

    Vue.component('blood-glucose-level',{
    template:'#bgl',
    props:['item'], 
    })
    Vue.component('blood-pressure',{
    template:'#bp',
    props:['item'], 
    })
    Vue.component('food',{
    template:'#food',
    props:['item'], 
    })
    Vue.component('medicine',{
    template:'#medicine',
    props:['item'], 
    })

    new Vue({
    
    el: '#app',
    
    data() {
        return {
        items: [
        { type: 'bgl', entryTime: '12:31 AM', value: '5.3'},
        { type: 'bp', entryTime: '12:48 AM', systolic: '122', diastolic: '80', pulse: '87/min'},
        { type:'medicine', entryTime: '7:45 AM', value: 'Thyroxin'},
        { type: 'food', entryTime: '9:42 AM', value: 'Small Vanilla Latte' },
        { type: 'food', entryTime: '11:06 AM', value: '1 Banana' },
        { type:'medicine', entryTime: '11:50 AM', value: 'Metformin 500 x 2'},
        { type: 'food', entryTime: '1:28 PM', value: 'Small lunch box of Upma' },
        { type: 'bgl', entryTime: '3:30 PM', value: '8.1'}
        ]
        };
    }            
    })

    export default Vue;
</script>





<style scoped>


#app {  
  margin-left: 50px;
  font-family: 'Open Sans', sans-serif;
  color: #607D8B; 
}
li { 
  list-style: none; 
  border-left: 1px dotted;
  height: 100%;
}
li:last-child {
  border: none;
}
.entry-time {
  margin-left: -32px;  
  width: 60px;
  height: 60px;
  border-radius: 50%;
  text-align: center;
  font-size: 11px;
  line-height: 60px;  
  border: 2px solid;
  background-color: white;
}
.reading-title {
  left: 40px;
  position: relative;
  top: -40px;
  text-transform: uppercase;
  opacity: 0.7;
  font-size: 12px;
}
.details {
  margin-left: 30px;
  margin-top: -30px;  
  width: 50%; 
  padding: 10px;
  border-radius: 5px;  
}
/* 
.bgl { color: #673AB7; }
.bp { color: #9C27B0; }
.food { color: #4CAF50; }
.medicine { color: #2196F3; }
*/


</style>

