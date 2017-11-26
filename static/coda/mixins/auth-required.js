import auth from '../services/auth';

var AuthRequired = {
  beforeRouteEnter (to, from, next) {
    if (auth.is_authed()) {
      next();
    } else {
      var param = encodeURIComponent('/login/next' + to.fullPath);
      location.href = '/auth/login/github/?next=' + param;
    }
  }
};

export default AuthRequired;
