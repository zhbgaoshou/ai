<template>
    <!-- 未登录 -->
    <div v-if="!userStore.isLogin" class="avatar placeholder btn btn-sm btn-circle" @click="$emit('openAuthModal')">
        <div class="bg-neutral text-neutral-content w-8 rounded-full">
            <span class="text-xs">登录</span>
        </div>
    </div>
    <!-- 登录 -->


    <div v-else class="dropdown dropdown-end">
        <label tabindex="0" role="button" class="avatar placeholder btn btn-sm btn-circle">
            <div class="bg-neutral text-neutral-content w-8 rounded-full">
                <img v-if="userStore.info.avatar" :src="userStore.info.avatar" @error="avatarError" />
                <span v-else class="text-xs">{{ userStore.firstName }}</span>
            </div>
        </label>
        <ul tabindex="0" class="dropdown-content menu bg-base-100 rounded-box z-[1] w-52 p-2 shadow">
            <li v-for="item in profileData"><a>
                    <component :is="item.icon" width="16"></component>{{ item.title }}
                    <RightArrowIcon width="18" />
                </a></li>
            <div class="divider">OR</div>
            <li @click="userStore.logout"><a>
                    <LogoutIcon width="16" />退出登录
                    <RightArrowIcon width="18" />
                </a></li>

        </ul>
    </div>
</template>

<script setup lang="ts">
// 图标
import LogoutIcon from '@/assets/svg/logout.svg?component'
import RightArrowIcon from '@/assets/svg/right-arrow.svg?component'
import PieIcon from '@/assets/svg/pie.svg?component'


// store
import { useUserStore } from '@/store'
const userStore = useUserStore()
defineEmits(['openAuthModal'])

/** 头像处理 */
function avatarError() {
    userStore.info.avatar = ''
}

// profile
const profileData = [
    { title: '个人信息', icon: PieIcon, path: '/profile' },
]

</script>

<style scoped></style>