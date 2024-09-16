let environment = "development";
const BASE_URL_DEV = 'http://localhost:8000';
const BASE_URL_PRD = 'http://15.228.45.143:8000';

const API_KEY = "AIzaSyDM40vfVqAgs1QUC08K8uCqtQ_r0mEdAyI";

export const API_BASE_URL = environment === "production" ? BASE_URL_PRD : BASE_URL_DEV;
export const GOOGLE_MAPS_API_KEY = API_KEY;
