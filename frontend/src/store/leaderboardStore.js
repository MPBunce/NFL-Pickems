import { defineStore } from 'pinia'
import axios from "axios"


//Prod
//const base_url = 'https://nmpymrjsvh.us-east-1.awsapprunner.com'
//Dev
const base_url = 'http://127.0.0.1:4000'
const this_year = 2024


export const leaderboardStore = defineStore('leaderboardStore', {
    state: () => {

        return { 
            leaderboard: localStorage.getItem('leaderboard') ? JSON.parse(localStorage.getItem('leaderboard')) : null
        }

    },
    actions: {
        async getLeaderboard() {



            try {
                const res = await axios.get(`${base_url}/api/leaderboard/?year=${this_year}`)
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