import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { createPinia } from 'pinia'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.min.js'
import 'bootstrap-icons/font/bootstrap-icons.css'
import BootstrapIcon from '@dvuckovic/vue3-bootstrap-icons'; 


const app = createApp(App)
app.use(createPinia())
app.use(router)
app.mount('#app')
