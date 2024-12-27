<template>
  <header class="navbar bg-base-100 shadow-sm min-h-12">
    <!-- 左边 -->
    <div class="flex-1 gap-1">
      <ToggleSideBar v-model="isCollapse" />
      <ToolButton v-for="item in toolData" :key="item.title" :tip="item.title">
        <component :is="item.icon" width="18" />
      </ToolButton>
    </div>
    <!-- 右边 -->
    <div class="flex-none gap-2">
      <!-- 主题切换 -->
      <div class="dropdown dropdown-end">
        <div tabindex="0" role="button">
          <div
            class="tooltip tooltip-left flex items-center"
            data-tip="主题切换"
          >
            <ThemeIcon width="20" />
          </div>
        </div>

        <ThemeMain />
      </div>
      <!-- auth -->
      <Auth />
    </div>
  </header>
</template>

<script setup lang="ts">
// 引入组件
import ToolButton from "@/components/base/ToolButton.vue";
import Auth from "./Auth.vue";
import ThemeMain from "./ThemeMain.vue";
import ToggleSideBar from "./ToggleSideBar.vue";
// 引入图标
import MailIcon from "@/assets/svg/mail.svg?component";
import MessageIcon from "@/assets/svg/message.svg?component";
import ThemeIcon from "@/assets/svg/theme.svg?component";

/** 左边的工具栏数据 */
const toolData = [
  {
    icon: MailIcon,
    title: "反馈",
  },
  {
    icon: MessageIcon,
    title: "联系我",
  },
];

const isCollapse = defineModel();
</script>

<style scoped></style>
