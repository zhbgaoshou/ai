<template>
  <div class="drawer min-h-0" :class="{ 'md:drawer-open': !isCollapse }">
    <input id="my-drawer" type="checkbox" class="drawer-toggle" />
    <div class="drawer-content flex flex-col min-h-0">
      <!-- 控制边栏 的按钮 -->
      <Header v-model="isCollapse" />
      <div class="overflow-auto flex-1">
        <Main />
      </div>
      <In v-model:content="content" :models="userStore.models" />
    </div>
    <div class="drawer-side">
      <label for="my-drawer" aria-label="close sidebar" class="drawer-overlay"></label>
      <Sidebar @close-sidebar="isCollapse = true" />
    </div>
  </div>
</template>

<script setup lang="ts">
// vue
import { ref, onMounted } from "vue";
// 组件
import Sidebar from "./Sidebar.vue";
import Header from "@/components/Header/index.vue";
import Main from "./Main.vue";
import In from "./In.vue";
// store
import { useUserStore } from "@/store";
const userStore = useUserStore();

// 边栏折叠操作
const isCollapse = ref(false);

// 数据
const content = ref("");

// 获取模型列表
function getModels() {
  userStore.getModels();
}
onMounted(() => {
  getModels();
});
</script>

<style scoped></style>
