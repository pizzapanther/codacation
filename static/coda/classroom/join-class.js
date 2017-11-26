import Vue from 'vue';

import DataGraph from '../services/graph_api';
import AuthRequired from '../mixins/auth-required';

var JoinClass = Vue.component('class-join', {
  template: '#tpl-classroom-join-class',
  mixins: [AuthRequired],
  data() {
    return {
      title: "Join Class",
      form_data: null
    };
  },
  watch: {'$route': 'init'},
  created() {
    this.init();
  },
  methods: {
    submit() {
      var m = {
        node: 'joinClass',
        input: this.form_data,
        attributes: ['redirectTo']
      };
      
      DataGraph().mutate(m).submit()
        .then((response) => {
          if (response.data.joinClass.data) {
            console.log(response.data.joinClass.data.redirectTo);
            var id = btoa('KlassNode:' + response.data.joinClass.data.redirectTo);
            this.$router.push(`/classes/${id}`);
          } else {
            alert("Invalid Invite Code.");
          }
          
        })
        .catch(function (e) {
          console.error(e);
          alert("Error joining class.");
        });
    },
    init() {
      var q = {
        node: 'myInfo',
        attributes: ['id', 'firstName', 'lastName', 'email']
      };
      
      DataGraph().all(q).submit()
        .then((response) => {
          var data = response.data.myInfo.nodes()[0];
          this.form_data = {
            firstName: data.firstName,
            lastName: data.lastName,
            email: data.email,
            inviteCode: ''
          };
        })
        .catch(function (e) {
          console.error(e);
          alert("Error fetching your info.");
        });
    }
  }
});

export default JoinClass;
