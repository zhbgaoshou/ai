<template>
    <div class="drawer min-h-0" :class="{ 'md:drawer-open': !isCollapse }">
        <input id="my-drawer" type="checkbox" class="drawer-toggle" />
        <div class="drawer-content relative">
            <Header />
            <!-- 控制边栏 的按钮 -->
            <div class="absolute top-[54px] left-2">
                <!-- h5 -->
                <label for="my-drawer" class="drawer-button">
                    <ExpandLeftIcon width="18" class="md:hidden" />
                </label>
                <!-- pc -->
                <div class="tooltip tooltip-right" data-tip="打开边栏">
                    <ExpandLeftIcon width="18" v-show="isCollapse" @click=" isCollapse = !isCollapse"
                        class="md:block hidden" />
                </div>
            </div>
        </div>
        <div class="drawer-side">
            <label for="my-drawer" aria-label="close sidebar" class="drawer-overlay"></label>
            <Sidebar @close-sidebar="isCollapse = true" />
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

// 边栏折叠操作
const isCollapse = ref(false);


</script>

<style scoped></style>