import { defineStore } from 'pinia'
import { authStore } from './authStore'
import axios from "axios"

const base_url = import.meta.env.VITE_API_URL;
const this_year = import.meta.env.VITE_YEAR;

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
                console.log(`${base_url}/v1/seasons/${this_year}`)
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