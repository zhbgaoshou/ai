<template>
  <div class="w-full md:w-[80%] max-w-[768px] m-auto">
    <template v-for="message in messages" :key="message.id">
      <div class="chat chat-end my-5" v-if="message.role === 'user'">
        <div class="chat-bubble pre ">{{ message.content }}</div>
      </div>
      <div class="chat chat-start" v-else>
        <div class="placeholder chat-image avatar py-2">
          <div class="w-8 bg-base-200  rounded-full">
            <AiLogo />
          </div>
        </div>
        <div v-highlight class="chat-bubble prose bg-transparent max-w-full px-0"
          v-html="marked.parse(markdownContent = message.content)" />
      </div>
    </template>
    <!-- 生成中 -->
    <div class="chat chat-start" v-show="generateText">
      <div class="hidden md:block chat-image placeholder avatar py-2">
        <div class="w-8 bg-base-200  rounded-full">
          <AiLogo />
        </div>
      </div>
      <div v-highlight class="chat-bubble prose bg-transparent max-w-full px-0" v-html="marked.parse(generateText)">
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
// markdown
import { Marked } from "marked";
import AiLogo from "@/assets/svg/ai-logo.svg?component";

defineProps(['messages', 'generateText'])
// marked
const marked = new Marked();
let markdownContent = ref("");
</script>

<style>
.chat-bubble::before {
  display: none;
}

.pre {
  white-space: pre-wrap;
  /* 保留空格和换行 */
  overflow-wrap: break-word;
  /* 遇到长单词时允许换行，避免溢出 */
}

.chat-image {
  align-self: start;
}
</style>
