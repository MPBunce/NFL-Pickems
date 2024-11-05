<script setup lang="ts">

  import { GoogleSignInButton, type CredentialResponse} from "vue3-google-signin";
  import { authStore } from '../store/authStore.js'
  import { ref } from 'vue';
  import router from "../router/index.js";

  const auth = authStore()

  const handleLoginSuccess = (response: CredentialResponse) => {
    const { credential } = response;
    console.log("Access Token", credential);
    auth.setToken(credential)
    router.push({name: 'SeasonPicks'})
  };

  const handleLoginError = () => {
    console.error("Login failed");
  };

</script>

<template>
  <GoogleSignInButton
    @success="handleLoginSuccess"
    @error="handleLoginError"
  ></GoogleSignInButton>
</template>
