<template>
    <div class="chat-image avatar placeholder">
        <div class="bg-neutral rounded-full" :class="`w-${size}`">
            <img :src="src" v-if="src" @error="src = ''" />
            <span v-else>{{ errorChar || 'Z' }}</span>
        </div>
    </div>
</template>

<script setup lang="ts">
defineProps(['size', 'errorChar'])
const src = defineModel<string>()
</script>

<style scoped></style>