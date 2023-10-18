<script setup>
  import Navbar from './components/Navbar.vue';
  import router from './router/index.js'
</script>


<template>

  <Navbar/>

  <div class="bg-indigo-500 text-black">
    App.Vue
  </div>

  <router-view></router-view>

</template>

<style scoped>

</style>
