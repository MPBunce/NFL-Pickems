<script setup>
    import Navbar from '../components/Navbar.vue';
    import { authStore } from '../store/authStore.js'
    import { ref } from 'vue';
    import router from '../router'

    const auth = authStore();


</script>


<template>

    <Navbar/>

    <div class="flex flex-col items-center justify-center px-8 py-8 mx-auto">
        <div class="w-full text-white bg-neutral-800 rounded">
            <div class="p-6 space-y-4 text-center text-2xl">
                <h1>About This Application</h1>
            </div>
            <div class="p-6 space-y-2">
                NFL Pickems is a prediction game that allows you to forecast divisional standings in all eight NFL conferences and make playoff predictions!
            </div>

            <h2 class="p-6 space-y-4">How to Use the App:</h2>            
            <div class="ml-6">
                <ol>

                    <li class="mt-4 font-bold"><a class="border-b-2">Phase 1 - Pre-Season Predictions</a></li>
                    <p class="my-2">Before the NFL season begins, you can make your regular season picks. Here's how:</p>
                    <ul class="sm:ml-20">
                        <li>- Create an account if you don't have one!</li>
                        <li>- Login and access the Season Picks section.</li>
                        <li>- Predict the divisional standings for all eight NFL conferences based on your football knowledge and insights.</li>
                        <li>- Lock in your selections to submit your pre-season predictions!</li>
                        <li>- Follow along and see how the season shakes out in the NFL Standings tab.</li>
                    </ul>

                    <li class="mt-4 font-bold"><a class="border-b-2">Phase 2 - Playoff Predictions</a></li>
                    <p class="my-2">Once the regular season ends, it's time to predict the playoff outcomes:</p>
                    <ul class="sm:ml-20">
                        <li>- Login and navigate to the Playoff Picks section.</li>
                        <li>- Make your predictions for which teams will advance and ultimately emerged as the Super Bowl champion.</li>
                        <li>- Submit your playoff predictions to complete Phase 2.</li>
                    </ul>

                    <li class="mt-4 font-bold"><a class="border-b-2">Scoring and Leaderboard</a></li>
                    <p class="my-2">Stay engaged and competitive with our scoring system and leaderboard:</p>
                    <ul class="sm:ml-20">
                        <li>- For each correct prediction you make, you will earn a point.</li>
                        <li>- Track your total score and see how your predictions stack up against others in the leaderboard tab.</li>
                    </ul>

                </ol>
            </div>
            <p class="p-6 space-y-4 mt-8">
                Feel free to contribute to the project on <a class="underline" href="https://github.com/MPBunce/NFL-Pickems">GitHub</a>. This app was developed using Python, FastAPI, and PostgreSQL on the backend and Vue.js and TailwindCSS for the frontend. AWS was used for hosting.
            </p>
        </div>
    </div>



</template>
