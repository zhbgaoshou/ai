<template>
  <div class="w-full md:w-[80%] m-auto h-full">
    <div class="chat chat-end my-5">
      <div class="chat-bubble">
        212
      </div>
    </div>
    <div class="chat chat-start">
      <div class="chat-bubble prose bg-transparent max-w-full" v-html="markdownContent" />
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue';
// markdown
import { Marked, type MarkedOptions } from 'marked';
import hljs from "highlight.js"; // 导入 highlight.js
import "highlight.js/styles/github.css"; // 引入 Highlight.js 的样式
// 组件

// marked
import axios from 'axios';

const marked = new Marked({});

let markdownText = ref("1")
const markdownContent = computed(() => {
  return marked.parse(markdownText.value);
})
axios.get('/demo.md').then(res => {
  markdownText.value = res.data
  console.log(markdownContent.value)
})
// 配置 marked 使用 highlight.js，强制类型断言以解决类型错误
marked.setOptions({
  highlight: (code: string, lang: string) => {
    if (lang && hljs.getLanguage(lang)) {
      return hljs.highlight(code, { language: lang }).value;
    }
    return hljs.highlightAuto(code).value; // 自动检测语言
  },
  langPrefix: "hljs language-", // 为代码块添加 hljs 的样式类
} as MarkedOptions); // 强制类型断言为 MarkedOptions
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
