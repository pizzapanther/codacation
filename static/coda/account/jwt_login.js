import Vue from 'vue';

var JWTLogin = Vue.component('jwt-login', {
  template: '#tpl-account-jwt_login',
  data() {
    console.log('JWT');
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
      console.log(this.$route.params[0]);
    }
  }
});

export default JWTLogin;