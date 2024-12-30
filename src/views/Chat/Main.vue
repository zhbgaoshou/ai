<template>
  <div class="w-full md:w-[80%] m-auto">
    <div class="chat chat-end my-5">
      <div class="chat-bubble pre"></div>
    </div>
    <div class="chat chat-start">
      <div
        v-highlight
        class="chat-bubble prose bg-transparent max-w-full"
        v-html="markdownContent"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from "vue";
// markdown
import { Marked } from "marked";
// 组件

// marked
const marked = new Marked();

let markdownText = ref("");
const markdownContent = computed(() => {
  return marked.parse(markdownText.value);
});
</script>

<style scoped>
.chat-bubble::before {
  display: none;
}

.pre {
  white-space: pre-wrap;
  /* 保留空格和换行 */
  overflow-wrap: break-word;
  /* 遇到长单词时允许换行，避免溢出 */
}
</style>
