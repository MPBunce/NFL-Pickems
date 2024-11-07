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

            var res
            const auth = authStore()
            const bearerToken = auth.token

            const headers = {
                'Authorization': `Bearer ${bearerToken}`,
            };

            try {
                res = await axios.get(`${base_url}/v1/get/picks/${this_year}`, {headers});
                console.log(res.data)
                this.picks = res.data.picks;
                localStorage.setItem('picks', JSON.stringify(res.data.picks));                    
            } catch (error) {
                console.log("Error:", error.message);
                this.picks = []
                return
            }

            return res.data.picks

        },
        async lockInPicks(picks_array){
            
            const auth = authStore()
            const bearerToken = auth.token

            var res

            const headers = {
                'Authorization': `Bearer ${bearerToken}`,
            };
            
            try{
                res = await axios.post(`${base_url}/v1/lockin/picks/${this_year}`, picks_array, {headers})
            
                this.picks = picks_array
                localStorage.setItem('picks', JSON.stringify(picks_array));
            } catch (error){
                console.log(error);
            }

            return "locked in fr fr"

        }
    }
})