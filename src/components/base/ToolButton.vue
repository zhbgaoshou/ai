<template>
    <div class="tooltip gap-1 tooltip-bottom" :data-tip="tip">
        <button class=" btn btn-ghost btn-sm btn-circle">
            <slot></slot>
        </button>
    </div>
</template>

<script setup lang="ts">
defineProps({
    tip: String,
})
</script>
