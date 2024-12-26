<template>
  <section class="menu w-80 bg-base-200 justify-between min-h-0 h-full overflow-hidden p-0 transition-all">
    <!-- header -->
    <div class="m-2">
      <li>
        <a class="flex justify-between gap-2">
          创建新对话
          <div class="tooltip tooltip-left" data-tip="创建对话">
            <EditIcon width="18" @click.stop="createNewChat" />
          </div>
        </a>
      </li>
    </div>
    <!-- main -->
    <SidebarMain class="p-4" />
    <!-- footer -->
    <div class="border-t-[1px] border-base-300 m-2">
      <li class="mt-2"><a>升级</a></li>
      <li class="mt-2"><a>签到</a></li>
    </div>
  </section>
</template>

<script setup lang="ts">
// vue
import { ref } from "vue";
// 组件
import SidebarMain from "./SidebarMain.vue";
// 图标
import EditIcon from "@/assets/svg/edit.svg?component";
import CodeIcon from "@/assets/svg/code.svg?component";

/** 创建新对话 */
const createNewChat = () => {
  console.log("createNewChat");
};

</script>

<style scoped></style>
