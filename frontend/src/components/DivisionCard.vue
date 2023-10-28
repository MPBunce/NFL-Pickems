<script setup>

  const props = defineProps({
    picks: Array,
    nflSeason: Array,
  });

</script>

<template>

  <div class="flex flex-col items-center justify-center py-6 px-6 mx-auto w-auto">

    <div class="w-full bg-neutral-800 rounded">
      <div v-if="props.picks && props.nflSeason" class="p-6 space-y-4 md:space-y-6 sm:p-8">
        
        <div class="text-center">
            <h1 class="my-4 text-white text-2xl font-mono">{{picks[0].team_division}}</h1>
        </div>

        <table class="table-fixed border-spacing-2">
          <thead>
            <tr>
              <th class="border-b-2 p-2">Position</th>
              <th class="border-b-2 p-2">Team Name</th>
              <th class="border-b-2 p-2">Prediction Status</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="p-4">{{ props.picks[0].division_position }}</td>
              <td class="p-4">{{ props.picks[0].team_name }}</td>
              <td
                :class="{
                  'p-4 text-green-200': props.picks[0].team_name === props.nflSeason[0].team_name, // Correct guess
                  'p-4 text-red-200': props.picks[0].team_name !== props.nflSeason[0].team_name, // Incorrect guess
                }"
              >
                {{ props.picks[0].team_name == props.nflSeason[0].team_name ? 'correct' : 'incorrect' }}
              </td>
            </tr>
            <tr>
              <td class="p-4">{{ props.picks[1].division_position }}</td>
              <td class="p-4">{{ props.picks[1].team_name }}</td>
              <td
                :class="{
                  'p-4 text-green-200': props.picks[1].team_name === props.nflSeason[1].team_name, // Correct guess
                  'p-4 text-red-200': props.picks[1].team_name !== props.nflSeason[1].team_name, // Incorrect guess
                }"
              >
                {{ props.picks[1].team_name == props.nflSeason[1].team_name ? 'correct' : 'incorrect' }}
              </td>
            </tr>
            <tr>
              <td class="p-4">{{ props.picks[2].division_position }}</td>
              <td class="p-4">{{ props.picks[2].team_name }}</td>
              <td
                :class="{
                  'p-4 text-green-200': props.picks[2].team_name === props.nflSeason[2].team_name, // Correct guess
                  'p-4 text-red-200': props.picks[2].team_name !== props.nflSeason[2].team_name, // Incorrect guess
                }"
              >
                {{ props.picks[2].team_name == props.nflSeason[2].team_name ? 'correct' : 'incorrect' }}
              </td>
            </tr>
            <tr>
              <td class="p-4">{{ props.picks[3].division_position }}</td>
              <td class="p-4">{{ props.picks[3].team_name }}</td>
              <td
                :class="{
                  'p-4 text-green-200': props.picks[3].team_name === props.nflSeason[3].team_name, // Correct guess
                  'p-4 text-red-200': props.picks[3].team_name !== props.nflSeason[3].team_name, // Incorrect guess
                }"
              >
                {{ props.picks[3].team_name == props.nflSeason[3].team_name ? 'correct' : 'incorrect' }}
              </td>
            </tr>
          </tbody>
        </table>


      </div>
    </div>
  </div>

</template>