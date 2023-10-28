import { defineStore } from 'pinia'
import { authStore } from './authStore'
import axios from "axios"

//Prod
//const base_url = 'https://nmpymrjsvh.us-east-1.awsapprunner.com'
//Dev
const base_url = 'http://127.0.0.1:8080'

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

            var res

            const headers = {
                'Authorization': `Bearer ${bearerToken}`,
            };
            
            try {

                res = await axios.get(`${base_url}/api/get_picks?year=${this_year}`, {headers});
                console.log(res.data)
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
        async lockInPicks(picks_array){
            
            const auth = authStore()
            const bearerToken = auth.token

            var res

            const headers = {
                'Authorization': `Bearer ${bearerToken}`,
            };
            
            try{
                res = await axios.post(`${base_url}/api/lockin_picks`, picks_array, {headers})
            
                this.picks = picks_array
                localStorage.setItem('picks', JSON.stringify(picks_array));
            } catch (error){
                console.log(error);
            }

            return "locked in"

        }
    }
})