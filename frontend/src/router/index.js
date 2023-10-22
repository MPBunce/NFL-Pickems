import { createRouter, createWebHistory } from 'vue-router'
import { authStore } from '../store/authStore.js'

//Views
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'
import LeaderBoard from '../views/Leaderboard.vue'



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
    {
        path: '/Leaderboard',
        name: 'LeaderBoard',
        component: LeaderBoard
    },

]

const router = createRouter({
    history: createWebHistory('/'),
    routes
})


router.beforeEach((to, from, next) => {

    const auth = authStore();
    const isAuthenticated = auth.token

    if (isAuthenticated !== null && to.name === 'Register') {
        next({ name: 'Home' })
    } else if (isAuthenticated !== null && to.name === 'Login') {
        next({ name: 'Home' })
    } else if (isAuthenticated === null && to.name === 'Home') {
        next({ name: 'Login' })
    } else {
        next()
    }

})


export default router