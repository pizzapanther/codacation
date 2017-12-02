import Vue from 'vue';

import { DateTime } from 'luxon';

import DataGraph from '../services/graph_api';
import store from '../services/store';

var Assignment = Vue.component('class-ass', {
  template: '#tpl-classroom-assignment',
  props: ['id'],
  data() {
    return {
      title: 'Assignment',
      ass: null,
      issue: null
    };
  },
  watch: {'$route': 'init'},
  created() {
    this.init();
  },
  computed: {
    created_ts() {
      if (this.ass && this.ass.created) {
        return DateTime
          .fromISO(this.ass.created)
          .toLocaleString(DateTime.DATETIME_MED);
      }
      
      return '';
    },
    issue_url() {
      if (this.ass && this.issue) {
        return this.ass.repoUrl + '/issues/' + this.issue.num;
      }
      
      return '';
    }
  },
  methods: {
    init() {
      var klass = {klass: ['name', 'isAdmin']};
      var issue = {issueSet: {edges: {node: ['num', 'mergeBranch']}}};
      
      var q = {
        node: 'myAssignments',
        filters: {id: this.id},
        attributes: ['id', 'name', 'shortDescription', 'repoUrl', 'created', klass, issue]
      };
      
      DataGraph().query(q).submit()
      .then((response) => {
        this.ass = response.data.myAssignments.nodes()[0];
        this.issue = response.nodes(this.ass.issueSet)[0];
        store.commit('set_title', this.ass.name + ' - ' + this.ass.klass.name);
      })
      .catch(function (e) {
          console.error(e);
          alert("Error fetching assignment.");
        });
    }
  }
});

export default Assignment;
