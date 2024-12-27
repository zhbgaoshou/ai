import { defineStore } from 'pinia'
import { getRecordsApi, toggleRecordApi, deleteRecordApi, editRecordApi } from '@/api/chat'
import type { IRequestData, IRecord } from '@/types'


export const useRecordStore = defineStore('record', {
    state: () => {
        return {
            records: [] as IRecord[],
        }
    },
    actions: {
        async getRecords(data: IRequestData) {
            const res = await getRecordsApi(data)
            this.records = res
        },
        async toggleRecord(id: number) {
            await toggleRecordApi(id)
        },
        async deleteRecord(id: number) {
            await deleteRecordApi(id)
        },
        async editRecord(data: IRecord) {
            await editRecordApi(data)
        }
    },
    getters: {
        activeRecordId: state => state.records.find(item => item.is_active)?.id || 0
    }
})