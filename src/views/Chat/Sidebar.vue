<template>
  <div class="relative h-full">
    <section
      class="menu bg-base-200 justify-between min-h-0 h-full overflow-hidden p-0 transition-all"
      :class="sideWidth"
    >
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

    <div
      class="tooltip tooltip-right absolute top-[40px] -right-4"
      data-tip="伸缩"
    >
      <button
        class="btn btn-circle btn-sm border-base-100"
        @click="toggleSidebar"
      >
        <CodeIcon width="18" />
      </button>
    </div>
  </div>
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
/** 侧边栏 展开/收起 */
let sideWidth = ref("w-64");
function toggleSidebar() {
  sideWidth.value = sideWidth.value === "w-64" ? "w-0" : "w-64";
}
</script>

<style scoped></style>
