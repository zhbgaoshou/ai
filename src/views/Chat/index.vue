<template>
  <div class="drawer min-h-0" :class="{ 'md:drawer-open': !isCollapse }">
    <input id="my-drawer" type="checkbox" class="drawer-toggle" />
    <div class="drawer-content flex flex-col min-h-0">
      <!-- 控制边栏 的按钮 -->
      <Header v-model="isCollapse" />
      <Main />
      <In v-model:content="content" />
    </div>
    <div class="drawer-side">
      <label for="my-drawer" aria-label="close sidebar" class="drawer-overlay"></label>
      <Sidebar @close-sidebar="isCollapse = true" />
    </div>
  </div>
</template>

<script setup lang="ts">
// vue
import { ref } from "vue";
// 组件
import Sidebar from "./Sidebar.vue";
import Header from "@/components/Header/index.vue";
import Main from "./Main.vue";
import In from "./In.vue";

// 边栏折叠操作
const isCollapse = ref(false);

// 数据
const content = ref("");
</script>

<style scoped></style>
