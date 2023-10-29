<script setup>
    import Navbar from '../components/Navbar.vue';
    import { authStore } from '../store/authStore.js'
    import { ref } from 'vue';
    import router from '../router'

    const auth = authStore();


</script>


<template>

    <Navbar/>

    <div class="flex flex-col items-center justify-center px-6 py-4 mx-auto md:h-screen lg:py-0 ">

        <div class="w-full bg-neutral-800 md:mt-0 sm:max-w-md xl:p-0 text-white bg-neutral-800 rounded">
            <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
                    Aboutr
            </div>
        </div>

    </div>

</template>
