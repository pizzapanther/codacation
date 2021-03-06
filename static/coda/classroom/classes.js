import Vue from 'vue';

import DataGraph from '../services/graph_api';
import AuthRequired from '../mixins/auth-required';

var Classes = Vue.component('my-classes', {
  template: '#tpl-classroom-classes',
  mixins: [AuthRequired],
  data() {
    console.log('classes');
    return {
      title: 'My Classes',
      classes: []
    };
  },
  watch: {'$route': 'init'},
  created() {
    this.init();
  },
  methods: {
    init() {
      var q = {
        node: 'myClasses',
        attributes: ['id', 'name', 'inviteCode', 'isAdmin']
      };
      
      DataGraph().all(q).submit()
        .then((response) => {
          this.classes = response.data.myClasses.nodes();
        })
        .catch(function () {
          alert("Error fetching classes.");
        });
    }
  }
});

export default Classes;
