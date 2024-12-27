<script setup lang="ts">
import MoreIcon from "@/assets/svg/more.svg?component";
import DeleteIcon from "@/assets/svg/delete.svg?component";
import PenIcon from "@/assets/svg/pen.svg?component";
import AiLogoIcon from "@/assets/svg/ai-logo.svg?component";
import { ref } from "vue";

defineProps(['records'])
const emit = defineEmits(['toggleRecord', 'deleteRecord', 'editRecord'])
/** 操作数据 */
const editData = [
  { name: "删除", icon: DeleteIcon },
  { name: "重命名", icon: PenIcon },
];
const oldRecord = ref({ name: '' })
function deleteOrEdit(record: any, name: string) {
  if (name === "删除") {
    // 删除
    emit('deleteRecord', record)
  } else {
    oldRecord.value = { ...record }
    // 重命名
    record.is_edited = !record.is_edited
  }
}
/** 编辑 */
// 定义自定义指令 v-focus
const vFocus = {
  mounted(el: HTMLElement) {
    el.focus(); // 在元素绑定到 DOM 后直接聚焦
  },
  updated(el: HTMLElement) {
    el.focus(); // 在绑定数据变化时再次聚焦
  },
};
function emitEditRecord(record: any) {
  record.is_edited = false
  if (record.name === oldRecord.value.name) return
  emit('editRecord', record)
}


</script>

<template>
  <ul class="menu flex-1 overflow-auto mt-8">
    <li class="menu-title">今天</li>

    <!-- 用 v-for 循环 records -->
    <li v-for="record in records" :key="record.id" class="group" @click="$emit('toggleRecord', record)">
      <!-- 主项 -->
      <a :class="{ active: record.is_active }">
        <AiLogoIcon />
        <span v-if="!record.is_edited" class="text-ellipsis">{{ record.name }}</span>
        <input v-else v-focus @blur="emitEditRecord(record)" class="input-xs input input-ghost w-full max-w-xs"
          type="text" v-model="record.name">

        <!-- 下拉按钮 -->
        <div class="dropdown dropdown-end">
          <label tabindex="0">
            <MoreIcon class="group-hover:visible" @click.stop />
          </label>

          <!-- 下拉菜单 -->
          <ul tabindex="0" class="dropdown-content menu bg-base-100 rounded-box z-[1] w-max p-2 shadow">
            <li v-for="item in editData" :key="item.name" @click.stop="deleteOrEdit(record, item.name)">
              <a :class="{ 'text-error': item.name === '删除' }">
                <component :is="item.icon" width="18" />
                {{ item.name }}
              </a>
            </li>
          </ul>
        </div>
      </a>
    </li>
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

.menu :where(li ul):before {
  width: 0;
}
</style>
