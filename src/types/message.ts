export interface IMessage {
    "unfinished"?: boolean,
    "is_copy"?: boolean,
    "role": string,
    "user_message_id"?: string,
    "model": string,
    "content": string,
    "id"?: string,
    "updated_at"?: string | null,
    "created_at"?: string,
    "user_id": number | string,
    "is_edited"?: boolean,
    "ai_message_id"?: string | null,
    "record_id": string
}

export interface IMessageRequest {
    page: number;
    page_size: number;
    record_id: number | string;
}