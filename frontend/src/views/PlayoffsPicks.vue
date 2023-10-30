<script setup>
    import Navbar from '../components/Navbar.vue';
    import { authStore } from '../store/authStore.js'
    import { ref } from 'vue';
    import router from '../router'

    const auth = authStore();


</script>


<template>

    <Navbar/>

    <div class="flex flex-col items-center justify-center px-6 py-4 mx-auto  ">

        <div class="w-full text-white bg-neutral-800 rounded">
            <div class="p-6 space-y-4 ">
                playoff pics
            </div>
        </div>

    </div>


</template>
