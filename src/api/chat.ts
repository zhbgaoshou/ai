import { $http } from '../utils/http2'
import type { IRequestData, IRecord } from '@/types'
// 获取记录列表
export const getRecordsApi = (data: IRequestData) =>
    $http<IRecord[]>({
        url: '/chat/record',
        method: 'get',
        params: data
    })

// 切换记录
export const toggleRecordApi = (id: number) =>
    $http({
        url: `/chat/record/toggle`,
        method: 'get',
        params: { record_id: id }
    })

// 删除记录
export const deleteRecordApi = (id: number) =>
    $http({
        url: `/chat/record/${id}`,
        method: 'delete',
    })

// 编辑记录
export const editRecordApi = (data: IRecord) =>
    $http({
        url: `/chat/record/${data.id}`,
        method: 'put',
        data
    })