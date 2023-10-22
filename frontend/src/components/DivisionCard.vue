<script setup>

  const props = defineProps({
    picks: Array,
    nflSeason: Array,
  });

  const log = () => {
    console.log(props.picks);
    console.log(props.nflSeason);
  };

</script>

<template>

  <div class="flex flex-col items-center justify-center py-6 px-6 mx-auto w-5/6">

    <div class="w-full bg-white rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0 dark:bg-gray-800 dark:border-gray-700">
      <div v-if="props.picks && props.nflSeason" class="p-6 space-y-4 md:space-y-6 sm:p-8">
        
        <h1>{{picks[0].team_division}}</h1>
        <table class="table-fixed border-separate border-spacing-2 ">
          <thead>

            <th class="border-b-2 p-2">Position</th>
            <th class="border-b-2 p-2">Team Name</th>
            <th class="border-b-2 p-2">Prediction Status</th>

          </thead>
          <tbody>
            <tr>
              <td class="my-4">{{props.picks[0].division_position}}</td>
              <td class="my-4">{{props.picks[0].team_name}}</td>
              <td class="my-4">{{props.picks[0].team_name == props.nflSeason[0].team_name ? 'correct' : 'incorrect' }}</td>
            </tr>
            <tr>
              <td>{{props.picks[1].division_position}}</td>
              <td>{{props.picks[1].team_name}}</td>
              <td>{{props.picks[1].team_name == props.nflSeason[1].team_name ? 'correct' : 'incorrect' }}</td>
            </tr>
            <tr>
              <td>{{props.picks[2].division_position}}</td>
              <td>{{props.picks[2].team_name}}</td>
              <td>{{props.picks[2].team_name == props.nflSeason[2].team_name? 'correct' : 'incorrect' }}</td>
            </tr>
            <tr>
              <td>{{props.picks[3].division_position}}</td>
              <td>{{props.picks[3].team_name}}</td>
              <td>{{props.picks[3].team_name == props.nflSeason[3].team_name ? 'correct' : 'incorrect'}}</td>
            </tr>
          </tbody>
        </table>

      </div>
    </div>
  </div>

</template>