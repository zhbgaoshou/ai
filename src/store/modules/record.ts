import { defineStore } from "pinia";
import {
  getRecordsApi,
  toggleRecordApi,
  deleteRecordApi,
  editRecordApi,
  createRecordApi,
} from "@/api/chat";
import type { IRequestData, IRecord } from "@/types";
import dayjs from "dayjs";

export const useRecordStore = defineStore("record", {
  state: () => {
    return {
      records: [] as IRecord[], // 记录列表
      next: true, // 是否还有下一页
    };
  },
  actions: {
    // 创建记录
    async createRecord(data: IRecord) {
      await createRecordApi(data);
    },
    // 获取记录列表
    async getRecords(data: IRequestData) {
      const res = await getRecordsApi(data);
      this.records.push(...res.data); // 添加数据到 records
      this.next = res.next; // 更新是否有下一页
    },
    // 切换记录状态（如激活/关闭）
    async toggleRecord(id?: number | string) {
      await toggleRecordApi(id as string);
    },
    // 删除记录
    async deleteRecord(id: number | string) {
      await deleteRecordApi(id);
      this.records = this.records.filter((record) => record.id !== id); // 本地移除记录
    },
    // 编辑记录
    async editRecord(data: IRecord) {
      await editRecordApi(data);
    },
    clearActiveRecord() {
      if (this.records.length > 0) {
        // 先将所有记录的 is_active 设置为 false
        this.records.forEach((record) => {
          record.is_active = false;
        });
      }
    }
  },
  getters: {
    // 获取当前激活的记录 ID
    activeRecordId: (state) =>
      state.records.find((item) => item.is_active)?.id || "",

    // 获取当前激活的记录
    activeRecord: (state) =>
      state.records.find((item) => item.is_active) || ({} as IRecord),
    // 按日期分类记录，并仅对 today 排序
    categorized: (state) => {
      // 获取当前时间
      const now = dayjs();

      // 初始化分类对象
      const result = {
        today: [] as IRecord[],
        yesterday: [] as IRecord[],
        earlier: [] as IRecord[],
      };

      // 根据 created_at 对记录进行分类
      state.records.forEach((record) => {
        const recordDate = dayjs(record.created_at); // 使用 dayjs 解析记录时间

        if (recordDate.isSame(now, "day")) {
          result.today.push(record); // 今天
        } else if (recordDate.isSame(now.subtract(1, "day"), "day")) {
          result.yesterday.push(record); // 昨天
        } else {
          result.earlier.push(record); // 更久以前
        }
      });

      // 仅对 today 分类按创建时间降序排序（最新的排前面）
      result.today.sort((a, b) => dayjs(b.created_at).valueOf() - dayjs(a.created_at).valueOf());

      return result; // 返回分类结果
    },

  },
});
