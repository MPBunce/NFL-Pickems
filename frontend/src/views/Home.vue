<script setup>

    import { ref, onMounted } from 'vue';
    import { authStore } from '../store/authStore';
    const authStoreInstance = authStore();
    const res = ref(null);

    onMounted(async () => {
        res.value = await authStoreInstance.test();
    });

</script>

<template>
    <div>
      hello home
      <p>{{ res }}</p>
    </div>
    <button @click="console.log(res)">log res</button>
</template>

