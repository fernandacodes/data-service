// utils/auth.js

import axios from 'axios';
import { API_BASE_URL } from '../environment/environment';

export const isAuthenticated = async () => {
  const token = localStorage.getItem('token');
  if (!token) {
    return false;
  }
  try {
    const response = await axios.post(`${API_BASE_URL}/api/token/verify/`, { token });
    return response.status === 200;
  } catch (error) {
    return false;
  }
};

export const isAdm = async () => {
  const userData = await getUserData();
  return userData.role === 'admin';
};

export const getUserData = async () => {
  const token = localStorage.getItem('token');
  if (!token) {
    throw new Error('Usuário não autenticado');
  }

  try {
    const response = await axios.get(`${API_BASE_URL}/api/user/`, {
      headers: {
        Authorization: `Bearer ${token}`
      }
    });

    return response.data;
  } catch (error) {
    throw error;
  }
};

export const logout = () => {
  localStorage.removeItem('token');
};
