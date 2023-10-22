<script setup>

    import Navbar from '../components/Navbar.vue';
    import DivisionCard from '../components/DivisionCard.vue';
    import PicksLockin from '../components/PicksLockin.vue';
    import { ref, onMounted } from 'vue';
    import { authStore } from '../store/authStore';
    import { picksStore } from '../store/picksStore';
    import { nflStore } from '../store/nflStore';

    const displayValue = ref(false);

    const authStoreInstance = authStore();
    const picksStoreInstance = picksStore()
    const user_picks = ref(null);
    const res = ref(null);

    const afcEast = ref(null);
    const afcNorth = ref(null);
    const afcWest = ref(null);
    const afcSouth = ref(null);

    const nfcEast = ref(null);
    const nfcNorth = ref(null);
    const nfcWest = ref(null);
    const nfcSouth = ref(null);

    const nflSeason = nflStore();
    const regularSeason = ref(null);

    const afcEastSeason = ref(null);
    const afcNorthSeason = ref(null);
    const afcWestSeason = ref(null);
    const afcSouthSeason = ref(null);

    const nfcEastSeason = ref(null);
    const nfcNorthSeason = ref(null);
    const nfcWestSeason = ref(null);
    const nfcSouthSeason = ref(null);

    

    onMounted(async () => {
        
        res.value = await authStoreInstance.test();
        const result = await picksStoreInstance.getPicks();
        user_picks.value = result;

        if(user_picks.value){

            //AFC
            afcEast.value = user_picks.value.filter(pick => pick.team_division === 'AFC East');
            afcNorth.value = user_picks.value.filter(pick => pick.team_division === 'AFC North');
            afcWest.value = user_picks.value.filter(pick => pick.team_division === 'AFC West');
            afcSouth.value = user_picks.value.filter(pick => pick.team_division === 'AFC South');

            //NFC
            nfcEast.value = user_picks.value.filter(pick => pick.team_division === 'NFC East');
            nfcNorth.value = user_picks.value.filter(pick => pick.team_division === 'NFC North');
            nfcWest.value = user_picks.value.filter(pick => pick.team_division === 'NFC West');
            nfcSouth.value = user_picks.value.filter(pick => pick.team_division === 'NFC South');       

        }

        const season_res = await nflSeason.getStandings();
        console.log(season_res)
        regularSeason.value = season_res;

        if(regularSeason.value){

            //AFC
            afcEastSeason.value = regularSeason.value.filter(pick => pick.team_division.trim() === 'AFC East');
            afcNorthSeason.value = regularSeason.value.filter(pick => pick.team_division.trim() === 'AFC North');
            afcWestSeason.value = regularSeason.value.filter(pick => pick.team_division.trim() === 'AFC West');
            afcSouthSeason.value = regularSeason.value.filter(pick => pick.team_division.trim() === 'AFC South');

            //NFC
            nfcEastSeason.value = regularSeason.value.filter(pick => pick.team_division.trim() === 'NFC East');
            nfcNorthSeason.value = regularSeason.value.filter(pick => pick.team_division.trim() === 'NFC North');
            nfcWestSeason.value = regularSeason.value.filter(pick => pick.team_division.trim() === 'NFC West');
            nfcSouthSeason.value = regularSeason.value.filter(pick => pick.team_division.trim() === 'NFC South');  
        }

        console.log("picks")
        console.log(user_picks.value)
        console.log(user_picks.value.length)
        if(user_picks.value.length == 0){
            displayValue.value = true
        }


    });


</script>

<template>

    <Navbar/>
    <div v-if="displayValue">

        <PicksLockin :regularSeason="regularSeason" />

    </div>
    <div v-else>
        
        <h1>User Picks</h1>
        <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-1 text-white h-48">

            <DivisionCard v-if="afcEast && afcEastSeason" :picks="afcEast" :nflSeason="afcEastSeason"/>
            <DivisionCard v-if="afcNorth && afcNorthSeason" :picks="afcNorth" :nflSeason="afcNorthSeason"/>
            <DivisionCard v-if="afcSouth && afcSouthSeason" :picks="afcSouth" :nflSeason="afcSouthSeason"/>
            <DivisionCard v-if="afcWest && afcWestSeason" :picks="afcWest" :nflSeason="afcWestSeason"/>

            <DivisionCard v-if="nfcEast && nfcEastSeason" :picks="nfcEast" :nflSeason="nfcEastSeason"/>
            <DivisionCard v-if="nfcNorth && nfcNorthSeason" :picks="nfcNorth" :nflSeason="nfcNorthSeason"/>
            <DivisionCard v-if="nfcWest && nfcWestSeason" :picks="nfcWest" :nflSeason="nfcWestSeason"/>
            <DivisionCard v-if="nfcSouth && nfcSouthSeason" :picks="nfcSouth" :nflSeason="nfcSouthSeason"/>

        </div>

    </div>



</template>

