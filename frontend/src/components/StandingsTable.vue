<script setup>
  const props = defineProps({
    nflSeason: Array,
  });

  const getTeamLogoUrl = (teamName) => {
    const imagePath = "src/assets/";
    const sanitizedTeamName = teamName.replace(/\s+/g, "_");
    return imagePath + sanitizedTeamName + ".png";
  }

  const log = () => {
    console.log(props.nflSeason);
    console.log(props.nflSeason);
  };

</script>

<template>

  <div v-if="props.nflSeason != null" class="rounded mx-4">
    <div class="bg-neutral-900">
        <div class="">
            <h1 class="my-2 py-4 ml-4 text-white text-2xl">{{ props.nflSeason[0].division }}</h1>
        </div>
        <div class="bg-neutral-800 cursor-pointer dragArea list-group w-full divide-y divide-black">
          <div
            class="flex flex-row"
            v-for="(team, index) in nflSeason"
            :key="team.id"
          >

            <div class="basis-1/4 bg-neutral-950 text-center py-6 text-lg">{{ index + 1 }} </div>
            <div class="basis-1/4 object-center ml-4 mt-4">
                <img class="w-10 h-10 object-center" :src="getTeamLogoUrl(team.team)">
            </div>

            <div class="basis-3/4 mt-6">{{ team.team }}</div>
            <div class="basis-1/4 mt-6 mr-2">
              {{props.nflSeason[index].wins }} - {{props.nflSeason[index].losses }} - {{props.nflSeason[index].ties }}
            </div>

          </div>
        </div>
    </div>
  </div>

</template>