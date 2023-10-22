<script setup>
    import { ref, onMounted } from 'vue';
    import Navbar from '../components/Navbar.vue';
    import { nflStore } from '../store/nflStore';
    import StandingsTable from '../components/StandingsTable.vue';

    const nfl = nflStore();
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

        const season_res = await nfl.getStandings();
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

    });



</script>


<template>

    <Navbar/>
    <h1>2023 NFL Season Standings</h1>
    <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-1 text-white h-48">

        <StandingsTable  :nflSeason="afcNorthSeason"/>
        <StandingsTable  :nflSeason="afcEastSeason"/>
        <StandingsTable  :nflSeason="afcSouthSeason"/>
        <StandingsTable  :nflSeason="afcWestSeason"/>
        
        <StandingsTable  :nflSeason="nfcNorthSeason"/>
        <StandingsTable  :nflSeason="nfcEastSeason"/>
        <StandingsTable  :nflSeason="nfcSouthSeason"/>
        <StandingsTable  :nflSeason="nfcWestSeason"/>

    </div>


</template>