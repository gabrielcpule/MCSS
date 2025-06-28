// This file exports interfaces for the login form and response structure.

export interface LoginForm {
    username: string;
    password: string;
}

export interface LoginResponse {
    success: boolean;
    message: string;
    token?: string; // Optional token for authenticated users
}