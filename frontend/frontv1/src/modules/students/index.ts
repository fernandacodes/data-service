import axios from 'axios';
import { API_BASE_URL } from '../../environment/environment';

/**
 * Verifica se um aluno já realizou uma submissão.
 * @param studentCpf - O CPF do aluno a ser verificado.
 * @returns Uma Promise que resolve para um booleano indicando se o aluno fez a submissão.
 */
export const hasStudentSubmitted = async (studentCpf: string): Promise<boolean> => {
  try {
    const response = await axios.get(`${API_BASE_URL}/submissions/has_submission/${studentCpf}/`);
    return response.data.has_submission;
  } catch (error: any) {
    if (error.response && error.response.status === 404) {
      return false; 
    }
    throw new Error('Erro ao verificar o status de submissão do aluno.');
  }
};
