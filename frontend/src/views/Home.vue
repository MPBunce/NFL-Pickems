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
        const result = await picksStoreInstance.getPicks();
        user_picks.value = result;

    });


</script>

<template>
    <Navbar/>

    <div>
        <h1>User Picks</h1>
        <div v-for="division in user_picks" :key="division.team_division">
            <h2>{{ division.team_division }}</h2>
            <ul>
                <li>
                    {{ division.team_name }} {{ division.division_position}} 
                </li>
            </ul>
        </div>
    </div>

</template>

