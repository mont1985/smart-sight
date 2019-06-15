import Vue from 'vue'
import Vuex from 'vuex'
import App from './App.vue'
import router from './router'
import './registerServiceWorker'
import ArgonDashboard from './plugins/argon-dashboard'

Vue.config.productionTip = false
Vue.use(Vuex)
Vue.use(ArgonDashboard)


const store = new Vuex.Store({
  state: {
      token: '',
      user: {
          pk: 1,
          username: 'goose',
          email: '',           
          name: ''
        }
      }
  },
)

new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')
