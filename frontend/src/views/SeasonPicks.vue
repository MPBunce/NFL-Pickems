<script setup>

    import Navbar from '../components/Navbar.vue';
    import DivisionCard from '../components/DivisionCard.vue';
    import PicksLockin from '../components/PicksLockin.vue';
    import { ref, onMounted, watch } from 'vue';
    import { authStore } from '../store/authStore';
    import { picksStore } from '../store/picksStore';
    import { nflStore } from '../store/nflStore';

    const authStoreInstance = authStore();
    const picksStoreInstance = picksStore();
    const nflSeason = nflStore();

    const show_ref = ref(false);

    const afcEast = ref(null);
    const afcNorth = ref(null);
    const afcWest = ref(null);
    const afcSouth = ref(null);

    const nfcEast = ref(null);
    const nfcNorth = ref(null);
    const nfcWest = ref(null);
    const nfcSouth = ref(null);

    const afcEastSeason = ref(null);
    const afcNorthSeason = ref(null);
    const afcWestSeason = ref(null);
    const afcSouthSeason = ref(null);

    const nfcEastSeason = ref(null);
    const nfcNorthSeason = ref(null);
    const nfcWestSeason = ref(null);
    const nfcSouthSeason = ref(null);

    onMounted(async () => {
        
        const res = await authStoreInstance.test();
        const result = await picksStoreInstance.getPicks();
        const season_res = await nflSeason.getStandings();

        show_ref.value = true

    });

    watch(() => picksStoreInstance.picks, (newPicks, oldPicks) => {

        if(picksStoreInstance.picks != null){
            //AFC
            afcEast.value =  picksStoreInstance.picks.filter(pick => pick.team_division.trim() === 'AFC East');
            afcNorth.value =  picksStoreInstance.picks.filter(pick => pick.team_division.trim() === 'AFC North');
            afcWest.value =  picksStoreInstance.picks.filter(pick => pick.team_division.trim() === 'AFC West');
            afcSouth.value =  picksStoreInstance.picks.filter(pick => pick.team_division.trim() === 'AFC South');

            //NFC
            nfcEast.value =  picksStoreInstance.picks.filter(pick => pick.team_division.trim() === 'NFC East');
            nfcNorth.value =  picksStoreInstance.picks.filter(pick => pick.team_division.trim() === 'NFC North');
            nfcWest.value =  picksStoreInstance.picks.filter(pick => pick.team_division.trim() === 'NFC West');
            nfcSouth.value =  picksStoreInstance.picks.filter(pick => pick.team_division.trim()=== 'NFC South');                 
        } 
  
    })

    watch( () => nflSeason.standings , (newPicks, oldPicks) => {

        if(nflSeason.standings != null){
            //AFC
            afcEastSeason.value = nflSeason.standings.filter(pick => pick.team_division.trim() === 'AFC East');
            afcNorthSeason.value = nflSeason.standings.filter(pick => pick.team_division.trim() === 'AFC North');
            afcWestSeason.value = nflSeason.standings.filter(pick => pick.team_division.trim() === 'AFC West');
            afcSouthSeason.value = nflSeason.standings.filter(pick => pick.team_division.trim() === 'AFC South');

            //NFC
            nfcEastSeason.value = nflSeason.standings.filter(pick => pick.team_division.trim() === 'NFC East');
            nfcNorthSeason.value = nflSeason.standings.filter(pick => pick.team_division.trim() === 'NFC North');
            nfcWestSeason.value = nflSeason.standings.filter(pick => pick.team_division.trim() === 'NFC West');
            nfcSouthSeason.value = nflSeason.standings.filter(pick => pick.team_division.trim() === 'NFC South');              
        }

    })

</script>

<template>
    <div>

        <Navbar/>

        <!-- <button @click="log">LOG</button> -->

        <div v-if="show_ref">
            <div v-if="picksStoreInstance.picks == null || picksStoreInstance.picks.length < 1">

                <PicksLockin :regularSeason="nflSeason.standings" />
                
            </div>
            <div v-else>
            
                <div class="text-center">
                    <h1 class="my-4 py-4 text-white text-2xl font-mono">Your picks for this Season!</h1>
                </div>

                <div class="grid grid-cols-1 lg:grid-cols-2 2xl:grid-cols-4 gap-1 text-white h-48">

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
        </div>


    </div>
</template>

