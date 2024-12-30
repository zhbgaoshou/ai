import { $http } from "../utils/http2";
import type { IRequestData, IRecord, IModel } from "@/types";
// 获取记录列表
export const getRecordsApi = (data: IRequestData) =>
  $http<{ data: IRecord[]; next: boolean }>({
    url: "/chat/record",
    method: "get",
    params: data,
  });

// 切换记录
export const toggleRecordApi = (id: number | string) =>
  $http({
    url: `/chat/record/toggle`,
    method: "get",
    params: { record_id: id },
  });

// 删除记录
export const deleteRecordApi = (id: number | string) =>
  $http({
    url: `/chat/record/${id}`,
    method: "delete",
  });

// 编辑记录
export const editRecordApi = (data: IRecord) =>
  $http({
    url: `/chat/record/${data.id}`,
    method: "put",
    data,
  });
// 创建记录
export const createRecordApi = (data: IRecord) =>
  $http({
    url: "/chat/record",
    method: "post",
    data,
  });

// 获取模型列表
export const getModelsApi = () =>
  $http<IModel[]>({
    url: "/chat/model",
    method: "get",
  });
