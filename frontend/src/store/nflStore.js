import { defineStore } from 'pinia'
import { authStore } from './authStore'
import axios from "axios"

//Prod
//const base_url = 'https://nmpymrjsvh.us-east-1.awsapprunner.com'
//Dev
const base_url = 'http://localhost:4000'

const this_year = 2024

export const nflStore = defineStore('nflStore', {
    state: () => {
        return { 
            standings: localStorage.getItem('nflStandings') ? JSON.parse(localStorage.getItem('nflStandings')) : null
        }
    },
    actions: {
        async getStandings(){ 
            var res
            try {
                res = await axios.get(`${base_url}/v1/seasons/${this_year}`);
                this.standings = res.data.teams;
                localStorage.setItem('nflStandings', JSON.stringify(res.data));
            } catch (error) {
                console.log("Error:", error.message);
            }
            return res.data.teams
        },
    }
})