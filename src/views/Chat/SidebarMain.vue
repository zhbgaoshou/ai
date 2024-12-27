<script setup lang="ts">
import MoreIcon from "@/assets/svg/more.svg?component";
import DeleteIcon from "@/assets/svg/delete.svg?component";
import PenIcon from "@/assets/svg/pen.svg?component";
import AiLogoIcon from "@/assets/svg/ai-logo.svg?component";

/** 操作数据 */
const editData = [
  { name: "删除", icon: DeleteIcon },
  { name: "重命名", icon: PenIcon },
];
</script>

<template>
  <ul class="flex-1 overflow-auto mt-8">
    <li class="menu-title">今天</li>
    <!-- 记录 -->
    <div class="dropdown dropdown-bottom dropdown-end w-full" v-for="i in 2">
      <li class="group">
        <a :class="{ active: i === 1 }">
          <AiLogoIcon />
          <span class="text-ellipsis"
            >爱是自由意志的沉沦爱是自由意志的沉沦</span
          >

          <button
            :tabindex="0"
            class="more-drop"
            data-tip="更多操作"
            @click.stop
          >
            <MoreIcon
              class="group-hover:visible"
              :class="{ invisible: i !== 1 }"
            />
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
            {{ item.name }}
          </a>
        </li>
      </ul>
    </div>
  </ul>
</template>

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
