import Vue from 'vue'
import App from './App.vue'
import router from './router'

Vue.config.productionTip = false
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';


Vue.use(ElementUI);

import Axios from 'axios'
// 数据请求模块
Vue.use(Axios.axios)

new Vue({
    router,
    render: h => h(App)
}).$mount('#app')
