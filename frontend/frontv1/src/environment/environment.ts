let environment = "production";
const BASE_URL_DEV = 'http://localhost:8000/api';
const BASE_URL_PRD = 'https://sistemaunasus.ufam.edu.br:8000/api';

const API_KEY = "AIzaSyDM40vfVqAgs1QUC08K8uCqtQ_r0mEdAyI";

export const API_BASE_URL = environment === "production" ? BASE_URL_PRD : BASE_URL_DEV;
export const GOOGLE_MAPS_API_KEY = API_KEY;
