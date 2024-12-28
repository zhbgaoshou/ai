<template>
  <div class="flex-1 min-h-0 overflow-auto w-full md:w-[80%] m-auto">
    <div class="chat chat-end">
      <div class="chat-image">
        <Avatar v-model="src" size="8" :error-char="userStore.firstName" />
      </div>
      <div class="chat-bubble">It's over Anakin, I have the high ground.</div>
    </div>
    <div class="chat chat-start">
      <div class="chat-image">
        <Avatar size="8" error-char="AI" />
      </div>
      <div class="chat-bubble">You underestimate my power!</div>
    </div>
  </div>

</template>

<script setup lang="ts">
import { ref } from 'vue';
// 组件
import Avatar from '@/components/base/Avatar.vue';
import { useUserStore } from '@/store';
const userStore = useUserStore();

const src = ref('');
</script>

<style scoped>
.chat-bubble::before {
  display: none;
}
</style>
