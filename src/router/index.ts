import { createWebHistory, createRouter } from 'vue-router'

export const routes = [
    { path: '/', name: 'chat', component: () => import('@/views/Chat/index.vue') },
]

const router = createRouter({
    routes,
    history: createWebHistory(),
})

export default router