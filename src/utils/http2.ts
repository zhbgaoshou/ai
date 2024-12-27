import axios, { AxiosError, type AxiosRequestConfig } from "axios";
import { useUserStore } from '@/store'
import router from "@/router";


const http = axios.create({
    baseURL: import.meta.env.VITE_BASE_URL,
    timeout: 5000,
});

console.log(import.meta.env.VITE_BASE_AUTH_URL)

export const $http = async<T>(config: AxiosRequestConfig) => {
    const userStore = useUserStore()
    const token = userStore.token;
    try {
        if (token) {
            config.headers = { ...config.headers, Authorization: `Bearer ${token}` };
        }
        const res = await http(config);
        return res.data as T

    } catch (error) {
        if (error instanceof AxiosError) {
            const errorDetail = error.response?.data.detail;
            console.log(errorDetail);
            if (errorDetail instanceof Array) {
                alert(errorDetail[0].msg)
            } else {
                alert(error.response?.data.detail)

            }
            if (error.response?.status === 401) {
                userStore.logout()
                router.push('/')
            }
        }
        return Promise.reject(error);
    }
};