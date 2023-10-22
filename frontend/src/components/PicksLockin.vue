<script setup>
    const props = defineProps({
        regularSeason: Array,
    });

    const log = () => {
        console.log(props.regularSeason);
    };
</script>

<template>
    <div v-if="regularSeason">
        {{ props.regularSeason[0] }}
    </div>
    <div v-else>
        <p>No data available for AFC North</p>
    </div>
    <button @click="log">HELLO</button>
</template>
