<script setup>
    import Navbar from '../components/Navbar.vue';
    import { authStore } from '../store/authStore.js'
    import { ref } from 'vue';
    import GoogleLogin from '../components/GoogleLogin.vue';

    const auth = authStore();

    const formData = ref({
        username: '',
        password: ''
    });

    const submitForm = async (e) => {
        e.preventDefault(); // Prevent the default form submission behavior
        console.log('Form submitted with data:', formData.value);

        // try {
        //     await auth.login(formData.value.username, formData.value.password);
        //     router.replace({ name: 'SeasonPicks' });
        //     // Reset the form fields after a successful login
        //     formData.value.username = '';
        //     formData.value.password = '';
        // } catch (error) {
        //     // Handle login errors
        //     console.error('Login failed:', error);
        // }
    };

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
