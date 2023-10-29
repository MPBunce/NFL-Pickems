import { createRouter, createWebHistory } from 'vue-router'
import { authStore } from '../store/authStore.js'

//Views
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'
import LeaderBoard from '../views/Leaderboard.vue'

import About from '../views/About.vue'
import SeasonPicks from '../views/SeasonPicks.vue'
import SeasonStandings from '../views/SeasonStandings.vue'
import PlayoffsPicks from '../views/PlayoffsPicks.vue'

const routes = [
    {
        path: '/',
        name: 'About',
        component: About
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
    {
        path: '/SeasonStandings',
        name: 'SeasonStandings',
        component: SeasonStandings
    },
    {
        path: '/SeasonPicks',
        name: 'SeasonPicks',
        component: SeasonPicks
    },
    {
        path: '/PlayoffsPicks',
        name: 'PlayoffsPicks',
        component: PlayoffsPicks
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
    } else if (isAuthenticated === null && to.name === 'SeasonPicks') {
        next({ name: 'Login' })
    } else if (isAuthenticated === null && to.name === 'PlayoffsPicks') {
        next({ name: 'Login' })
    } else {
        next()
    }

})


export default router