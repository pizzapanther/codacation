import jwtDecode from 'jwt-decode';

class LocalStorage {
  constructor () {
    try {
      localStorage.setItem('test', 1);
      this.storage = localStorage;
      this.type = 'local';
    } catch (e) {
      // only temporary storage for private modes
      this.storage = {};
      this.type = 'temp';
    }
  }
  
  setJwt(value) {
    this.setItem('jwt', value);
  }
  
  setItem(key, value) {
    this.storage[key] = JSON.stringify(value);
  }
  
  getItem(key) {
    var value = this.storage[key];
    
    if (value) {
      value = JSON.parse(value);
    }
    
    return value;
  }
  
  removeItem(key) {
    if (this.type == 'temp') {
      delete this.storage[key];
    } else {
      this.storage.removeItem(key);
    }
  }
  
  clear() {
    if (this.type == 'temp') {
      this.storage = {};
    } else {
      this.storage.clear();
    }
  }
  
  check_jwt(jwt) {
    if (!jwt) {
      jwt = this.getItem('jwt');
    }
    
    if (jwt) {
      var data = jwtDecode(jwt);
      if (data.exp * 1000 > Date.now()) {
        return {payload: data, jwt: jwt};
      }
    }
    
    return false;
  }
}

var local_store = new LocalStorage();

export default local_store;
