import { createWebHistory, createRouter } from 'vue-router'
import { useUserStore } from '@/store'


export const routes = [
    { path: '/', name: 'chat', component: () => import('@/views/Chat/index.vue') },
]

const router = createRouter({
    routes,
    history: createWebHistory(),
})


router.beforeEach(async (to, from, next) => {
    from
    const userStore = useUserStore()
    const token = userStore.token
    const username = userStore.info.username

    if (token) {
        if (username) {
            next()
        } else {
            await userStore.getInfo()
            next({ ...to, replace: true })
        }
    } else {
        next()
    }

})

export default router