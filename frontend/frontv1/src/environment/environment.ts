let environment = "production";
const BASE_URL_DEV = 'http://localhost:8000';
const BASE_URL_PRD = 'http://15.228.45.143:8000';

export const API_BASE_URL = environment === "production"? BASE_URL_PRD : BASE_URL_DEV;
