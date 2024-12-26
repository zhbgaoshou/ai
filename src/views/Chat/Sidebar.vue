<template>
    <section class="menu bg-base-200 w-64 justify-between min-h-0">
        <!-- header -->
        <div>
            <li>
                <a class="flex justify-between gap-2">
                    创建新对话
                    <div class="tooltip tooltip-right" data-tip="创建对话">
                        <EditIcon width="18" @click.stop="createNewChat" />
                    </div>
                </a>
            </li>
        </div>

        <!-- main -->

        <ul class="flex-1 overflow-auto mt-5">
            <li class="menu-title">今天</li>
            <li v-for="i in 10"><a>Item 1</a></li>
        </ul>

        <!-- footer -->
        <div class="border-t-[1px]">
            <li class="mt-2"><a>升级套餐</a></li>
        </div>
    </section>
</template>

<script setup lang="ts">
import EditIcon from '@/assets/svg/edit.svg?component'

/** 创建新对话 */
const createNewChat = () => {
    console.log('createNewChat')
}

</script>

<style scoped></style>