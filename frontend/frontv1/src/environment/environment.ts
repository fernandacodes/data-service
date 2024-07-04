let environment = "production";
const BASE_URL_DEV = 'http://localhost:8000';
const BASE_URL_PRD = 'https://web:8000';

// Exportando as constantes para uso em outras partes do seu aplicativo
export const API_BASE_URL = environment === "production"? BASE_URL_PRD : BASE_URL_DEV;
