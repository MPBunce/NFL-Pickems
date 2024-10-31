import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import './index.css'
import router from './router'
import GoogleSignInPlugin from "vue3-google-signin"

const myClientId = import.meta.env.VITE_GOOGLE_CLIENT_ID;
const pinia = createPinia()

console.log(myClientId)

createApp(App)
    .use(router)
    .use(pinia)
    .use(GoogleSignInPlugin, {
        clientId: myClientId,
    })
    .mount('#app')
