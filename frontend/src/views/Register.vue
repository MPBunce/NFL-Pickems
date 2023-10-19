<script setup>
    import { ref } from 'vue';
    import router from '../router'

    const formData = ref({
        username: '',
        email: '',
        password: '', // Add this line for the password
        passwordCheck: '' // Add this line for the passwordCheck
    });

    const submitForm = (e) => {

        e.preventDefault(); // Prevent the default form submission behavior

        if (formData.value.password !== formData.value.passwordCheck) {
            console.log("Passwords don't match");
            return;
        }

        console.log('Form submitted with data:', formData.value);

        formData.value.username = ''        
        formData.value.email = ''    
        formData.value.password = ''
        formData.value.passwordCheck= ''

        router.push({name: 'Login'})

    };

</script>


<template>

    <div class="flex flex-col items-center justify-center px-6 py-4 mx-auto md:h-screen lg:py-0">

        <div class="w-full bg-white rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0 dark:bg-gray-800 dark:border-gray-700">
            <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
                <h1 class="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white">
                    Sign in to your account
                </h1>

                <form class="space-y-4 md:space-y-6" @submit="submitForm">

                    <div>
                        <label class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Your username</label>
                        <input v-model="formData.username" class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="username" required="">
                    </div>
                    <div>
                        <label for="email" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Your Email</label>
                        <input v-model="formData.email" type="email" name="email" id="email" placeholder="email@email.com" class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" required="">
                    </div>
                    <div>
                        <label for="password" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Password</label>
                        <input v-model="formData.password" placeholder="••••••••" class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" required="">
                    </div>
                    <div>
                        <label for="password" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Confirm Password</label>
                        <input v-model="formData.passwordCheck"  placeholder="••••••••" class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" required="">
                    </div>
                    <button type="submit" class="w-full text-white bg-primary-600 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800">Register</button>
                    <p class="text-sm font-light text-gray-500 dark:text-gray-400">
                        Already have an account? <router-link to="/Login" class="underline decoration-white text-white">Login</router-link>
                    </p>

                </form>

            </div>
        </div>
    </div>

</template>

<style scoped>

</style>
