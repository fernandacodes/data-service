// utils/auth.js

import axios from 'axios';
import { API_BASE_URL } from '../environment/environment';

export const isAuthenticated = async () => {
  const token = sessionStorage.getItem('token');
  return !!token;
};


export const isAdm = async () => {
  const userData = await getUserData();
  return userData.role === 'admin';
};

export const getUserData = async () => {
  const token = sessionStorage.getItem('token');
  if (!token) {
    throw new Error('Usuário não autenticado');
  }

  try {
    const response = await axios.get(`${API_BASE_URL}/user/`, {
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
  sessionStorage.removeItem('token');
};
