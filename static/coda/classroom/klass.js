import Vue from 'vue';

import DataGraph from '../services/graph_api';
import store from '../services/store';

import ClassPeople from './class-people';

var Klass = Vue.component('my-class', {
  template: '#tpl-classroom-klass',
  props: ['id'],
  data() {
    return {
      title: 'Class',
      join_url: SETTINGS.BASE_URL + '/classes/join',
      klass: null,
      students: [],
      admins: []
    };
  },
  watch: {'$route': 'init'},
  created() {
    this.init();
  },
  methods: {
    init() {
      var sub = {
        admins: {
          edges: {
            node: 'id, email, name'
          }
        },
        students: {
          edges: {
            node: 'id, email, name'
          }
        }
      };
      
      var q = {
        node: 'myClasses',
        filters: {id: this.id},
        attributes: ['id', 'name', 'inviteCode', 'isAdmin', sub]
      };
      
      DataGraph().all(q).submit()
        .then((response) => {
          this.klass = response.data.myClasses.nodes()[0];
          store.commit('set_title', this.klass.name);
          this.students = response.nodes(this.klass.students);
          this.admins = response.nodes(this.klass.admins);
        })
        .catch(function (e) {
          console.error(e);
          alert("Error fetching class.");
        });
    }
  }
});

export default Klass;
