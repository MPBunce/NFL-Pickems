import { defineStore } from 'pinia'
import { authStore } from './authStore'
import axios from "axios"

//Prod
const base_url = 'https://nmpymrjsvh.us-east-1.awsapprunner.com'
//Dev
//const base_url = 'http://127.0.0.1:8080'
const this_year = 2023

export const nflStore = defineStore('nflStore', {
    state: () => {
        return { 
            standings: localStorage.getItem('nflStandings') ? JSON.parse(localStorage.getItem('nflStandings')) : null
        }
    },
    actions: {
        async getStandings(){ 

            const auth = authStore()
            const bearerToken = auth.token

            var res

            const headers = {
                'Authorization': `Bearer ${bearerToken}`,
            };
            
            try {

                res = await axios.get(`${base_url}/api/seasons/?year=${this_year}`, {headers});
                console.log(res.data)
                this.standings = res.data;
                localStorage.setItem('nflStandings', JSON.stringify(res.data));

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