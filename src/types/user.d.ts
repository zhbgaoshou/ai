// 注册登录
export interface IAuthData {
    username: string
    password: string,
    email?: null
}
// 登录返回数据
export interface ILoginResData {
    access_token: string
    expire_in: number
    refresh_token: string
    token_type: string
}

// 用户信息
export interface IInfo {
    "username": string,
    "email": string,
    "avatar": string,
    "id": number,
    "is_active": boolean,
    "is_superuser": boolean,
    "created_at": string,
    "last_login": string
}


