import { defineStore } from 'pinia'
import axios from "axios"

const base_url = 'https://nmpymrjsvh.us-east-1.awsapprunner.com'

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

                console.log(res)

                const new_token = res.data.access_token;
                this.token = new_token;
                localStorage.setItem('token', JSON.stringify(new_token));

            } catch (error) {
                console.log(error);
            }
        },
        logout(){
            this.token = null
            localStorage.removeItem('token');

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