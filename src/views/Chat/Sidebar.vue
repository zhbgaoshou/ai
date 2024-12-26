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

    <ul class="flex-1 overflow-auto mt-5">
      <li class="menu-title">今天</li>
      <!-- 记录 -->
      <div class="dropdown dropdown-bottom dropdown-end w-full" v-for="i in 2">
        <li class="group">
          <a :class="{ focus: i === 1 }">
            <span class="text-ellipsis"
              >爱是自由意志的沉沦爱是自由意志的沉沦</span
            >
            <button
              :tabindex="0"
              class="more-drop"
              data-tip="更多操作"
              @click.stop
            >
              <MoreIcon />
            </button>
          </a>
        </li>
        <!-- 下拉菜单内容 -->
        <ul
          tabindex="0"
          class="dropdown-content menu bg-base-100 rounded-box z-[1] w-max p-2 shadow"
        >
          <li v-for="item in editData" :key="item.name">
            <a :class="{ 'text-error': item.name === '删除' }">
              <component :is="item.icon" width="18" />
              {{ item.name }}</a
            >
          </li>
        </ul>
      </div>
    </ul>

    <!-- footer -->
    <div class="border-t-[1px] border-base-300">
      <li class="mt-2"><a>升级</a></li>
      <li class="mt-2"><a>签到</a></li>
    </div>
  </section>
</template>

<script setup lang="ts">
// 图标
import EditIcon from "@/assets/svg/edit.svg?component";
import MoreIcon from "@/assets/svg/more.svg?component";
import DeleteIcon from "@/assets/svg/delete.svg?component";
import PenIcon from "@/assets/svg/pen.svg?component";

/** 创建新对话 */
const createNewChat = () => {
  console.log("createNewChat");
};

/** 操作数据 */
const editData = [
  { name: "删除", icon: DeleteIcon },
  { name: "重命名", icon: PenIcon },
];
</script>

<style scoped>
.text-ellipsis {
  /*1. 先强制一行内显示文本*/
  white-space: nowrap;
  /*2. 超出的部分隐藏*/
  overflow: hidden;
  /*3. 文字用省略号替代超出的部分*/
  text-overflow: ellipsis;
}
</style>
