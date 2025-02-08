<script setup>
    import { ref, onMounted, watch } from 'vue';
    import Navbar from '../components/Navbar.vue';
    import { leaderboardStore } from '../store/leaderboardStore';

    const leaderStore = leaderboardStore();

    const sorted = ref([]);

    onMounted(async () => {
        const res = await leaderStore.getLeaderboard();
    });

    watch(() => leaderStore.leaderboard, (newPicks, oldPicks) => {
        sorted.value = leaderStore.leaderboard.map(item => {
            if (item.regular_season_score === null) {
                item.regular_season_score = 0;
            }
            if (item.playoff_score === null) {
                item.playoff_score = 0;
            }
            item.total_score = (item.regular_season_score || 0) + (item.playoff_score || 0);
            return item;
        });

        sorted.value = sorted.value.sort((a, b) => b.total_score - a.total_score);
        console.log(sorted.value);
    });

    const log = () => {
        console.log(sorted.value);
    }
</script>


<template>

    <Navbar/>
    <div>

        <div>
            <div class="text-center">
                <h1 class="my-4 py-4 text-white text-2xl font-mono">2023 NFL Pickems leaderboard</h1>
            </div>

            <div class="relative overflow-x-auto my-4 mx-4">
                <table class="w-full text-sm text-left text-gray-500 dark:text-gray-400">
                    <thead class="text-xs text-white uppercase bg-neutral-600">
                        <tr>
                            <th scope="col" class="px-6 py-3">
                                Position
                            </th>
                            <th scope="col" class="px-6 py-3">
                                User
                            </th>
                            <!-- <th scope="col" class="px-6 py-3">
                                Regular Season Score
                            </th>
                            <th scope="col" class="px-6 py-3">
                                Playoffs Score
                            </th> -->
                            <th scope="col" class="px-6 py-3">
                                Total
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="( item, index) in sorted" class="text-white bg-neutral-800">
                            <td class="px-6 py-4">
                                <div class="mt-2 text-2xl">
                                    {{ index + 1 }}
                                </div>
                            </td>
                            <td class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white  flex flex-row gap-2">

                                <div class="h-12 w-12">
                                    <img class="rounded-2xl" v-bind:src="item.Picture" /> 
                                </div>
                                <div class="mt-4">
                                    {{ item.Name }}
                                </div>                            
                            </td>
                            <!-- <td class="px-6 py-4">
                                {{ item.regular_season_score }}
                            </td>
                            <td class="px-6 py-4">
                                {{ item.playoff_score }}
                            </td> -->
                            <td class="px-6 py-4 text-2xl">
                                {{ item.Score }}
                            </td>
                        </tr>

                    </tbody>
                </table>
            </div>

        </div>

    </div>


</template>