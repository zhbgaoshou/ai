<template>
    <div class="drawer min-h-0" :class="{ 'md:drawer-open': !isCollapse }">
        <input id="my-drawer" type="checkbox" class="drawer-toggle" />
        <div class="drawer-content relative">
            <Header />
            <!-- 控制边栏 的按钮 -->
            <div class="absolute top-[54px] left-2">
                <label for="my-drawer" class="drawer-button">
                    <ExpandLeftIcon class="md:hidden" />
                </label>
                <div class="tooltip tooltip-right" data-tip="展开/收缩">
                    <ExpandLeftIcon @click=" isCollapse = !isCollapse" class="md:block hidden"></ExpandLeftIcon>
                </div>
            </div>
        </div>
        <div class="drawer-side">
            <label for="my-drawer" aria-label="close sidebar" class="drawer-overlay"></label>
            <Sidebar />
        </div>
    </div>
</template>

<script setup lang="ts">
// vue
import { ref } from 'vue';
// 组件
import Sidebar from './Sidebar.vue';
import Header from "@/components/Header/index.vue";
// 图标
import ExpandLeftIcon from "@/assets/svg/expand-left.svg?component";

const isCollapse = ref(false);


</script>

<style scoped></style>