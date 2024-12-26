export const setToken = (token: string) => {
    localStorage.setItem('token', token)
}

export const setRefreshToken = (token: string) => {
    localStorage.setItem('refresh_token', token)
}

export const getToken = () => {
    return localStorage.getItem('token') || ''
}
export const getRefreshToken = () => {
    return localStorage.getItem('refresh_token')
}

export const removeToken = () => {
    localStorage.removeItem('token')
}

