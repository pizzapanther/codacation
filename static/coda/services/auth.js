import local_store from './storage';

class Auth {
  logout() {
    local_store.removeItem('jwt');
    this.jwt = null;
  }
  
  is_authed(jwt) {
    var data = local_store.check_jwt(jwt);
    return data;
  }
}

var auth = new Auth();

export default auth;
