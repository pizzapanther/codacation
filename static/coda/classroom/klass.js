import Vue from 'vue';

import DataGraph from '../services/graph_api';
import store from '../services/store';

var Klass = Vue.component('my-class', {
  template: '#tpl-classroom-klass',
  props: ['id'],
  data() {
    return {
      title: 'Class',
      klass: null
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
        filters: {id: this.id},
        attributes: ['id', 'name', 'inviteCode', 'isAdmin']
      };
      
      DataGraph().all(q).submit()
        .then((response) => {
          this.klass = response.data.myClasses.nodes()[0];
          store.commit('set_title', this.klass.name);
          
        })
        .catch(function (e) {
          console.error(e);
          alert("Error fetching class.");
        });
    }
  }
});

export default Klass;
