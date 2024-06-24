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

export const getUserData = async () => {
  const token = localStorage.getItem('token');
  if (!token) {
    throw new Error('Usuário não autenticado');
  }

  try {
    // Fazer a requisição para obter os dados do usuário
    const response = await axios.get('http://localhost:8000/api/user/', {
      headers: {
        Authorization: `Bearer ${token}`
      }
    });

    return response.data;
  } catch (error) {
    console.error('Erro ao obter dados do usuário:', error);
    throw error;
  }
};
export const logout = () => {
  localStorage.removeItem('token');  
};