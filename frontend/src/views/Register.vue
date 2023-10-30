<script setup>
    import { ref } from 'vue';
    import router from '../router'
    import Navbar from '../components/Navbar.vue';
    import { authStore } from '../store/authStore.js'

    const auth = authStore()

    const formData = ref({
        username: '',
        email: '',
        password: '', // Add this line for the password
        passwordCheck: '' // Add this line for the passwordCheck
    });

    const submitForm = async (e) => {

        e.preventDefault(); // Prevent the default form submission behavior

        try{

            if (formData.value.password !== formData.value.passwordCheck) {
                console.log("Passwords don't match");
                return;
            }

            await auth.register(formData.value.username, formData.value.email, formData.value.password)

            formData.value.username = ''        
            formData.value.email = ''    
            formData.value.password = ''
            formData.value.passwordCheck= ''

            router.push({name: 'About'})

        } catch (error) {
            console.log(error)
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

                <form class="space-y-4 md:space-y-6" @submit="submitForm">
                    <div>
                        <label class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Your username</label>
                        <input v-model="formData.username" class="bg-neutral-600 text-white sm:text-sm rounded-lg block w-full p-2.5" placeholder="username" required="">
                    </div>
                    <div>
                        <label for="email" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Your Email</label>
                        <input v-model="formData.email" type="email" name="email" id="email" placeholder="email@email.com"  class="bg-neutral-600 text-white sm:text-sm rounded-lg block w-full p-2.5" required="">
                    </div>
                    <div>
                        <label for="password" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Password</label>
                        <input v-model="formData.password" placeholder="••••••••"  class="bg-neutral-600 text-white sm:text-sm rounded-lg block w-full p-2.5" required="">
                    </div>
                    <div>
                        <label for="password" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Confirm Password</label>
                        <input v-model="formData.passwordCheck"  placeholder="••••••••"  class="bg-neutral-600 text-white sm:text-sm rounded-lg block w-full p-2.5" required="">
                    </div>
                    <button type="submit" class="w-full text-white bg-blue-700 hover:bg-blue-500 rounded px-5 py-2.5 text-center">Register</button>
                    <p class="text-sm font-light text-gray-500 dark:text-gray-400">
                        Already have an account? <router-link to="/Login" class="hover:underline decoration-white text-white">Login</router-link>
                    </p>
                </form>

            </div>
        </div>
    </div>

</template>

<style scoped>

</style>
