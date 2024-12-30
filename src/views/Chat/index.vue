<template>
  <div class="drawer min-h-0" :class="{ 'md:drawer-open': !isCollapse }">
    <input id="my-drawer" type="checkbox" class="drawer-toggle" />
    <div class="drawer-content flex flex-col min-h-0">
      <!-- 控制边栏 的按钮 -->
      <Header v-model="isCollapse" />
      <div class="overflow-auto flex-1 mx-1">
        <Main />
      </div>
      <In @send="send" v-model:content="content" :models="userStore.models" />
    </div>
    <div class="drawer-side">
      <label
        for="my-drawer"
        aria-label="close sidebar"
        class="drawer-overlay"
      ></label>
      <Sidebar @close-sidebar="isCollapse = true" />
    </div>
  </div>
</template>

<script setup lang="ts">
import { fetchEventSource } from "@microsoft/fetch-event-source";
import { nanoid } from "nanoid";
import moment from "moment-timezone";

// vue
import { ref, onMounted } from "vue";
// 组件
import Sidebar from "./Sidebar.vue";
import Header from "@/components/Header/index.vue";
import Main from "./Main.vue";
import In from "./In.vue";
// store
import { useUserStore, useRecordStore } from "@/store";
const userStore = useUserStore();
const recordStore = useRecordStore();

// 边栏折叠操作
const isCollapse = ref(false);

// 获取模型列表
function getModels() {
  userStore.getModels();
}
onMounted(() => {
  getModels();
});

/** 发送流式请求 openai */
/**
 * 没有默认记录时创建
 * @param model 模型名称
 */
function createRecord(model: string, rid: string | number) {
  return {
    id: rid,
    name: "新会话",
    model: model,
    user_id: userStore.userId,
    endpoint: "openai",
    is_edited: false,
    is_active: true,
    created_at: formatByMomentTimezone(new Date().toISOString()),
  };
}
/**
 * 格式化到中国大陆时区的时间
 * @param time
 * @returns 格式化时区的时间
 */
const formatByMomentTimezone = (time: string) => {
  let timezoneName = moment.tz.guess(true);
  const resDate = moment.tz(time, timezoneName)?.format();
  return resDate || ""; //
};

/**
 * 创建消息
 * @param record_id string
 * @param model string
 */
function createMessage(record_id: string | number, model: string) {
  const data = {
    content: content.value,
    user_id: userStore.userId,
    model: model,
    role: "user",
    record_id: record_id,
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
function send() {
  const controller = new AbortController();
  const model = userStore.defaultModel.value;

  let record_id = recordStore.activeRecordId;
  let isCreate = false;

  /** 没有默认记录时创建 */
  if (!record_id) {
    record_id = nanoid();
    isCreate = true;
  }

  const userMessage = createMessage(record_id, model);

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
      if (content.value) {
        content.value = "";
      }
      if (streamData.start && isCreate) {
        const newRecord = createRecord(model, record_id);
        recordStore.records.unshift(newRecord);
        recordStore.createRecord(newRecord);
      }
      if (streamData.text) {
        console.log(streamData.text);
      }
    },
    onclose() {
      console.log("close");
    },
    onerror(err) {
      throw err;
    },
  });
}
</script>

<style scoped></style>
