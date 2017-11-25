import Vue from 'vue';
import VueRouter from 'vue-router';
import VueMaterial from 'vue-material';
import Vuex from 'vuex';

import router from './routes';
import store from './services/store';

Vue.use(VueRouter);
Vue.use(VueMaterial);
// Vue.use(Vuex);

Vue.material.registerTheme('default', {
  primary: 'cyan',
  accent: 'brown',
  warn: 'red',
  background: 'white'
});

var app = new Vue({
  router: router,
  data() {
    return {};
  },
  computed: {
    loading() {
      return store.state.loading;
    }
  },
  created: function () {
    console.log('created App');
  },
  methods: {
    
  }
});

app.$mount('#app');
