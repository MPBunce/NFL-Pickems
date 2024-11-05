<script setup>

    import Navbar from '../components/Navbar.vue';
    import GoogleLogin from '../components/GoogleLogin.vue';

</script>


<template>

    <Navbar/>

    <div class="flex flex-col items-center justify-center px-6 mx-auto lg:py-0">

        <div class="w-full bg-neutral-800 mt-10 sm:max-w-md xl:p-0 bg-neutral-800 mt-48 rounded-2xl">
            <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
                <h1 class="text-xl font-bold leading-tight text-center tracking-tight text-gray-900 md:text-2xl dark:text-white">
                    Login With Google Auth!
                </h1>
                <div class="flex justify-center items-center h-24">
                    <GoogleLogin/>                    
                </div>
            </div>
        </div>
    </div>

</template>
