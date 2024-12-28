<template>
    <details class="dropdown dropdown-top dropdown-open" ref="dropdownRef" v-on-click-outside="closeDropdown">
        <summary class="btn btn-sm text-sm font-normal">
            {{ userStore.defaultModel.name }}
            <ChvronUpIcon width="20" />
        </summary>
        <ul class="dropdown-content menu bg-base-100 rounded-box z-[1] w-60 p-2 shadow">
            <li v-for="model in models" @click="userStore.setDefaultModel(model)">
                <a>
                    <span></span>
                    <div>
                        {{ model.name }}
                        <p class=" text-xs opacity-50">
                            {{ model.description }}
                        </p>
                    </div>
                    <SuccessUpIcon width="20" v-show="userStore.defaultModel.id === model.id" />
                    <button class="btn btn-sm rounded-full" v-if="model.is_vip && !userStore.isSupperUser">
                        升级
                    </button>
                </a>
            </li>
        </ul>
    </details>
</template>

<script setup lang="ts">
import ChvronUpIcon from "@/assets/svg/chvron-up.svg?component";
import SuccessUpIcon from "@/assets/svg/success.svg?component";
import { useUserStore } from '@/store'
import { ref } from "vue";
import { vOnClickOutside } from '@vueuse/components'


const userStore = useUserStore()
defineProps(['models'])
defineEmits(['toggelModel'])
const dropdownRef = ref<HTMLElement>()

const closeDropdown = () => {
    dropdownRef.value?.removeAttribute('open')
}
</script>
