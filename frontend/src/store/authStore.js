import { defineStore } from 'pinia'
import axios from "axios"

import {nflStore} from './nflStore'
import { picksStore } from './picksStore'

//Prod
//const base_url = 'https://nmpymrjsvh.us-east-1.awsapprunner.com'
//Dev
const base_url = 'http://127.0.0.1:4000'

export const authStore = defineStore('authStore', {
    state: () => {
        return { 
            token: localStorage.getItem('token') ? JSON.parse(localStorage.getItem('token')) : null
        }
    },
    actions: {
        async test(){ 
            const res = await axios.get(`${base_url}/`);
            return res.data.message;
        },
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