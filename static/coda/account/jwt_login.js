import Vue from 'vue';

import DataGraph from '../services/graph_api';
import local_store from '../services/storage';

var JWTLogin = Vue.component('jwt-login', {
  template: '#tpl-account-jwt_login',
  data() {
    return {
      title: "Generating login token"
    };
  },
  watch: {'$route': 'init'},
  created() {
    this.init();
  },
  methods: {
    init() {
      var next_url = '/' + this.$route.params[0];
      var m = {
        node: 'getJwt',
        input: {extra: 'narf'},
        attributes: ['jwt']
      };
      
      DataGraph().mutate(m).submit()
        .then((response) => {
          local_store.setJwt(response.data.getJwt.data.jwt);
          this.$router.push(next_url);
        })
        .catch(function () {
          alert("Error logging in, go back and try again.");
        });
    }
  }
});

export default JWTLogin;