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
            afcEastSeason.value = props.regularSeason.filter(pick => pick.division.trim() === 'AFC East');
            afcNorthSeason.value = props.regularSeason.filter(pick => pick.division.trim() === 'AFC North');
            afcWestSeason.value = props.regularSeason.filter(pick => pick.division.trim() === 'AFC West');
            afcSouthSeason.value = props.regularSeason.filter(pick => pick.division.trim() === 'AFC South');

            //NFC
            nfcEastSeason.value = props.regularSeason.filter(pick => pick.division.trim() === 'NFC East');
            nfcNorthSeason.value = props.regularSeason.filter(pick => pick.division.trim() === 'NFC North');
            nfcWestSeason.value = props.regularSeason.filter(pick => pick.division.trim() === 'NFC West');
            nfcSouthSeason.value = props.regularSeason.filter(pick => pick.division.trim() === 'NFC South');  
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
                "team": team.team,
                "division": team.division,
                "division_position": i + 1
            };
            lockin_array.push(data);
        }
        for (let i = 0; i < afcNorthSeason.value.length; i++) {
            const team = afcNorthSeason.value[i];
            const data = {
                "year": this_year,
                "team": team.team,
                "division": team.division,
                "division_position": i + 1
            };
            lockin_array.push(data);
        }
        for (let i = 0; i < afcWestSeason.value.length; i++) {
            const team = afcWestSeason.value[i];
            const data = {
                "year": this_year,
                "team": team.team,
                "division": team.division,
                "division_position": i + 1
            };
            lockin_array.push(data);
        }
        for (let i = 0; i < afcSouthSeason.value.length; i++) {
            const team = afcSouthSeason.value[i];
            const data = {
                "year": this_year,
                "team": team.team,
                "division": team.division,
                "division_position": i + 1
            };
            lockin_array.push(data);
        }

        //NFC
        for (let i = 0; i < nfcEastSeason.value.length; i++) {
            const team = nfcEastSeason.value[i];
            const data = {
                "year": this_year,
                "team": team.team,
                "division": team.division,
                "division_position": i + 1
            };
            lockin_array.push(data);
        }
        for (let i = 0; i < nfcNorthSeason.value.length; i++) {
            const team = nfcNorthSeason.value[i];
            const data = {
                "year": this_year,
                "team": team.team,
                "division": team.division,
                "division_position": i + 1
            };
            lockin_array.push(data);
        }
        for (let i = 0; i < nfcSouthSeason.value.length; i++) {
            const team = nfcSouthSeason.value[i];
            const data = {
                "year": this_year,
                "team": team.team,
                "division": team.division,
                "division_position": i + 1
            };
            lockin_array.push(data);
        }
        for (let i = 0; i < nfcWestSeason.value.length; i++) {
            const team = nfcWestSeason.value[i];
            const data = {
                "year": this_year,
                "team": team.team,
                "division": team.division,
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

    const getTeamLogoUrl = (teamName) => {
        const imagePath = "src/assets/";
        const sanitizedTeamName = teamName.replace(/\s+/g, "_");
        return imagePath + sanitizedTeamName + ".png";
    }

</script>

<template>

    <div class="text-center my-4">
        <h1 class="my-4 pt-4 text-white text-2xl font-mono">Lockin's your picks for the 2023 season!</h1>
        
        <button type="button" class="text-center rounded max-w-sm w-full bg-gradient-to-r from-green-400 to-blue-500 hover:from-pink-500 hover:to-yellow-500 text-white text-2xl uppercase font-bold shadow-md mx-auto p-5">
            <div>LOCKIN</div>
        </button>
    </div>


    <div class="grid grid-cols-1 lg:grid-cols-2 2xl:grid-cols-4 gap-2 text-white mb-8">


        <div class="rounded mx-4">
            <div class="bg-neutral-900">
                <div class="">
                    <h1 class="my-2 py-4 ml-4 text-white text-2xl">AFC North</h1>
                </div>
                <VueDraggableNext class="bg-neutral-800 cursor-pointer dragArea list-group w-full divide-y divide-black" :list="afcNorthSeason" @change="handleAfcNorthSeasonChange">
                    <div
                        class="flex flex-row"
                        v-for="(team, index) in afcNorthSeason"
                        :key="team.id"
                    >

                        <div class="basis-1/4 bg-neutral-950 text-center py-6 text-lg">{{ index + 1 }} </div>
                        <div class="basis-1/4 object-center ml-4 mt-4">
                            <img class="w-10 h-10 object-center" :src="getTeamLogoUrl(team.team)">
                        </div>

                        <div class="basis-3/4 mt-6">{{ team.team }}</div>
                        <div class="mr-2 mt-6">
                            <svg class="fill-current h-6 w-10 text-neutral-900" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                                <path d="M0 3h20v2H0V3zm0 6h20v2H0V9zm0 6h20v2H0v-2z"/>
                            </svg>
                        </div>

                    </div>
                </VueDraggableNext>
            </div>

        </div>

        
        <div class="rounded mx-4">
            <div class="bg-neutral-900">
                <div class="">
                    <h1 class="my-2 py-4 ml-4 text-white text-2xl">AFC East</h1>
                </div>
                <VueDraggableNext class="bg-neutral-800 cursor-pointer dragArea list-group w-full divide-y divide-black" :list="afcEastSeason" @change="handleAfcEastSeasonChange">
                    <div
                        class="flex flex-row"
                        v-for="(team, index) in afcEastSeason"
                        :key="team.id"
                    >

                        <div class="basis-1/4 bg-neutral-950 text-center py-6 text-lg">{{ index + 1 }} </div>
                        <div class="basis-1/4 object-center ml-4 mt-4">
                            <img class="w-10 h-10 object-center" :src="getTeamLogoUrl(team.team)">
                        </div>

                        <div class="basis-3/4 mt-6">{{ team.team }}</div>
                        <div class="mr-2 mt-6">
                            <svg class="fill-current h-6 w-10 text-neutral-900" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                                <path d="M0 3h20v2H0V3zm0 6h20v2H0V9zm0 6h20v2H0v-2z"/>
                            </svg>
                        </div>

                    </div>
                </VueDraggableNext>
            </div>
        </div>

        <div class="rounded mx-4">
            <div class="bg-neutral-900">
                <div class="">
                    <h1 class="my-2 py-4 ml-4 text-white text-2xl">AFC South</h1>
                </div>
                <VueDraggableNext class="bg-neutral-800 cursor-pointer dragArea list-group w-full divide-y divide-black" :list="afcSouthSeason" @change="handleAfcSouthSeasonChange">
                    <div
                        class="flex flex-row"
                        v-for="(team, index) in afcSouthSeason"
                        :key="team.id"
                    >

                        <div class="basis-1/4 bg-neutral-950 text-center py-6 text-lg">{{ index + 1 }} </div>
                        <div class="basis-1/4 object-center ml-4 mt-4">
                            <img class="w-10 h-10 object-center" :src="getTeamLogoUrl(team.team)">
                        </div>

                        <div class="basis-3/4 mt-6">{{ team.team }}</div>
                        <div class="mr-2 mt-6">
                            <svg class="fill-current h-6 w-10 text-neutral-900" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                                <path d="M0 3h20v2H0V3zm0 6h20v2H0V9zm0 6h20v2H0v-2z"/>
                            </svg>
                        </div>

                    </div>
                </VueDraggableNext>
            </div>
        </div>

        <div class="rounded mx-4">
            <div class="bg-neutral-900">
                <div class="">
                    <h1 class="my-2 py-4 ml-4 text-white text-2xl">AFC West</h1>
                </div>
                <VueDraggableNext class="bg-neutral-800 cursor-pointer dragArea list-group w-full divide-y divide-black" :list="afcWestSeason" @change="handleAfcWestSeasonChange">
                    <div
                        class="flex flex-row"
                        v-for="(team, index) in afcWestSeason"
                        :key="team.id"
                    >

                        <div class="basis-1/4 bg-neutral-950 text-center py-6 text-lg">{{ index + 1 }} </div>
                        <div class="basis-1/4 object-center ml-4 mt-4">
                            <img class="w-10 h-10 object-center" :src="getTeamLogoUrl(team.team)">
                        </div>

                        <div class="basis-3/4 mt-6">{{ team.team }}</div>
                        <div class="mr-2 mt-6">
                            <svg class="fill-current h-6 w-10 text-neutral-900" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                                <path d="M0 3h20v2H0V3zm0 6h20v2H0V9zm0 6h20v2H0v-2z"/>
                            </svg>
                        </div>

                    </div>
                </VueDraggableNext>
            </div>
        </div>

        <div class="rounded mx-4">
            <div class="bg-neutral-900">
                <div class="">
                    <h1 class="my-2 py-4 ml-4 text-white text-2xl">NFC North</h1>
                </div>
                <VueDraggableNext class="bg-neutral-800 cursor-pointer dragArea list-group w-full divide-y divide-black" :list="nfcNorthSeason" @change="handleNfcNorthSeasonChange">
                    <div
                        class="flex flex-row"
                        v-for="(team, index) in nfcNorthSeason"
                        :key="team.id"
                    >

                        <div class="basis-1/4 bg-neutral-950 text-center py-6 text-lg">{{ index + 1 }} </div>
                        <div class="basis-1/4 object-center ml-4 mt-4">
                            <img class="w-10 h-10 object-center" :src="getTeamLogoUrl(team.team)">
                        </div>

                        <div class="basis-3/4 mt-6">{{ team.team }}</div>
                        <div class="mr-2 mt-6">
                            <svg class="fill-current h-6 w-10 text-neutral-900" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                                <path d="M0 3h20v2H0V3zm0 6h20v2H0V9zm0 6h20v2H0v-2z"/>
                            </svg>
                        </div>

                    </div>
                </VueDraggableNext>
            </div>
        </div>

        <div class="rounded mx-4">
            <div class="bg-neutral-900">
                <div class="">
                    <h1 class="my-2 py-4 ml-4 text-white text-2xl">NFC East</h1>
                </div>
                <VueDraggableNext class="bg-neutral-800 cursor-pointer dragArea list-group w-full divide-y divide-black" :list="nfcEastSeason" @change="handleNfcEastSeasonChange">
                    <div
                        class="flex flex-row"
                        v-for="(team, index) in nfcEastSeason"
                        :key="team.id"
                    >

                        <div class="basis-1/4 bg-neutral-950 text-center py-6 text-lg">{{ index + 1 }} </div>
                        <div class="basis-1/4 object-center ml-4 mt-4">
                            <img class="w-10 h-10 object-center" :src="getTeamLogoUrl(team.team)">
                        </div>

                        <div class="basis-3/4 mt-6">{{ team.team }}</div>
                        <div class="mr-2 mt-6">
                            <svg class="fill-current h-6 w-10 text-neutral-900" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                                <path d="M0 3h20v2H0V3zm0 6h20v2H0V9zm0 6h20v2H0v-2z"/>
                            </svg>
                        </div>

                    </div>
                </VueDraggableNext>
            </div>
        </div>

        <div class="rounded mx-4">
            <div class="bg-neutral-900">
                <div class="">
                    <h1 class="my-2 py-4 ml-4 text-white text-2xl">NFC South</h1>
                </div>
                <VueDraggableNext class="bg-neutral-800 cursor-pointer dragArea list-group w-full divide-y divide-black" :list="nfcSouthSeason" @change="handleNfcSouthSeasonChange">
                    <div
                        class="flex flex-row"
                        v-for="(team, index) in nfcSouthSeason"
                        :key="team.id"
                    >

                        <div class="basis-1/4 bg-neutral-950 text-center py-6 text-lg">{{ index + 1 }} </div>
                        <div class="basis-1/4 object-center ml-4 mt-4">
                            <img class="w-10 h-10 object-center" :src="getTeamLogoUrl(team.team)">
                        </div>

                        <div class="basis-3/4 mt-6">{{ team.team }}</div>
                        <div class="mr-2 mt-6">
                            <svg class="fill-current h-6 w-10 text-neutral-900" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                                <path d="M0 3h20v2H0V3zm0 6h20v2H0V9zm0 6h20v2H0v-2z"/>
                            </svg>
                        </div>

                    </div>
                </VueDraggableNext>
            </div>
        </div>

        <div class="rounded mx-4">
            <div class="bg-neutral-900">
                <div class="">
                    <h1 class="my-2 py-4 ml-4 text-white text-2xl">NFC West</h1>
                </div>
                <VueDraggableNext class="bg-neutral-800 cursor-pointer dragArea list-group w-full divide-y divide-black" :list="nfcWestSeason" @change="handleNfcWestSeasonChange">
                    <div
                        class="flex flex-row"
                        v-for="(team, index) in nfcWestSeason"
                        :key="team.id"
                    >

                        <div class="basis-1/4 bg-neutral-950 text-center py-6 text-lg">{{ index + 1 }} </div>
                        <div class="basis-1/4 object-center ml-4 mt-4">
                            <img class="w-10 h-10 object-center" :src="getTeamLogoUrl(team.team)">
                        </div>

                        <div class="basis-3/4 mt-6">{{ team.team }}</div>
                        <div class="mr-2 mt-6">
                            <svg class="fill-current h-6 w-10 text-neutral-900" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                                <path d="M0 3h20v2H0V3zm0 6h20v2H0V9zm0 6h20v2H0v-2z"/>
                            </svg>
                        </div>

                    </div>
                </VueDraggableNext>
            </div>
        </div>

    </div>

</template>
