import Vue from 'vue';
import VueRouter from 'vue-router';
import VueMaterial from 'vue-material';

import router from './routes';

Vue.use(VueRouter);
Vue.use(VueMaterial);

Vue.material.registerTheme('default', {
  primary: 'cyan',
  accent: 'brown',
  warn: 'red',
  background: 'white'
});

var app = new Vue({
  router: router,
  data() {
    return {
      
    };
  },
  created: function () {
    console.log('created App');
  },
  methods: {
    
  }
});

app.$mount('#app');
