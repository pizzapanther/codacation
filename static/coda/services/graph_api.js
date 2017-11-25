import DataGraph from 'neutron-graph';

import local_store from './storage';

export function data_graph () {
  var http = axios_instance();
  return DataGraph('/data-graph', {http: http})();
}

export function axios_instance () {
  var data = local_store.check_jwt();
  var jwt = data.jwt || 'none';
  
  var instance = axios.create({
    baseURL: `${SETTINGS.BASE_URL}`,
    timeout: 20000,
    headers: {'Authorization': 'Bearer ' +  jwt}
  });
  
  return instance;
}

export default data_graph;
