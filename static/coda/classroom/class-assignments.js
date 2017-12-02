import Vue from 'vue';

import { DateTime } from 'luxon';

var ClassAssignments = Vue.component('class-assignments', {
  template: '#tpl-classroom-class-assignments',
  props: ['assignments'],
  data() {
    return {
      
    };
  },
  methods: {
    created(ts) {
      return DateTime
        .fromISO(ts)
        .toLocaleString(DateTime.DATE_MED);
    }
  }
});

export default ClassAssignments;
