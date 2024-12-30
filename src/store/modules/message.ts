import { defineStore } from "pinia";
import type { IMessage, IMessageRequest } from "@/types";
import { getMessagesApi } from "@/api/chat";

export const useMessageStore = defineStore("message", {
  state: () => ({
    messages: [] as IMessage[],
  }),
  actions: {
    async getMessages(data: IMessageRequest) {
      const res = await getMessagesApi(data);
      this.messages = res.data
    },
    addMessage(message: IMessage) {
      this.messages.push(message);
    },
  },
});
