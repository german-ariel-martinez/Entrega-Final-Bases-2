import Vue from 'vue'
import './plugins/axios'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify'
import Toolbar from './components/Toolbar'
import '@mdi/font/css/materialdesignicons.css'
import axios from "axios"
import DatetimePicker from 'vuetify-datetime-picker'
 
Vue.use(DatetimePicker)
Vue.config.productionTip = false

// Componentes que queremos que sean globales:
Vue.component('Toolbar', Toolbar);

// Para axios
axios.defaults.withCredentials = true;
axios.defaults.baseURL = 'http://localhost:8000/';  // the FastAPI backend

// Bus de notifiaciones
export const logInBus = new Vue();

new Vue({
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app')
