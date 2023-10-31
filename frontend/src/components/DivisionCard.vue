<script setup>

  const getTeamLogoUrl = (teamName) => {
    const imagePath = "src/assets/";
    const sanitizedTeamName = teamName.replace(/\s+/g, "_");
    return imagePath + sanitizedTeamName + ".png";
  } 

  const getTeamPosition = (teamName) => {
    const teamData = props.nflSeason.find((data) => data.team_name === teamName);
    return teamData ? teamData.divisional_position : 'Position Not Found';
  }

  const props = defineProps({
    picks: Array,
    nflSeason: Array,
  });

  const log = () =>{
    console.log(props.nflSeason)
  }

</script>

<template>

  <div v-if="props.nflSeason != null" class="rounded mx-4">
    <div class="bg-neutral-900">
        <div class="">

            <h1 class="my-2 py-4 ml-4 text-white text-2xl">{{ props.nflSeason[0].team_division}}</h1>

        </div>
        <div class="bg-neutral-800 cursor-pointer dragArea list-group w-full divide-y divide-black">
          <div
            class="flex flex-row"
            v-for="(team, index) in picks"
            :key="team.id"
          >

            <div class="basis-1/4 bg-neutral-950 text-center py-6 text-lg">{{ index + 1 }} </div>
            <div class="basis-1/4 object-center ml-4 mt-4">
                <img class="w-10 h-10 object-center" :src="getTeamLogoUrl(team.team_name)">
            </div>
            <div class="basis-3/4 mt-6 overflow-visible">{{ team.team_name }}</div>

            <div v-if="team.division_position === getTeamPosition(team.team_name)">
              <div class="basis-1/4 bg-emerald-500 text-center py-6 px-6 text-lg">
                {{ getTeamPosition(team.team_name) }}                  
              </div>
            </div>
            <div v-else>
              <div class="basis-1/4 bg-rose-600 text-center py-6 px-6 text-lg">
                {{ getTeamPosition(team.team_name) }}                  
              </div>
            </div>

          </div>
        </div>
    </div>
  </div>

</template>