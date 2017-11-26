import Vue from 'vue';

import DataGraph from '../services/graph_api';
import AuthRequired from '../mixins/auth-required';

var JoinClass = Vue.component('class-join', {
  template: '#tpl-classroom-join-class',
  mixins: [AuthRequired],
  data() {
    return {
      title: "Join Class"
    };
  }
});

export default JoinClass;
