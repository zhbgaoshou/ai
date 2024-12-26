<template>
    <ul tabindex="0" class="dropdown-content menu bg-base-100 rounded-box z-[1] w-64 p-2 shadow">
        <li v-for="themeProp, themeName in themes" @click="settingsStore.setTheme(themeName)">
            <a>
                <SuccessIcon width="16" :class="themeName == settingsStore.currentTheme ? 'visible' : 'invisible'" />
                <span :style="{ fontFamily: themeProp.fontFamily }">{{ themeName }}</span>

                <div class="flex justify-center items-center gap-1">
                    <span class="block w-4 h-4 rounded-full" :style="{
                        backgroundColor: themeProp.primary,
                        'border-radius': themeProp['--rounded-badge'],
                    }"></span>
                    <span class="block w-4 h-4 rounded-full" :style="{
                        backgroundColor: themeProp.secondary,
                        'border-radius': themeProp['--rounded-box'],
                    }"></span>
                    <span class="block w-4 h-4 rounded-full" :style="{
                        backgroundColor: themeProp.accent,
                        'border-radius': themeProp['--rounded-btn'],
                    }"></span>
                    <span class="block w-4 h-4 rounded-full" :style="{
                        backgroundColor: themeProp.neutral,
                        'border-radius': themeProp['--tab-radius'],
                    }"></span>
                </div>
            </a>
        </li>
    </ul>
</template>

<script setup lang="ts">
// vue
import { computed } from 'vue'
// 图标
import SuccessIcon from '@/assets/svg/success.svg?component'
// store
import { useSettingsStore } from '@/store'

const settingsStore = useSettingsStore()

/** 主题设置 */
const themes = computed(() => settingsStore.getTheme())
</script>

<style scoped></style>