// utils/auth.js

import axios from 'axios';

export const isAuthenticated = async () => {
  const token = localStorage.getItem('token');
  if (!token) {
    return false;
  }

  try {
    // Verificar se o token é válido
    const response = await axios.post('http://localhost:8000/api/token/verify/', { token });
    return response.status === 200;
  } catch (error) {
    console.error('Erro ao verificar token:', error);
    return false;
  }
};
