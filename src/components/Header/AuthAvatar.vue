<template>
    <div class="avatar placeholder btn btn-sm btn-circle" @click="$emit('openAuthModal')">
        <div class="bg-neutral text-neutral-content w-8 rounded-full">
            <span class="text-xs">登录</span>
        </div>
    </div>
</template>

<script setup lang="ts">
defineEmits(['openAuthModal'])

</script>

<style scoped></style>