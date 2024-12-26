<template>
    <div v-if="!userStore.isLogin" class="avatar placeholder btn btn-sm btn-circle" @click="$emit('openAuthModal')">
        <div class="bg-neutral text-neutral-content w-8 rounded-full">
            <span class="text-xs">登录</span>
        </div>
    </div>

    <div v-else class="avatar placeholder btn btn-sm btn-circle">
        <div class="bg-neutral text-neutral-content w-8 rounded-full">
            <img v-if="userStore.info.avatar" :src="userStore.info.avatar" @error="avatarError" />
            <span v-else class="text-xs">{{ userStore.firstName }}</span>
        </div>
    </div>
</template>

<script setup lang="ts">
// store
import { useUserStore } from '@/store'
const userStore = useUserStore()
defineEmits(['openAuthModal'])

/** 头像处理 */
function avatarError() {
    userStore.info.avatar = ''
}

</script>

<style scoped></style>