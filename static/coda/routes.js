import Vue from 'vue';
import VueRouter from 'vue-router';

import Home from './home';
import JWTLogin from './account/jwt_login';

const NotFound = {template: '#tpl-404'};

export const routes = [
  {path: '/login/next/*', name: 'jwt-login', component: JWTLogin},
  {path: '/', component: Home},
  {path: '*', component: NotFound}
];

const router = new VueRouter({
  mode: 'history',
  routes: routes,
  scrollBehavior: function(to, from, savedPosition) {
    return savedPosition || {x: 0, y: 0};
  }
});

router.set_title = (to) => {
  var title = '';
  
  if (typeof(to) == 'string') {
    title = to;
  } else if (to.matched[0] && to.matched[0].instances && to.matched[0].instances.default) {
    if (to.matched[0].instances.default.title) {
      title = to.matched[0].instances.default.title;
    }
  }
  
  if (title) {
    title += ' \u22C5 Codacation';
  } else {
    title = 'Codacation \u22C5 Coding Education via Git Workflows';
  }
  
  document.title = title;
};

router.afterEach((to, from) => {
  Vue.nextTick(() => {
    router.set_title(to);
  });
});

export default router;
