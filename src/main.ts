import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import store, { useSettingsStore } from './store'
import router from './router'

const app = createApp(App)

app.use(store)
app.use(router)

// 初始化设置
useSettingsStore().initSettings()

app.mount('#app')
