<script setup>

    import router from '../router';
    import { authStore } from '../store/authStore';
    import { ref, onMounted } from 'vue';

    const auth = authStore();

    const toggleNav = () => {
        const navContent = document.getElementById('nav-content');
        if (navContent) {
            navContent.classList.toggle('hidden');
        }
    };

    onMounted(() => {
        const navToggle = document.getElementById('nav-toggle');
        if (navToggle) {
            navToggle.onclick = toggleNav;
        }
    });

    const logout = () => {
        console.log("logout")
        auth.logout()
        router.push('/Login')
    }

</script>

<template>

    <div class="bg-gray-400 font-sans leading-normal tracking-normal">
        <nav class="flex items-center justify-between flex-wrap bg-neutral-800 p-6 fixed w-full z-10 top-0">
            <div class="flex items-center flex-shrink-0 text-white mr-6">
                <a class="text-white no-underline hover:text-white hover:no-underline" href="#">
                    <span class="text-2xl pl-2 flex flex-row">

                        <a class="inline-block ">
                            <router-link to="/" class="decoration-white text-white flex flex-row text-center">
                                <img class="w-10 mx-2" src="../assets/NFL.png">
                                <a class="pl-2 mt-2">NFL Pickems</a>                                    
                            </router-link>
                        </a>


                    </span>
                </a>
            </div>

            <div class="block lg:hidden">
                <button id="nav-toggle" class="flex items-center px-3 py-2 border rounded text-gray-500 border-gray-600 hover:text-white hover:border-white">
                    <svg class="fill-current h-3 w-3" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><title>Menu</title><path d="M0 3h20v2H0V3zm0 6h20v2H0V9zm0 6h20v2H0v-2z"/></svg>
                </button>
            </div>

            <div class="w-full flex-grow lg:flex lg:items-center lg:w-auto hidden lg:block pt-6 lg:pt-0" id="nav-content">
                <ul class="list-reset lg:flex justify-end flex-1 items-center">

                    <li class="mr-3 hover:border-l-2 lg:hover:border-l-0 lg:hover:border-b-2" v-if="!auth.token">
                        <a class="inline-block py-2 px-4">
                            <router-link to="/Login" :class="{'font-bold': $route.name === 'Login'}" class="text-white">Login</router-link>
                        </a>
                    </li>
                    <!-- <li class="mr-3 hover:border-l-2 lg:hover:border-l-0 lg:hover:border-b-2" v-if="!auth.token">
                        <a class="inline-block py-2 px-4">
                            <router-link to="/Register" :class="{'font-bold': $route.name === 'Register'}" class="text-white">Register</router-link>
                        </a>
                    </li> -->
                    <li class="mr-3 hover:border-l-2 lg:hover:border-l-0 lg:hover:border-b-2" v-if="auth.token">
                        <a class="inline-block py-2 px-4">
                            <router-link to="/SeasonPicks" :class="{'font-bold': $route.name === 'SeasonPicks'}" class="text-white">Season Picks</router-link>
                        </a>
                    </li>
                    <!-- <li class="mr-3 hover:border-l-2 lg:hover:border-l-0 lg:hover:border-b-2" v-if="auth.token">
                        <a class="inline-block py-2 px-4">
                            <router-link to="/PlayoffsPicks" :class="{'font-bold': $route.name === 'PlayoffsPicks'}" class=" text-white">Playoff Picks</router-link>
                        </a>
                    </li> -->
                    <li class="mr-3 hover:border-l-2 lg:hover:border-l-0 lg:hover:border-b-2">
                        <a class="inline-block py-2 px-4">
                            <router-link to="/SeasonStandings" :class="{'font-bold': $route.name === 'SeasonStandings'}" class="text-white">NFL Standings</router-link>
                        </a>
                    </li>
                    <li class="mr-3 hover:border-l-2 lg:hover:border-l-0 lg:hover:border-b-2">
                        <a class="inline-block py-2 px-4">
                            <router-link to="/Leaderboard" :class="{'font-bold': $route.name === 'LeaderBoard'}" class="text-white">Picks Leaderboard</router-link>
                        </a>
                    </li>

                    <li class="mr-16  rounded cursor max-w-10 text-center" v-if="auth.token">
                        <button @click="logout" class="bg-blue-700 hover:bg-blue-500 text-white font-bold py-2 px-4 rounded-full">
                            <a  class="text-white">Logout</a>
                        </button>
                    </li>
                </ul>
            </div>
        </nav>

        <!--Container-->
        <div class="container shadow-lg mx-auto bg-white mt-24 md:mt-18">

        </div>
    </div>

</template>