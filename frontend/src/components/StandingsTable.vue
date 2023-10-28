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

  <div class="flex flex-col items-center justify-center py-6 px-6 mx-auto">

    <div class="w-full bg-neutral-800 rounded">
      <div v-if="props.nflSeason" class="p-6 space-y-4 md:space-y-6 sm:p-8">
      
        <div class="text-center">
          <h1 class="my-2 text-white text-2xl font-mono">{{nflSeason[0].team_division}}</h1>
        </div>

        <table class="table-auto">
          <thead>

            <th class="border-b-2 p-2">Position</th>
            <th class="border-b-2 p-2">Team Name</th>
            <th class="border-b-2 p-2">Wins</th>
            <th class="border-b-2 p-2">Losses</th>
            <th class="border-b-2 p-2">Ties</th>
          </thead>
          <tbody>
            <tr>
              <td className="p-4 " >{{props.nflSeason[0].divisional_position}}</td>
              <td className="p-4 ">{{props.nflSeason[0].team_name}}</td>
              <td className="p-4 ">{{props.nflSeason[0].wins }}</td>
              <td className="p-4 ">{{props.nflSeason[0].losses }}</td>
              <td className="p-4 ">{{props.nflSeason[0].ties }}</td>
            </tr>
            <tr class="">
              <td className="p-4 ">{{props.nflSeason[1].divisional_position}}</td>
              <td className="p-4 ">{{props.nflSeason[1].team_name}}</td>
              <td className="p-4 ">{{props.nflSeason[1].wins }}</td>
              <td className="p-4 ">{{props.nflSeason[1].losses }}</td>
              <td className="p-4 ">{{props.nflSeason[1].ties }}</td>
            </tr>
            <tr>
              <td className="p-4 ">{{props.nflSeason[2].divisional_position}}</td>
              <td className="p-4 ">{{props.nflSeason[2].team_name}}</td>
              <td className="p-4 ">{{props.nflSeason[2].wins }}</td>
              <td className="p-4 ">{{props.nflSeason[2].losses }}</td>
              <td className="p-4 ">{{props.nflSeason[2].ties }}</td>
            </tr>
            <tr>
              <td className="p-4 ">{{props.nflSeason[3].divisional_position}}</td>
              <td className="p-4 ">{{props.nflSeason[3].team_name}}</td>
              <td className="p-4 ">{{props.nflSeason[3].wins }}</td>
              <td className="p-4 ">{{props.nflSeason[3].losses }}</td>
              <td className="p-4 ">{{props.nflSeason[3].ties }}</td>
            </tr>
          </tbody>
        </table>

      </div>
    </div>
  </div>

</template>