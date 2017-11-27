import DataGraph from 'neutron-graph';

import local_store from './storage';
import store from './store';

export function data_graph () {
  var http = axios_instance();
  return DataGraph('/data-graph', {http: http})();
}

export function rest_api () {
  return axios_instance();
}

export function axios_instance () {
  var data = local_store.check_jwt();
  var jwt = data.jwt || 'none';
  
  var instance = axios.create({
    baseURL: `${SETTINGS.BASE_URL}`,
    timeout: 20000,
    headers: {'Authorization': 'Bearer ' +  jwt},
    transformRequest: [function (data, headers) {
      store.commit('start_ajax');
      return axios.defaults.transformRequest[0](data, headers);
    }],
    transformResponse: [function (data) {
      store.commit('stop_ajax');
      return axios.defaults.transformResponse[0](data);
    }],
  });
  
  return instance;
}

export default data_graph;
