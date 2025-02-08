import { defineStore } from 'pinia'
import {nflStore} from './nflStore'
import { picksStore } from './picksStore'

export const authStore = defineStore('authStore', {
    state: () => {
        return { 
            token: localStorage.getItem('token') ? JSON.parse(localStorage.getItem('token')) : null
        }
    },
    actions: {
        setToken (new_token) {
            try {
                this.token = new_token;
                localStorage.setItem('token', JSON.stringify(new_token));

            } catch (error) {
                console.log(error);
            }
        },
        logout(){

            const picksInstance = picksStore()
            const nflInstance = nflStore() 
            picksInstance.picks = null
            nflInstance.standings = null
            this.token = null
            localStorage.removeItem('token');
            localStorage.removeItem('picks');

        }
    }
})