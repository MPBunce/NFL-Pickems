import { defineStore } from 'pinia'
import { authStore } from './authStore'
import axios from "axios"

//Prod
//const base_url = 'https://nmpymrjsvh.us-east-1.awsapprunner.com'
//Dev
const base_url = 'http://localhost:4000'

const this_year = 2024

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
                'Authorization': `Bearer ${bearerToken}`
            };

            console.log(headers)
            try {
                console.log("Working")
                res = await axios.get(`${base_url}/v1/get/picks/${this_year}`, {headers});
                console.log("working?" + res.data)
                this.picks = res.data;
                localStorage.setItem('picks', JSON.stringify(res.data));

            } catch (error) {


                console.log("Error:", error.message);

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