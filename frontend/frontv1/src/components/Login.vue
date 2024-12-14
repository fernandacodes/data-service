<template>
  <div class="flex min-h-full flex-1 flex-col justify-center px-6 py-12 lg:px-8">
    <div class="sm:mx-auto sm:w-full sm:max-w-sm">
      <img class="mx-auto h-10 w-auto" src="https://unasus.ufam.edu.br/images/headers/banner01.png" alt="UNASUS-UFAM" />
      <h2 class="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">Entrar na sua conta</h2>
    </div>

    <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
      <form class="space-y-6" @submit.prevent="login()">
        <div>
          <label for="cpf" class="block text-sm font-medium leading-6 text-gray-900">CPF</label>
          <div class="mt-2">
            <input type="text" v-model="cpf" name="cpf" id="cpf" autocomplete="cpf" class="block flex-1 border-0 bg-transparent py-1.5 pl-1 text-gray-900 placeholder:text-gray-400 focus:ring-0 sm:text-sm sm:leading-6" placeholder="000.000.000-00" />
          </div>
        </div>

        <div>
          <div class="flex items-center justify-between">
            <label for="password" class="block text-sm font-medium leading-6 text-gray-900">Senha</label>
            <div class="text-sm">
              <!-- Comentado a parte de "Esqueceu sua senha?" -->
              <!-- <a href="#" class="font-semibold text-indigo-600 hover:text-indigo-500">Esqueceu sua senha?</a> -->
            </div>
          </div>
          <div class="mt-2">
            <input type="password" v-model="password" name="password" id="password" autocomplete="current-password" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" placeholder="••••••••" />
          </div>
        </div>

        <div>
          <button type="submit" class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Entrar</button>
        </div>
      </form>

      <p class="mt-10 text-center text-sm text-gray-500">
                <!-- Não tem uma conta? -->
        
        <!-- <a href="#" class="font-semibold leading-6 text-indigo-600 hover:text-indigo-500">Crie uma</a> -->
      </p>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref } from 'vue';
import router from '../router';
import { notify } from 'notiwind';
import { API_BASE_URL } from '../environment/environment';

const cpf = ref('');
const password = ref('');

const removeCpfFormatting = (cpf) => {
  return cpf.replace(/[.-]/g, '');
};

const login = async () => {
  var cpfFormatted = removeCpfFormatting(cpf.value);
  try {
    const response = await axios.post(`${API_BASE_URL}/api/token/`, {
      username: cpfFormatted,
      password: password.value
    });
    localStorage.setItem('token', response.data.token);
    router.push('/'); 

    notify({
      group: 'foo',
      title: 'Sucesso',
      text: 'Logado com sucesso!'
    });
  } catch (error) {
    notify({
      group: 'error',
      title: 'Erro',
      text: 'Falha ao fazer login. Verifique suas credenciais.'
    });
  }
};

axios.interceptors.request.use(config => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
})
</script>

<style>
</style>
