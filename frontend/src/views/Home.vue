<script setup>

    import Navbar from '../components/Navbar.vue';
    import { ref, onMounted } from 'vue';
    import { authStore } from '../store/authStore';
    import { picksStore } from '../store/picksStore';
import router from '../router';

    const authStoreInstance = authStore();
    const picksStoreInstance = picksStore()
    const user_picks = ref(null);
    const res = ref(null);

    onMounted(async () => {
        
        res.value = await authStoreInstance.test();

    });

    const getPicks = async () => {

        res = await picksStoreInstance.getPicks();
        // if(res == "Token"){
        //     authStoreInstance.logout()
        //     router.push('Login')
        // }

        user_picks.value = res  
    }

</script>

<template>
    <Navbar/>
    <div>
      hello home
      <p>{{ res }}</p>
      <p>{{ user_picks }}</p>
    </div>
    <button @click="getPicks">log res</button>
</template>

