import Vue from 'vue';

import DataGraph from '../services/graph_api';

var JoinClass = Vue.component('class-join', {
  template: '#tpl-classroom-join-class',
  data() {
    return {
      title: "Join Class"
    };
  }
});

export default JoinClass;
