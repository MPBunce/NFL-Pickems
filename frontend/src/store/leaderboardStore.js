import { defineStore } from 'pinia'
import axios from "axios"

const base_url = import.meta.env.VITE_API_URL;
const this_year = import.meta.env.VITE_YEAR;

export const leaderboardStore = defineStore('leaderboardStore', {
    state: () => {

        return { 
            leaderboard: localStorage.getItem('leaderboard') ? JSON.parse(localStorage.getItem('leaderboard')) : null
        }

    },
    actions: {
        async getLeaderboard() {


            try {
                console.log(`${base_url}v1/leaderboard/${this_year}`)
                const res = await axios.get(`${base_url}v1/leaderboard/${this_year}`)
                console.log(res)
                this.leaderboard = res.data
                localStorage.setItem('leaderboard', JSON.stringify(res.data));
                return res.data

            } catch (error) {
                console.log(error);
            }

            
        }
    }
})