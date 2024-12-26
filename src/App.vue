<script setup lang="ts">
import Header from "./components/Header/index.vue";

</script>

<template>
  <div class=" flex flex-col justify-between h-full">
    <Header />
    <router-view class="flex-1" />
  </div>
</template>
