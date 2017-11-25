import Vuex from 'vuex';

const store = new Vuex.Store({
  state: {
    loading: false,
    title: 'Codacation \u22C5 Coding Education via Git Workflows'
  },
  mutations: {
    set_title (state, title) {
      console.log(title);
      if (title) {
        title += ' \u22C5 Codacation';
      } else {
        title = 'Codacation \u22C5 Coding Education via Git Workflows';
      }
      
      state.title = title;
      document.title = title;
    },
    
    start_ajax (state) {
      state.loading = true;
    },
    
    stop_ajax (state) {
      state.loading = false;
    }
  }
});

export default store;
