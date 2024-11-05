<script setup>
    import { ref, onMounted, watch } from 'vue';
    import Navbar from '../components/Navbar.vue';
    import { nflStore } from '../store/nflStore';
    import StandingsTable from '../components/StandingsTable.vue';

    const nflSeason = nflStore();

    const afcEastSeason = ref(null);
    const afcNorthSeason = ref(null);
    const afcWestSeason = ref(null);
    const afcSouthSeason = ref(null);

    const nfcEastSeason = ref(null);
    const nfcNorthSeason = ref(null);
    const nfcWestSeason = ref(null);
    const nfcSouthSeason = ref(null);

    onMounted(async () => {

        const season_res = await nflSeason.getStandings();
        console.log(season_res)
    });

    watch( () => nflSeason.standings , (newPicks, oldPicks) => {

        if(nflSeason.standings != null){
            //AFC
            afcEastSeason.value = nflSeason.standings.filter(pick => pick.division.trim() === 'AFC East');
            afcNorthSeason.value = nflSeason.standings.filter(pick => pick.division.trim() === 'AFC North');
            afcWestSeason.value = nflSeason.standings.filter(pick => pick.division.trim() === 'AFC West');
            afcSouthSeason.value = nflSeason.standings.filter(pick => pick.division.trim() === 'AFC South');

            //NFC
            nfcEastSeason.value = nflSeason.standings.filter(pick => pick.division.trim() === 'NFC East');
            nfcNorthSeason.value = nflSeason.standings.filter(pick => pick.division.trim() === 'NFC North');
            nfcWestSeason.value = nflSeason.standings.filter(pick => pick.division.trim() === 'NFC West');
            nfcSouthSeason.value = nflSeason.standings.filter(pick => pick.division.trim() === 'NFC South');              
        }

    })

</script>


<template>

    <Navbar/>
    <div class="text-center">
        <h1 class="my-4 py-4 text-white text-2xl font-mono">2023 NFL Season Standings</h1>
    </div>
    <div class="grid grid-cols-1 lg:grid-cols-2 2xl:grid-cols-4 gap-1 text-white mb-8">

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