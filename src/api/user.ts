import { $http } from '@/utils/http'
import type { IAuthData, ILoginResData, IInfo } from '@/types'


export const loginApi = (authData: IAuthData) => {
    return $http<ILoginResData>({
        url: '/login',
        method: 'post',
        headers: { 'Content-Type': 'multipart/form-data' },
        data: authData
    })
}

export const infoApi = () => {
    return $http<IInfo>({
        url: '/me',
        method: 'get'
    })
}