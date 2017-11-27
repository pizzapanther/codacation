import {rest_api} from '../../services/graph_api';
import store from '../../services/store';

function AddAssignmentDialog (parent) {
  var Dialog = {
    template: "#tpl-classroom-dialogs-add-assignment",
    data() {
      return {
        form: {},
        repos: []
      };
    },
    mounted() {
      this.init();
      
      this.$nextTick(() => {
        this.$refs.add_dialog.open();
      });
    },
    computed: {
      loading() {
        return store.state.loading;
      }
    },
    methods: {
      init() {
        var http = rest_api();
        http.get('/gh/repos')
          .then((response) => {
            this.repos = response.data;
          })
          .catch(function (e) {
            console.error(e);
            alert('Error listing repositories.');
          });
      },
      closeDialog() {
        this.$refs.add_dialog.close();
        parent.close_assignment();
      }
    }
  };
  
  return Dialog;
}

export default AddAssignmentDialog;
