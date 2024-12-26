<template>
    <header class="navbar bg-base-100 shadow-sm min-h-12">
        <!-- 左边 -->
        <div class="flex-1">
            <ToolButton v-for="item in toolData" :key="item.title" :tip="item.title">
                <component :is="item.icon" width="18" />
            </ToolButton>
        </div>
        <!-- 右边 -->
        <div class="flex-none gap-2">
            <!-- 主题切换 -->
            <div class="dropdown dropdown-end">
                <div tabindex="0" role="button">
                    <div class="tooltip tooltip-left flex items-center" data-tip="主题切换">
                        <ThemeIcon />
                    </div>
                </div>
                <ul tabindex="0" class="dropdown-content menu bg-base-100 rounded-box z-[1] w-52 p-2 shadow">
                    <li v-for="themeProp, themeName in themes" @click="settingsStore.setTheme(themeName)">
                        <a>
                            <SuccessIcon width="16" v-if="themeName === settingsStore.currentTheme" />
                            <span :style="{ fontFamily: themeProp.fontFamily }">{{ themeName }}</span>
                        </a>
                    </li>
                </ul>
            </div>
            <!-- auth -->
            <Auth />
        </div>
    </header>


</template>

<script setup lang="ts">
// vue
import { computed } from 'vue'
// 引入组件
import ToolButton from '@/components/base/ToolButton.vue'
import Auth from './Auth.vue'
// 引入图标
import MailIcon from '@/assets/svg/mail.svg?component'
import MessageIcon from '@/assets/svg/message.svg?component'
import ThemeIcon from '@/assets/svg/theme.svg?component'
import SuccessIcon from '@/assets/svg/success.svg?component'


// store
import { useSettingsStore } from '@/store'

const settingsStore = useSettingsStore()

/** 主题设置 */
const themes = computed(() => settingsStore.getTheme())

/** 左边的工具栏数据 */
const toolData = [
    {
        icon: MailIcon,
        title: '反馈',
    },
    {
        icon: MessageIcon,
        title: '联系我',
    },
]
</script>

<style scoped></style>