// src/config.js
const isProd = process.env.NODE_ENV === 'production';
export const API_BASE = isProd ? "/api" : "http://localhost:5000/api";
export const FILE_BASE = isProd ? "" : "http://localhost:5000";
