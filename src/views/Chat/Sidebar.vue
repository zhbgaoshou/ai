<template>
  <section class="menu w-72 bg-base-200 justify-between min-h-0 h-full overflow-hidden p-0 transition-all">
    <!-- header -->
    <div class="m-2">
      <li>
        <span class="flex justify-between gap-2">
          <div class="tooltip tooltip-right hidden md:block" data-tip="关闭边栏">
            <ExpandLeftIcon width="18" @click="$emit('closeSidebar')" />
          </div>
          <div class="tooltip tooltip-bottom" data-tip="新对话">
            <EditIcon width="18" @click.stop="createNewChat" />
          </div>
        </span>
      </li>

    </div>
    <!-- main -->
    <SidebarMain class="p-2" />
    <!-- footer -->
    <div class="border-t-[1px] border-base-300 m-2">
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
import ExpandLeftIcon from "@/assets/svg/expand-left.svg?component";

defineEmits(['closeSidebar'])
/** 创建新对话 */
const createNewChat = () => {
  console.log("createNewChat");
};

</script>

<style scoped></style>
