<template>
    <AuthAvatar @open-auth-modal="openAuthModal" />

    <!-- Open the modal using ID.showModal() method -->
    <dialog class="modal modal-bottom md:modal-middle" ref="modal">
        <div class="modal-box">
            <!-- 标签切换 -->
            <div role="tablist" class="tabs tabs-boxed" @click="toggleTab">
                <a role="tab" class="tab" data-source="login" :class="{ 'tab-active': isLoginTab }">登录</a>
                <a role="tab" class="tab" data-source="register" :class="{ 'tab-active': !isLoginTab }">注册</a>
            </div>
            <!-- 组件 -->
            <AuthLogin v-if="isLoginTab" @login="handleLogin" />
            <AuthRegister v-else @register="handleRegister" />
            <!-- 关闭 -->
            <div class="modal-action">
                <form method="dialog">
                    <button class="btn btn-xs btn-circle btn-ghost absolute right-1 top-1">✕</button>
                </form>
            </div>
        </div>
    </dialog>

    <!-- 登录成功弹窗 -->
    <div class="toast toast-top toast-end" v-if="isLogingSuccess">
        <div class="alert alert-info">
            <span class="flex gap-2">
                <SuccessIcon width="20" />{{ userStore.info.username }} 欢迎回来!!!
            </span>
        </div>
    </div>

    <!-- 注册成功弹窗 -->
    <div class="toast toast-top toast-end" v-if="isRegisterSuccess">
        <div class="alert alert-success">
            <span class="flex gap-2">
                <SuccessIcon width="20" />恭喜，注册成功!!!
            </span>
        </div>
    </div>
</template>

<script setup lang="ts">
// vue
import { ref } from 'vue'
// 组件
import AuthLogin from './AuthLogin.vue'
import AuthRegister from './AuthRegister.vue'
import AuthAvatar from './AuthAvatar.vue'
// 图标
import SuccessIcon from '@/assets/svg/success.svg?component'

// store
import { useUserStore } from "@/store";
const userStore = useUserStore()

/** 打开登录/注册弹窗 */
const modal = ref<HTMLDialogElement>()
function openAuthModal() {
    modal.value?.showModal()
}
/** 切换 注册/登录 modal*/
let isLoginTab = ref(true)
function toggleTab(e: Event) {
    const dataset = (e.target as HTMLElement).dataset
    const source = dataset.source
    source === 'login' ? isLoginTab.value = true : isLoginTab.value = false
}

/** 登录 or 注册 回调*/
let isLogingSuccess = ref(false)
async function handleLogin() {
    await userStore.login()

    if (userStore.isLogin) {
        isLogingSuccess.value = true
        modal.value?.close()
        const timer = setTimeout(() => {
            isLogingSuccess.value = false
            clearTimeout(timer)
        }, 2000)
    }
}
let isRegisterSuccess = ref(false)
async function handleRegister() {
    await userStore.register()

    isRegisterSuccess.value = true
    isLoginTab.value = true

    const timer = setTimeout(() => {
        isRegisterSuccess.value = false
        clearTimeout(timer)
    }, 2000)
}

</script>

<style scoped></style>