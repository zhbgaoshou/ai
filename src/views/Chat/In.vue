<template>
    <div class="flex justify-center p-2">
        <div class="w-[90%] bg-base-200 p-2 rounded-[20px]">
            <form>
                <textarea @input="inputChange" ref="textareaRef" key="textareaRef" v-model.trim="content"
                    class="bg-transparent h-12 w-full p-2 outline-none resize-none max-h-80 format-text"
                    placeholder="想问点什么呢"></textarea>
            </form>
            <!-- 工具 -->
            <div class="flex justify-between items-center">
                <section class="flex items-center gap-2">
                    <!-- 附件 -->
                    <div class="dropdown dropdown-hover dropdown-top">
                        <div tabindex="0" role="button" class="btn btn-sm btn-circle"
                            :class="{ 'btn-disabled': recordStore.activeRecord.model !== 'gpt-4o' }">
                            <AttaIcon width="20" height="20" />
                        </div>
                        <div tabindex="0" v-show="recordStore.activeRecord.model !== 'gpt-4o'"
                            class="dropdown-content card card-compact bg-primary text-primary-content z-[1] w-64 p-2 shadow">
                            <div class="card-body">
                                当前模型不支持附件，请切换到 gpt-4o 模型
                            </div>
                        </div>
                    </div>
                    <!-- 模型 -->
                    <ModelView :models="models" />
                </section>
                <!-- 发送 -->
                <div class="tooltip tooltip-base-content tooltip-left" :data-tip="content ? '发送' : '内容为空'">
                    <button class="btn btn-sm btn-circle" :class="{ 'btn-disabled': !content }">
                        <UpIcon width="20" />
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
// vue
import { useTemplateRef, ref } from "vue";
// 图标
import UpIcon from "@/assets/svg/up.svg?component";
import AttaIcon from "@/assets/svg/atta.svg?component";

// 组件
import ModelView from "./ModelView.vue";
// store
import { useRecordStore } from '@/store'
const recordStore = useRecordStore()



const content = defineModel<string>('content')
defineProps(['models'])

// 监听 textarea 的内容变化
const textareaRef = useTemplateRef<HTMLTextAreaElement>('textareaRef')
function inputChange() {
    if (textareaRef.value!.scrollHeight <= 48 || !content.value) {
        return textareaRef.value!.style.height = '48px'
    }
    textareaRef.value!.style.height = 'auto'
    textareaRef.value!.style.height = textareaRef.value!.scrollHeight + 'px'
}

</script>

<style scoped>
.format-text {
    white-space: pre-wrap;
    /* 保留空格和换行 */
    word-wrap: break-word;
    /* 自动换行（可选） */
}
</style>
