import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'

import { authStore } from '../store/authStore.js'

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/Login',
        name: 'Login',
        component: Login
    },
    {
        path: '/Register',
        name: 'Register',
        component: Register
    },
]

const router = createRouter({
    history: createWebHistory('/'),
    routes
})


router.beforeEach((to, from, next) => {

    const auth = authStore();
    const isAuthenticated = auth.token

    console.log(isAuthenticated)

    if (isAuthenticated !== null && to.name === 'Register') {
        console.log("1" + isAuthenticated)
        next({ name: 'Home' })
    } else if (isAuthenticated !== null && to.name === 'Login') {
        console.log("2" +isAuthenticated)
        next({ name: 'Home' })
    } else if (isAuthenticated === null && to.name === 'Home') {
        console.log("3" +isAuthenticated)
        next({ name: 'Login' })
    } else {
        next()
    }

})



export default router