import Vue from 'vue';
import tableComponent from './components/table-component.vue';
console.log(tableComponent);

Vue.component('table-component', tableComponent);

new Vue({
    el: '#app',
    components: {
      tableComponent
    }
  })