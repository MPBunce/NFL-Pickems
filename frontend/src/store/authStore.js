import { defineStore } from 'pinia'
import axios from "axios"

import {nflStore} from './nflStore'
import { picksStore } from './picksStore'

//Prod
const base_url = 'https://nmpymrjsvh.us-east-1.awsapprunner.com'
//Dev
//const base_url = 'http://127.0.0.1:8080'

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
        async login(input_username, input_password) {

            const form_data = {
                username: input_username, 
                password: input_password, 
            };

            try {
                const res = await axios.post(`${base_url}/api/auth/login`, form_data, {headers: {
                    "Content-Type": "multipart/form-data"}
                });

                const new_token = res.data.access_token;
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
            localStorage.removeItem('nflStandings');

        },
        async register(input_username, input_email, input_password) {

            const form_data = {
                username: input_username, 
                email: input_email,
                password: input_password, 
            };

            try {
                const res = await axios.post(`${base_url}/api/auth/register`, form_data, {headers: 
                    {
                        "Content-Type": "application/json"
                    }
                });

                console.log(res)

            } catch (error) {
                console.log(error);
            }

            try{
                const login_res = await this.login(input_username, input_password)
            }catch (error) {
                console.log(error);
            }

            
        }

    }
})