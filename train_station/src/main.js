// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import Router from 'vue-router'
import index from './components/index'
import result from './components/result'
import VueResource from 'vue-resource'

Vue.config.productionTip = false;
Vue.use(Router);
Vue.use(VueResource);

const routes = [
    {path:"/",name:"index",component:index},
    {path:"/result",name:"result",component:result}
];

const router = new Router({
    routes,
    mode:"history"
})

/* eslint-disable no-new */
new Vue({
    el: '#app',
    router,
    components: { App },
    template: '<App/>'
});
