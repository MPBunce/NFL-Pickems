<script setup>

    import { ref, onMounted } from 'vue';
    import { VueDraggableNext } from 'vue-draggable-next'

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


    const log = () => {
        console.log(nfcEastSeason)
    }


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

</script>

<template>
    <h1 class="my-2">Enter Your Picks for the Season!  <button @click="log">log</button></h1>

    <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-1 text-white h-48">

        <div>
            <h1 class="text-black">AFC North</h1>
            <VueDraggableNext class="dragArea list-group w-full" :list="afcNorthSeason" @change="handleAfcNorthSeasonChange">
                <div
                    class="list-group-item bg-gray-300 m-1 p-3 rounded-md text-center text-black"
                    v-for="team in afcNorthSeason"
                    :key="team.id"
                >
                    {{ team.team_name }}
                </div>
            </VueDraggableNext>
        </div>

        <div>
            <h1 class="text-black">AFC East</h1>
            <VueDraggableNext class="dragArea list-group w-full" :list="afcEastSeason" @change="handleAfcEastSeasonChange">
                <div
                    class="list-group-item bg-gray-300 m-1 p-3 rounded-md text-center text-black"
                    v-for="team in afcEastSeason"
                    :key="team.id"
                >
                    {{ team.team_name }}
                </div>
            </VueDraggableNext>
        </div>

        <div>
            <h1 class="text-black">AFC South</h1>
            <VueDraggableNext class="dragArea list-group w-full" :list="afcSouthSeason" @change="handleAfcSouthSeasonChange">
                <div
                    class="list-group-item bg-gray-300 m-1 p-3 rounded-md text-center text-black"
                    v-for="team in afcSouthSeason"
                    :key="team.id"
                >
                    {{ team.team_name }}
                </div>
            </VueDraggableNext>
        </div>

        <div>
            <h1 class="text-black">AFC West</h1>
            <VueDraggableNext class="dragArea list-group w-full" :list="afcWestSeason" @change="handleAfcWestSeasonChange">
                <div
                    class="list-group-item bg-gray-300 m-1 p-3 rounded-md text-center text-black"
                    v-for="team in afcWestSeason"
                    :key="team.id"
                >
                    {{ team.team_name }}
                </div>
            </VueDraggableNext>
        </div>

        <div>
            <h1 class="text-black">NFC North</h1>
            <VueDraggableNext class="dragArea list-group w-full" :list="nfcNorthSeason" @change="handleNfcNorthSeasonChange">
                <div
                    class="list-group-item bg-gray-300 m-1 p-3 rounded-md text-center text-black"
                    v-for="team in nfcNorthSeason"
                    :key="team.id"
                >
                    {{ team.team_name }}
                </div>
            </VueDraggableNext>
        </div>

        <div>
            <h1 class="text-black">NFC East</h1>
            <VueDraggableNext class="dragArea list-group w-full" :list="nfcEastSeason" @change="handleNfcEastSeasonChange">
                <div
                    class="list-group-item bg-gray-300 m-1 p-3 rounded-md text-center text-black"
                    v-for="team in nfcEastSeason"
                    :key="team.id"
                >
                    {{ team.team_name }}
                </div>
            </VueDraggableNext>
        </div>

        <div>
            <h1 class="text-black">NFC South</h1>
            <VueDraggableNext class="dragArea list-group w-full" :list="nfcSouthSeason" @change="handleNfcSouthSeasonChange">
                <div
                    class="list-group-item bg-gray-300 m-1 p-3 rounded-md text-center text-black"
                    v-for="team in nfcSouthSeason"
                    :key="team.id"
                >
                    {{ team.team_name }}
                </div>
            </VueDraggableNext>
        </div>

        <div>
            <h1 class="text-black">NFC West</h1>
            <VueDraggableNext class="dragArea list-group w-full" :list="nfcWestSeason" @change="handleNfcWestSeasonChange">
                <div
                    class="list-group-item bg-gray-300 m-1 p-3 rounded-md text-center text-black"
                    v-for="team in nfcWestSeason"
                    :key="team.id"
                >
                    {{ team.team_name }}
                </div>
            </VueDraggableNext>
        </div>

    </div>

</template>
