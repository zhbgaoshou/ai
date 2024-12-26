import { defineStore } from 'pinia'
import { loginApi, infoApi } from '@/api/user'
import type { IAuthData, IInfo } from '@/types'
import { setRefreshToken, setToken, getToken, removeToken } from '@/utils/auth'


export const useUserStore = defineStore('user', {

    state: () => {
        return {
            token: getToken(),
            authData: {} as IAuthData,
            info: {} as IInfo
        }
    },
    getters: {
        isLogin: state => state.token !== '',
        firstName: state => state.info.username?.split('')[0].toUpperCase()

    },
    actions: {
        logout() {
            this.token = ''
            removeToken()
        },
        async login() {
            const res = await loginApi(this.authData)
            this.token = res.access_token
            setToken(res.access_token)
            setRefreshToken(res.refresh_token)
            await this.getInfo()
        },
        async getInfo() {
            const res = await infoApi()
            this.info = res
            return res
        },
        resetAuthData() {
            this.authData = {} as IAuthData
        }
    }
})