import { defineStore } from 'pinia'
import axios from "axios"

export const authStore = defineStore('authStore', {
    state: () => {
        return { 
            token: localStorage.getItem('token') ? JSON.parse(localStorage.getItem('token')) : null 
        }
    },
    getters: {
        setToken: (state) => {
            return (newToken) => {
                state.token = newToken
                localStorage.setItem('token', JSON.stringify(newToken) )
            }
        },
        removeToken: (state) => {
            state.token = null;
            localStorage.setItem('token', JSON.stringify(null) )
        }
    },
    actions: {

    }
})