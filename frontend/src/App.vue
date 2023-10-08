<script setup>
  import HelloWorld from './components/HelloWorld.vue'
  import axios from 'axios';
  const data = {
    responseData: null
  };

  const fetchData = () => {
  fetch('/')
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then(data => {
      // Handle the response data
      responseData.value = data; // Assuming you're using Vue 3 Composition API
    })
    .catch(error => {
      console.error('There was a problem with the fetch operation:', error);
    });
};

</script>


<template>
  <div>
    <a href="https://vitejs.dev" target="_blank">
      <img src="./assets/vue.svg" class="logo" alt="Vite logo" />
    </a>
    <a href="https://vuejs.org/" target="_blank">
      <img src="./assets/vue.svg" class="logo vue" alt="Vue logo" />
    </a>
  </div>
  <HelloWorld msg="Vite + Vue from github actions" />

  <div>
    <button @click="fetchData">Fetch Data</button>
    <div>{{ responseData }}</div>
  </div>

</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
