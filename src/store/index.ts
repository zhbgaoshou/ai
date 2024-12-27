import { createPinia } from 'pinia'
export { useSettingsStore } from './modules/settings'
export { useUserStore } from './modules/user'
export { useRecordStore } from './modules/record'

export default createPinia()