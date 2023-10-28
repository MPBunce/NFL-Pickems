<script setup>

    import { ref, onMounted } from 'vue';
    import { VueDraggableNext } from 'vue-draggable-next'
    import { picksStore } from '../store/picksStore'

    const picksInstance = picksStore()

    const props = defineProps({
        regularSeason: Array,
    });

    const afcEastSeason = ref(null);
    const afcNorthSeason = ref(null);
    const afcWestSeason = ref(null);
    const afcSouthSeason = ref(null);

    const nfcEastSeason = ref(null);
    const nfcNorthSeason = ref(null);
    const nfcWestSeason = ref(null);
    const nfcSouthSeason = ref(null);


    onMounted(async () => {

        if(props.regularSeason){

            //AFC
            afcEastSeason.value = props.regularSeason.filter(pick => pick.team_division.trim() === 'AFC East');
            afcNorthSeason.value = props.regularSeason.filter(pick => pick.team_division.trim() === 'AFC North');
            afcWestSeason.value = props.regularSeason.filter(pick => pick.team_division.trim() === 'AFC West');
            afcSouthSeason.value = props.regularSeason.filter(pick => pick.team_division.trim() === 'AFC South');

            //NFC
            nfcEastSeason.value = props.regularSeason.filter(pick => pick.team_division.trim() === 'NFC East');
            nfcNorthSeason.value = props.regularSeason.filter(pick => pick.team_division.trim() === 'NFC North');
            nfcWestSeason.value = props.regularSeason.filter(pick => pick.team_division.trim() === 'NFC West');
            nfcSouthSeason.value = props.regularSeason.filter(pick => pick.team_division.trim() === 'NFC South');  
        }

    });

    //AFC
    const newAfcEastSeason = ref([]);
    const handleAfcEastSeasonChange = (newOrder) => {
        newAfcEastSeason.value = newOrder;
    }

    const newAfcNorthSeason = ref([]);
    const handleAfcNorthSeasonChange = (newOrder) => {
        newAfcNorthSeason.value = newOrder;
    }

    const newAfcWestSeason = ref([]);
    const handleAfcWestSeasonChange = (newOrder) => {
        newAfcWestSeason.value = newOrder;
    }

    const newAfcSouthSeason = ref([]);
    const handleAfcSouthSeasonChange = (newOrder) => {
        newAfcSouthSeason.value = newOrder;
    }

    //NFC
    const newNfcEastSeason = ref([]);
    const handleNfcEastSeasonChange = (newOrder) => {
        newNfcEastSeason.value = newOrder;
    }

    const newNfcNorthSeason = ref([]);
    const handleNfcNorthSeasonChange = (newOrder) => {
        newNfcNorthSeason.value = newOrder;
    }

    const newNfcWestSeason = ref([]);
    const handleNfcWestSeasonChange = (newOrder) => {
        newNfcWestSeason.value = newOrder;
    }

    const newNfcSouthSeason = ref([]);
    const handleNfcSouthSeasonChange = (newOrder) => {
        newNfcSouthSeason.value = newOrder;
    }


    const log = async () => {
        const this_year = 2023
        const lockin_array = []

        //AFC
        for (let i = 0; i < afcEastSeason.value.length; i++) {
            const team = afcEastSeason.value[i];
            const data = {
                "year": this_year,
                "team_name": team.team_name,
                "team_division": team.team_division,
                "division_position": i + 1
            };
            lockin_array.push(data);
        }
        for (let i = 0; i < afcNorthSeason.value.length; i++) {
            const team = afcNorthSeason.value[i];
            const data = {
                "year": this_year,
                "team_name": team.team_name,
                "team_division": team.team_division,
                "division_position": i + 1
            };
            lockin_array.push(data);
        }
        for (let i = 0; i < afcWestSeason.value.length; i++) {
            const team = afcWestSeason.value[i];
            const data = {
                "year": this_year,
                "team_name": team.team_name,
                "team_division": team.team_division,
                "division_position": i + 1
            };
            lockin_array.push(data);
        }
        for (let i = 0; i < afcSouthSeason.value.length; i++) {
            const team = afcSouthSeason.value[i];
            const data = {
                "year": this_year,
                "team_name": team.team_name,
                "team_division": team.team_division,
                "division_position": i + 1
            };
            lockin_array.push(data);
        }

        //NFC
        for (let i = 0; i < nfcEastSeason.value.length; i++) {
            const team = nfcEastSeason.value[i];
            const data = {
                "year": this_year,
                "team_name": team.team_name,
                "team_division": team.team_division,
                "division_position": i + 1
            };
            lockin_array.push(data);
        }
        for (let i = 0; i < nfcNorthSeason.value.length; i++) {
            const team = nfcNorthSeason.value[i];
            const data = {
                "year": this_year,
                "team_name": team.team_name,
                "team_division": team.team_division,
                "division_position": i + 1
            };
            lockin_array.push(data);
        }
        for (let i = 0; i < nfcSouthSeason.value.length; i++) {
            const team = nfcSouthSeason.value[i];
            const data = {
                "year": this_year,
                "team_name": team.team_name,
                "team_division": team.team_division,
                "division_position": i + 1
            };
            lockin_array.push(data);
        }
        for (let i = 0; i < nfcWestSeason.value.length; i++) {
            const team = nfcWestSeason.value[i];
            const data = {
                "year": this_year,
                "team_name": team.team_name,
                "team_division": team.team_division,
                "division_position": i + 1
            };
            lockin_array.push(data);
        }
        console.log(lockin_array)
        
        try{
            const res = await picksInstance.lockInPicks(lockin_array)
        } catch (error){
            console.log(error)
        }

    }

</script>

<template>

    <div class="text-center">
        <h1 class="my-4 text-white text-2xl font-mono">Enter Your Picks for the Season!</h1>
        <button class="my-8 bg-yellow-500 hover:bg-yellow-700 text-black py-2 px-8 rounded-full" @click="log">LOCK IN</button>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-1 text-white h-48">

        <div class="cursor-pointer bg-neutral-800 my-4 mx-4 px-4 py-4 rounded-lg">
            <div class="text-center">
                <h1 class="my-4 text-white text-2xl font-mono">AFC North</h1>
            </div>
            <VueDraggableNext class="dragArea list-group w-full divide-y" :list="afcNorthSeason" @change="handleAfcNorthSeasonChange">
                <div
                    class="flex flex-row py-4"
                    v-for="(team, index) in afcNorthSeason"
                    :key="team.id"
                >

                    <div class="basis-1/4">{{ index + 1 }} </div>
                    <div class="basis-3/4">{{ team.team_name }}</div>

                </div>
            </VueDraggableNext>
        </div>

        <div class="cursor-pointer bg-neutral-800 my-4 mx-4 px-4 py-4 rounded-lg">
            <div class="text-center">
                <h1 class="my-4 text-white text-2xl font-mono">AFC East</h1>
            </div>
            <VueDraggableNext class="dragArea list-group w-full divide-y" :list="afcEastSeason" @change="handleAfcEastSeasonChange">
                <div
                    class="flex flex-row py-4"
                    v-for="(team, index) in afcEastSeason"
                    :key="team.id"
                >

                    <div class="basis-1/4">{{ index + 1 }} </div>
                    <div class="basis-3/4">{{ team.team_name }}</div>
                </div>
            </VueDraggableNext>
        </div>

        <div class="cursor-pointer bg-neutral-800 my-4 mx-4 px-4 py-4 rounded-lg">
            <div class="text-center">
                <h1 class="my-4 text-white text-2xl font-mono">AFC South</h1>
            </div>
            <VueDraggableNext class="dragArea list-group w-full divide-y" :list="afcSouthSeason" @change="handleAfcSouthSeasonChange">
                <div
                    class="flex flex-row py-4"
                    v-for="(team, index) in afcSouthSeason"
                    :key="team.id"
                >
                    <div class="basis-1/4">{{ index + 1 }} </div>
                    <div class="basis-3/4">{{ team.team_name }}</div>
                </div>
            </VueDraggableNext>
        </div>

        <div class="cursor-pointer bg-neutral-800 my-4 mx-4 px-4 py-4 rounded-lg">
            <div class="text-center">
                <h1 class="my-4 text-white text-2xl font-mono">AFC West</h1>
            </div>
            <VueDraggableNext class="dragArea list-group w-full divide-y" :list="afcWestSeason" @change="handleAfcWestSeasonChange">
                <div
                    class="flex flex-row py-4"
                    v-for="(team, index) in afcWestSeason"
                    :key="team.id"
                >
                    <div class="basis-1/4">{{ index + 1 }} </div>
                    <div class="basis-3/4">{{ team.team_name }}</div>
                </div>
            </VueDraggableNext>
        </div>

        <div class="cursor-pointer bg-neutral-800 my-4 mx-4 px-4 py-4 rounded-lg">
            <div class="text-center">
                <h1 class="my-4 text-white text-2xl font-mono">NFC North</h1>
            </div>
            <VueDraggableNext class="dragArea list-group w-full divide-y" :list="nfcNorthSeason" @change="handleNfcNorthSeasonChange">
                <div
                    class="flex flex-row py-4"
                    v-for="(team, index) in nfcNorthSeason"
                    :key="team.id"
                >
                    <div class="basis-1/4">{{ index + 1 }} </div>
                    <div class="basis-3/4">{{ team.team_name }}</div>
                </div>
            </VueDraggableNext>
        </div>

        <div class="cursor-pointer bg-neutral-800 my-4 mx-4 px-4 py-4 rounded-lg">
            <div class="text-center">
                <h1 class="my-4 text-white text-2xl font-mono">NFC East</h1>
            </div>
            <VueDraggableNext class="dragArea list-group w-full divide-y" :list="nfcEastSeason" @change="handleNfcEastSeasonChange">
                <div
                    class="flex flex-row py-4"
                    v-for="(team, index) in nfcEastSeason"
                    :key="team.id"
                >
                    <div class="basis-1/4">{{ index + 1 }} </div>
                    <div class="basis-3/4">{{ team.team_name }}</div>
                </div>
            </VueDraggableNext>
        </div>

        <div class="cursor-pointer bg-neutral-800 my-4 mx-4 px-4 py-4 rounded-lg">
            <div class="text-center">
                <h1 class="my-4 text-white text-2xl font-mono">NFC Sorth</h1>
            </div>
            <VueDraggableNext class="dragArea list-group w-full divide-y" :list="nfcSouthSeason" @change="handleNfcSouthSeasonChange">
                <div
                    class="flex flex-row py-4"
                    v-for="(team, index) in nfcSouthSeason"
                    :key="team.id"
                >
                    <div class="basis-1/4">{{ index + 1 }} </div>
                    <div class="basis-3/4">{{ team.team_name }}</div>
                </div>
            </VueDraggableNext>
        </div>

        <div class="cursor-pointer bg-neutral-800 my-4 mx-4 px-4 py-4 rounded-lg">
            <div class="text-center">
                <h1 class="my-4 text-white text-2xl font-mono">NFC West</h1>
            </div>
            <VueDraggableNext class="dragArea list-group w-full divide-y" :list="nfcWestSeason" @change="handleNfcWestSeasonChange">
                <div
                    class="flex flex-row py-4"
                    v-for="(team, index) in nfcWestSeason"
                    :key="team.id"
                >
                    <div class="basis-1/4">{{ index + 1 }} </div>
                    <div class="basis-3/4">{{ team.team_name }}</div>
                </div>
            </VueDraggableNext>
        </div>

    </div>

</template>
