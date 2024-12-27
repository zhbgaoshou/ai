export interface IRequestData {
    page: number
    page_size: number
    user_id: number
    name?: string
}

export interface IRecord {
    "name": string,
    "model": string,
    "user_id": number,
    "endpoint": string,
    "is_edited": boolean,
    "is_active": boolean,
    "id": number,
    "created_at": string,
    "updated_at": string | null
}