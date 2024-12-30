<template>
  <div class="drawer min-h-0" :class="{ 'md:drawer-open': !isCollapse }">
    <input id="my-drawer" type="checkbox" class="drawer-toggle" />
    <div class="drawer-content flex flex-col min-h-0">
      <!-- 控制边栏 的按钮 -->
      <Header v-model="isCollapse" />
      <div class="overflow-auto flex-1 mx-1 pr-2">
        <Main :messages="messageStore.messages" :generate-text="generateText" />

      </div>
      <In @send="send" v-model:content="content" :models="userStore.models" />
    </div>
    <div class="drawer-side ">
      <label for="my-drawer" aria-label="close sidebar" class="drawer-overlay"></label>
      <Sidebar @close-sidebar="isCollapse = true" />
    </div>
  </div>
</template>

<script setup lang="ts">
import { fetchEventSource } from "@microsoft/fetch-event-source"

// vue
import { ref, reactive, watch } from "vue";
// 组件
import Sidebar from "./Sidebar.vue";
import Header from "@/components/Header/index.vue";
import Main from "./Main.vue";
import In from "./In.vue";
// store
import { useUserStore, useRecordStore, useMessageStore } from "@/store";
const userStore = useUserStore();
const recordStore = useRecordStore();
const messageStore = useMessageStore();

// 边栏折叠操作
const isCollapse = ref(false);

// 获取模型列表
function getModels() {
  userStore.getModels();
}
// 获取消息
interface IMessageParams {
  page: number;
  page_size: number;
  record_id: number | string;
}

const getMessageParams = reactive<IMessageParams>({
  page: 1,
  page_size: 10,
  record_id: recordStore.activeRecordId,
});
function getMessages(data: IMessageParams) {
  messageStore.getMessages(data)
}

getModels();
watch(() => recordStore.activeRecordId, record_id => {
  if (record_id) {
    getMessageParams.record_id = record_id
    getMessages(getMessageParams)
  }
}, {
  immediate: true
})

/** 发送流式请求 openai */
/**
 * 创建消息
 * @param record_id string
 * @param model string
 */
function createMessage(record_id: string | number, model: string, content: string, endpoint: string = 'openai', role: string = 'user') {
  const data = {
    content,
    user_id: userStore.userId,
    model: model,
    role: role,
    record_id: record_id as string,
    endpoint,
    unfinished: true,
  };

  return data;
}

// 数据
const content = ref("");
interface IStream {
  text: string;
  start: boolean;
  finish: boolean;
  data?: any;
}
let generateText = ref('')
function send() {
  const controller = new AbortController();
  const model = userStore.defaultModel.value;

  let record_id = recordStore.activeRecordId;

  const userMessage = createMessage(record_id, model, content.value);

  if (content.value) {
    content.value = "";
    messageStore.addMessage(userMessage);
  }

  fetchEventSource(`${import.meta.env.VITE_BASE_URL}/chat/message/stream`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${userStore.token}`,
    },
    signal: controller.signal,
    openWhenHidden: true,
    body: JSON.stringify(userMessage),
    onmessage(ev) {
      const streamData: IStream = JSON.parse(ev.data);
      if (streamData.text) {
        generateText.value += streamData.text
      }
    },
    async onclose() {
      if (!record_id) {
        await recordStore.getRecords({
          page: 1,
          page_size: 1,
          user_id: userStore.userId,
        })
        record_id = recordStore.activeRecordId
      }
      if (generateText.value) {
        const aiMessage = createMessage(record_id, model, generateText.value, 'openai', 'assistant');
        generateText.value = ''
        messageStore.addMessage(aiMessage);
      }
    },
    onerror(err) {
      throw err;
    },
  });
}
</script>

<style scoped></style>
