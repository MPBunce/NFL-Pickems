<script setup>

  const props = defineProps({
    nflSeason: Array,
  });

  const log = () => {
    console.log(props.nflSeason);
    console.log(props.nflSeason);
  };

</script>

<template>

  <div class="flex flex-col items-center justify-center py-6 px-6 mx-auto w-5/6">

    <div class="w-full bg-white rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0 dark:bg-gray-800 dark:border-gray-700">
      <div v-if="props.nflSeason" class="p-6 space-y-4 md:space-y-6 sm:p-8">
        
        <h1>{{nflSeason[0].team_division}}</h1>
        <table class="table-fixed border-separate border-spacing-2 ">
          <thead>

            <th class="border-b-2 p-2">Position</th>
            <th class="border-b-2 p-2">Team Name</th>
            <th class="border-b-2 p-2">Prediction Status</th>

          </thead>
          <tbody>
            <tr>
              <td>{{props.nflSeason[0].division_position}}</td>
              <td>{{props.nflSeason[0].team_name}}</td>
              <td>{{props.nflSeason[0].wins }}</td>
              <td>{{props.nflSeason[0].losses }}</td>
              <td>{{props.nflSeason[0].ties }}</td>
            </tr>
            <tr>
              <td>{{props.nflSeason[1].division_position}}</td>
              <td>{{props.nflSeason[1].team_name}}</td>
              <td>{{props.nflSeason[1].team_name  }}</td>
              <td>{{props.nflSeason[1].losses }}</td>
              <td>{{props.nflSeason[1].ties }}</td>
            </tr>
            <tr>
              <td>{{props.nflSeason[2].division_position}}</td>
              <td>{{props.nflSeason[2].team_name}}</td>
              <td>{{props.nflSeason[2].team_name  }}</td>
              <td>{{props.nflSeason[2].losses }}</td>
              <td>{{props.nflSeason[2].ties }}</td>
            </tr>
            <tr>
              <td>{{props.nflSeason[3].division_position}}</td>
              <td>{{props.nflSeason[3].team_name}}</td>
              <td>{{props.nflSeason[3].team_name }}</td>
              <td>{{props.nflSeason[3].losses }}</td>
              <td>{{props.nflSeason[3].ties }}</td>
            </tr>
          </tbody>
        </table>

      </div>
    </div>
  </div>

</template>