<script setup lang="ts">
import ToolButton from "@/components/base/ToolButton.vue";
import ExpandLeftIcon from "@/assets/svg/expand-left.svg?component";
const isCollapse = defineModel();
</script>

<template>
  <!-- h5 -->

  <label
    for="my-drawer"
    class="drawer-button md:hidden btn btn-ghost btn-sm btn-circle flex items-center -translate-y-[2px]"
  >
    <ExpandLeftIcon width="18" />
  </label>

  <!-- pc -->
  <ToolButton
    tip="打开边栏"
    class="md:block hidden tooltip-right"
    v-show="isCollapse"
    @click="isCollapse = !isCollapse"
  >
    <ExpandLeftIcon width="18" />
  </ToolButton>
</template>
