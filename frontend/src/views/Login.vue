<script setup>
    import Navbar from '../components/Navbar.vue';
    import { authStore } from '../store/authStore.js'
    import { ref } from 'vue';
    import router from '../router'

    const auth = authStore();

    const formData = ref({
        username: '',
        password: ''
    });

    const submitForm = async (e) => {
        e.preventDefault(); // Prevent the default form submission behavior
        console.log('Form submitted with data:', formData.value);

        try {
            await auth.login(formData.value.username, formData.value.password);
            router.replace({ name: 'SeasonPicks' });
            // Reset the form fields after a successful login
            formData.value.username = '';
            formData.value.password = '';
        } catch (error) {
            // Handle login errors
            console.error('Login failed:', error);
        }
    };

</script>


<template>

    <Navbar/>

    <div class="flex flex-col items-center justify-center px-6 mx-auto lg:py-0">

        <div class="w-full bg-neutral-800 mt-10 sm:max-w-md xl:p-0 bg-neutral-800 mt-48">
            <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
                <h1 class="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white">
                    Sign in to your account
                </h1>
                <form class="space-y-4 md:space-y-6" action="#" @submit="submitForm">
                    <div>
                        <label class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Your username</label>
                        <input v-model="formData.username" class="bg-neutral-600 text-white sm:text-sm rounded-lg block w-full p-2.5" placeholder="username" required="">
                    </div>
                    <div>
                        <label for="password" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Password</label>
                        <input v-model="formData.password" type="password" name="password" id="password" placeholder="••••••••"  class="bg-neutral-600 text-white sm:text-sm rounded-lg block w-full p-2.5" required="">
                    </div>

                    <button type="submit" class="w-full text-white bg-blue-700 hover:bg-blue-500 rounded px-5 py-2.5 text-center">Sign in</button>
                    <p class="text-sm font-light text-gray-500 dark:text-gray-400">
                        Don’t have an account yet? <router-link to="/Register" class="hover:underline decoration-white text-white">Register</router-link>
                    </p>
                </form>
            </div>
        </div>
    </div>

</template>
