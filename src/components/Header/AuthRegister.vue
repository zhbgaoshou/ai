<template>
    <form>
        <label class="input input-bordered flex items-center gap-2 m-4 rounded-box">
            <UserIcon width="18" />
            <input type="text" class="grow" placeholder="用户名" v-model="userStore.authData.username" />
        </label>
        <label class="input input-bordered flex items-center gap-2 m-4 rounded-box">
            <PasswordIcon width="18" />
            <input :type="showPassword ? 'text' : 'password'" class="grow" placeholder="密码"
                v-model="userStore.authData.password" />
            <label class="swap swap-flip">
                <!-- this hidden checkbox controls the state -->
                <input type="checkbox" v-model="showPassword" />
                <!-- sun icon -->
                <EyeIcon class="swap-off" width="20" />
                <EyeOffIcon class="swap-on" width="20" />
            </label>
        </label>
        <label class="input input-bordered flex items-center gap-2 m-4 rounded-box">
            <MailIcon width="18" />
            <input type="email" class="grow" placeholder="邮箱地址" v-model="userStore.authData.email" />
        </label>

        <div class="flex gap-2 m-2 mt-8">
            <button class="btn btn-success flex-1" @click="$emit('register')">注册
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
import { ref, onMounted } from "vue";
// 图标
import UserIcon from "@/assets/svg/user.svg?component";
import PasswordIcon from "@/assets/svg/password.svg?component";
import RefreshIcon from "@/assets/svg/refresh.svg?component";
import LoginIcon from "@/assets/svg/login.svg?component";
import MailIcon from '@/assets/svg/mail.svg?component'
import EyeIcon from "@/assets/svg/eye.svg?component";
import EyeOffIcon from "@/assets/svg/eye-off.svg?component";

// store
import { useUserStore } from "@/store";
const userStore = useUserStore()

defineEmits(['register'])

/**
 * 密码是否显示
*/
let showPassword = ref(false)

onMounted(() => {
    userStore.resetAuthData()
})

</script>

<style scoped></style>