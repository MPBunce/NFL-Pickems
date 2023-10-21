import { defineStore } from 'pinia'
import { authStore } from './authStore'
import axios from "axios"

const base_url = 'https://nmpymrjsvh.us-east-1.awsapprunner.com'
const this_year = 2023

export const picksStore = defineStore('picksStore', {
    state: () => {
        return { 
            picks: localStorage.getItem('picks') ? JSON.parse(localStorage.getItem('picks')) : null
        }
    },
    actions: {
        async getPicks(){ 

            const auth = authStore()
            const bearerToken = auth.token

            const headers = {
                'Authorization': `Bearer ${bearerToken}`,
            };
            
            try {

                const res = await axios.get(`${base_url}/api/get_pickspicks?year=${this_year}`, {headers});
                this.picks = res.data;
                localStorage.setItem('picks', JSON.stringify(res.data));

            } catch (error) {
                // Check if the error contains a response object with data
                if (error.response && error.response.data) {
                    // Log the error data
                    console.log("Error data:", error.response.data.detail);
                    //handle exp token
                    if(error.response.data.detail.trim() === "Token has expired"){
                        return "Token"
                    }

                } else {
                    // If there's no response or data, log the generic error message
                    console.log("Error:", error.message);
                }
            }
            
            return res.data
        },
    }
})