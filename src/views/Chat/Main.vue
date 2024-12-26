<template>
    <div class="flex-1 min-h-0 overflow-auto px-5">
        <div class="chat chat-end" v-for="i in 20">
            <div class="chat-bubble">
                It's over Anakin,
                I have the high ground.
            </div>
        </div>
        <div class="chat chat-start" v-for="i in 20">
            <div class="chat-bubble">You underestimate my power!</div>
        </div>
    </div>
</template>

<script setup lang="ts">
// 图标


</script>

<style scoped>
.chat-bubble::before {
    display: none;
}
</style>