<template>
  <section
    class="menu w-72 bg-base-100 justify-between min-h-0 h-full overflow-hidden transition-all shadow-sm border-[1px] border-base-200">
    <!-- header -->

    <li>
      <span class="flex justify-between gap-2">
        <div class="tooltip tooltip-right hidden md:block" data-tip="关闭边栏">
          <ExpandLeftIcon width="18" @click="$emit('closeSidebar')" />
        </div>
        <div class="tooltip tooltip-bottom" data-tip="新对话">
          <EditIcon width="18" @click.stop="createNewChat" />
        </div>
      </span>
    </li>

    <!-- main -->
    <SidebarMain :records="recordStore.records" @toggle-record="toggleRecord" @delete-record="deleteRecord"
      @edit-record="editRecord" />
    <!-- footer -->
    <div class="border-t-[1px] border-base-300 ">
      <li class="mt-2"><a>升级</a></li>
      <li><a>签到</a></li>
    </div>
  </section>
  <!-- Open the modal using ID.showModal() method -->
  <dialog id="my_modal_5" class="modal modal-bottom sm:modal-middle" ref="modal">
    <div class="modal-box">
      <h3 class="text-lg font-bold">删除对话?</h3>
      <p class="py-4">确定删除
        <span class="font-bold">{{ DeleteRecordName }}</span>
      </p>
      <div class="modal-action">
        <form method="dialog">
          <!-- if there is a button in form, it will close the modal -->
          <button class="btn">取消</button>
        </form>
        <button class="btn" @click="deleteRecordHandler">确定</button>
      </div>
    </div>
  </dialog>
</template>

<script setup lang="ts">
// vue
import { reactive, watch, useTemplateRef, ref } from "vue";
// 组件
import SidebarMain from "./SidebarMain.vue";
// 图标
import EditIcon from "@/assets/svg/edit.svg?component";
import ExpandLeftIcon from "@/assets/svg/expand-left.svg?component";
// type
import type { IRequestData, IRecord } from '@/types'
// store
import { useRecordStore, useUserStore } from '@/store'
const recordStore = useRecordStore()
const userStore = useUserStore()

defineEmits(['closeSidebar'])
/** 创建新对话 */
const createNewChat = () => {
  console.log("createNewChat");
};


// 获取对话列表
let requestData = reactive<IRequestData>({
  page: 0,
  page_size: 10,
  user_id: userStore.userId,
  name: ''
})
async function getRecords() {
  await recordStore.getRecords(requestData)
}

// 切换对话记录
async function toggleRecord(record: IRecord) {
  if (record.id === recordStore.activeRecordId) return
  await recordStore.toggleRecord(record.id)
  await getRecords()
}

// 删除对话记录
const modal = useTemplateRef<HTMLDialogElement>('modal')
const DeleteRecordName = ref('')
const deleteRecordDetail = ref<IRecord>({} as IRecord)
async function deleteRecord(record: IRecord) {
  modal.value?.showModal()
  DeleteRecordName.value = record.name
  deleteRecordDetail.value = record
}
async function deleteRecordHandler() {
  await recordStore.deleteRecord(deleteRecordDetail.value.id)
  modal.value?.close()
  await getRecords()
}

// 编辑对话记录
async function editRecord(record: IRecord) {
  await recordStore.editRecord(record)
}

// 用户登录之后获取对话列表
watch(() => userStore.userId, async (newId) => {
  if (!newId) return
  requestData.user_id = newId
  await getRecords()
}, { immediate: true })


</script>
