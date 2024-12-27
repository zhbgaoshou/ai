<template>
  <div class="drawer min-h-0" :class="{ 'md:drawer-open': !isCollapse }">
    <input id="my-drawer" type="checkbox" class="drawer-toggle" />
    <div class="drawer-content flex flex-col min-h-0">
      <!-- 控制边栏 的按钮 -->
      <Header v-model="isCollapse" />
      <Main />
      <input type="text" class="h-[100px]" value="iioo" />
    </div>
    <div class="drawer-side">
      <label
        for="my-drawer"
        aria-label="close sidebar"
        class="drawer-overlay"
      ></label>
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
// 图标

// 边栏折叠操作
const isCollapse = ref(false);
</script>

<style scoped></style>
