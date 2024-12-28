<script setup lang="ts">
import MoreIcon from "@/assets/svg/more.svg?component";
import DeleteIcon from "@/assets/svg/delete.svg?component";
import PenIcon from "@/assets/svg/pen.svg?component";
import AiLogoIcon from "@/assets/svg/ai-logo.svg?component";
import { ref, useTemplateRef, watch, nextTick } from "vue";


const props = defineProps(['categorizedRecords', 'isShowLoader'])
const emit = defineEmits(['toggleRecord', 'deleteRecord', 'editRecord', 'moreLoader'])
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
// 获取 loaderRef
const cb: IntersectionObserverCallback = (entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      // 如果目标进入视口
      emit('moreLoader')
    }
  });
}

watch(() => props.isShowLoader, async (newVal) => {
  if (newVal) {
    nextTick(() => {
      observer.observe(loaderRef.value as HTMLElement);
    })
  } else {
    stopObserver()
  }
})

const stopObserver = () => {
  observer.disconnect();
}
const loaderRef = useTemplateRef<HTMLSpanElement>('loaderRef')
const observer = new IntersectionObserver(cb, { threshold: 0.5, rootMargin: '50px' });
</script>

<template>
  <ul class="flex-1 overflow-auto mt-8 flex-nowrap">
    <!-- 今天 -->
    <li class="menu-title" v-if="categorizedRecords.today.length">今天</li>
    <li v-for="record in categorizedRecords.today" :key="record.id" class="group"
      @click="$emit('toggleRecord', record)">
      <!-- 主项 -->
      <a :class="{ active: record.is_active }">
        <AiLogoIcon />
        <span v-if="!record.is_edited" class="text-ellipsis">{{ record.name }}</span>
        <input v-else v-focus @blur="emitEditRecord(record)"
          @keydown.enter="(e) => (e.target as HTMLInputElement).blur()"
          class="input-xs input input-ghost w-full max-w-xs" type="text" v-model="record.name">

        <!-- 下拉按钮 -->
        <div class="dropdown dropdown-end">
          <label tabindex="0">
            <MoreIcon class="group-hover:visible" @click.stop :class="{ 'invisible': !record.is_active }" />
          </label>

          <!-- 下拉菜单 -->
          <ul tabindex="0" class="dropdown-content menu bg-base-100 rounded-box z-[1] w-max p-2 shadow">
            <li v-for="item in editData" :key="item.name" @click.stop="deleteOrEdit(record, item.name)">
              <a :class="{ 'text-error': item.name === '删除', 'text-info': item.name === '重命名' }">
                <component :is="item.icon" width="18" />
                {{ item.name }}
              </a>
            </li>
          </ul>
        </div>
      </a>
    </li>
    <!-- 昨天 -->
    <li class="menu-title" v-if="categorizedRecords.yesterday.length">昨天</li>
    <li v-for="record in categorizedRecords.yesterday" :key="record.id" class="group"
      @click="$emit('toggleRecord', record)">
      <!-- 主项 -->
      <a :class="{ active: record.is_active }">
        <AiLogoIcon />
        <span v-if="!record.is_edited" class="text-ellipsis">{{ record.name }}</span>
        <input v-else v-focus @blur="emitEditRecord(record)"
          @keydown.enter="(e) => (e.target as HTMLInputElement).blur()"
          class="input-xs input input-ghost w-full max-w-xs" type="text" v-model="record.name">

        <!-- 下拉按钮 -->
        <div class="dropdown dropdown-end">
          <label tabindex="0">
            <MoreIcon class="group-hover:visible" @click.stop :class="{ 'invisible': !record.is_active }" />
          </label>

          <!-- 下拉菜单 -->
          <ul tabindex="0" class="dropdown-content menu bg-base-100 rounded-box z-[1] w-max p-2 shadow">
            <li v-for="item in editData" :key="item.name" @click.stop="deleteOrEdit(record, item.name)">
              <a :class="{ 'text-error': item.name === '删除', 'text-info': item.name === '重命名' }">
                <component :is="item.icon" width="18" />
                {{ item.name }}
              </a>
            </li>
          </ul>
        </div>
      </a>
    </li>
    <!-- 更早 -->
    <li class="menu-title" v-if="categorizedRecords.earlier.length">更早</li>
    <li v-for="record in categorizedRecords.earlier" :key="record.id" class="group"
      @click="$emit('toggleRecord', record)">
      <!-- 主项 -->
      <a :class="{ active: record.is_active }">
        <AiLogoIcon />
        <span v-if="!record.is_edited" class="text-ellipsis">{{ record.name }}</span>
        <input v-else v-focus @blur="emitEditRecord(record)"
          @keydown.enter="(e) => (e.target as HTMLInputElement).blur()"
          class="input-xs input input-ghost w-full max-w-xs" type="text" v-model="record.name">

        <!-- 下拉按钮 -->
        <div class="dropdown dropdown-end">
          <label tabindex="0">
            <MoreIcon class="group-hover:visible" @click.stop :class="{ 'invisible': !record.is_active }" />
          </label>

          <!-- 下拉菜单 -->
          <ul tabindex="0" class="dropdown-content menu bg-base-100 rounded-box z-[1] w-max p-2 shadow">
            <li v-for="item in editData" :key="item.name" @click.stop="deleteOrEdit(record, item.name)">
              <a :class="{ 'text-error': item.name === '删除', 'text-info': item.name === '重命名' }">
                <component :is="item.icon" width="18" />
                {{ item.name }}
              </a>
            </li>
          </ul>
        </div>
      </a>
    </li>
    <!-- 底部加载更多 -->
    <li v-if="isShowLoader">
      <a class="flex justify-center">
        <span key="loaderRef" ref="loaderRef"></span>
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
</style>
