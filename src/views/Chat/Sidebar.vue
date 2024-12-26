<template>
  <section class="menu bg-base-200 w-64 justify-between min-h-0">
    <!-- header -->
    <div>
      <li>
        <a class="flex justify-between gap-2">
          创建新对话
          <div class="tooltip tooltip-right" data-tip="创建对话">
            <EditIcon width="18" @click.stop="createNewChat" />
          </div>
        </a>
      </li>
    </div>

    <!-- main -->
    <SidebarMain />

    <!-- footer -->
    <div class="border-t-[1px] border-base-300">
      <li class="mt-2"><a>升级</a></li>
      <li class="mt-2"><a>签到</a></li>
    </div>
  </section>
</template>

<script setup lang="ts">
// 组件
import SidebarMain from "./SidebarMain.vue";
// 图标
import EditIcon from "@/assets/svg/edit.svg?component";

/** 创建新对话 */
const createNewChat = () => {
  console.log("createNewChat");
};
</script>

<style scoped></style>
