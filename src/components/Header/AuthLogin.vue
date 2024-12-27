<template>
    <form @submit.prevent="$emit('login')">
        <label class="input input-bordered flex items-center gap-2 m-4 rounded-box">
            <UserIcon width="18" />
            <input type="text" class="grow" placeholder="用户名" v-model="userStore.authData.username" required />
        </label>
        <label class="input input-bordered flex items-center gap-2 m-4 rounded-box">
            <PasswordIcon width="18" />
            <input :type="showPassword ? 'text' : 'password'" class="grow" placeholder="密码"
                v-model="userStore.authData.password" required minlength="6" />
            <label class="swap swap-flip">
                <!-- this hidden checkbox controls the state -->
                <input type="checkbox" v-model="showPassword" />
                <!-- sun icon -->
                <EyeIcon class="swap-off" width="20" />
                <EyeOffIcon class="swap-on" width="20" />
            </label>
        </label>

        <div class="flex gap-2 m-2 mt-8">
            <button class="btn btn-info flex-1">登录
                <LoginIcon width="18" />
            </button>
            <button class="btn" type="reset">重置
                <RefreshIcon width="18" />
            </button>
        </div>
    </form>
</template>

<script setup lang="ts">
// vue
import { ref } from "vue";
// 图标
import UserIcon from "@/assets/svg/user.svg?component";
import PasswordIcon from "@/assets/svg/password.svg?component";
import RefreshIcon from "@/assets/svg/refresh.svg?component";
import LoginIcon from "@/assets/svg/login.svg?component";
import EyeIcon from "@/assets/svg/eye.svg?component";
import EyeOffIcon from "@/assets/svg/eye-off.svg?component";
// store
import { useUserStore } from "@/store";
const userStore = useUserStore()

defineEmits(['login'])

// 密码显示隐藏
let showPassword = ref(false)

</script>

<style scoped></style>