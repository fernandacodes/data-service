<template>
  <form @submit.prevent="login">
    <div class="space-y-12">
      <div class="border-b border-gray-900/10 pb-12">
        <h2 class="text-base font-semibold leading-7 text-gray-900">Login</h2>
        <p class="mt-1 text-sm leading-6 text-gray-600">Insira seu CPF e senha para acessar sua conta.</p>

        <div class="mt-10 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6">
          <div class="sm:col-span-4">
            <label for="cpf" class="block text-sm font-medium leading-6 text-gray-900">CPF</label>
            <div class="mt-2">
              <div class="flex rounded-md shadow-sm ring-1 ring-inset ring-gray-300 focus-within:ring-2 focus-within:ring-inset focus-within:ring-indigo-600 sm:max-w-md">
                <input type="text" v-model="cpf" name="cpf" id="cpf" autocomplete="cpf" class="block flex-1 border-0 bg-transparent py-1.5 pl-1 text-gray-900 placeholder:text-gray-400 focus:ring-0 sm:text-sm sm:leading-6" placeholder="000.000.000-00" />
              </div>
            </div>
          </div>

          <div class="sm:col-span-4">
            <label for="password" class="block text-sm font-medium leading-6 text-gray-900">Senha</label>
            <div class="mt-2">
              <input type="password" v-model="password" name="password" id="password" autocomplete="current-password" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" placeholder="••••••••" />
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="mt-6 flex items-center justify-end gap-x-6">
      <button type="button" class="text-sm font-semibold leading-6 text-gray-900">Cancelar</button>
      <button type="submit" class="rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Entrar</button>
    </div>
  </form>
</template>

<script setup>
import axios from 'axios';
import { ref } from 'vue';
import router from '../router';

const cpf = ref('');
const password = ref('');

const removeCpfFormatting = (cpf) => {
  // Remove pontos e traços usando expressões regulares
  return cpf.replace(/[.-]/g, '');
};

const login = async () => {
  var cpfFormatted = removeCpfFormatting(cpf.value)
  try {
    const response = await axios.post('http://localhost:8000/api/token/', {
      username:  cpfFormatted,
      password: password.value
    });
    localStorage.setItem('token', token);
    router.push('/');
  } catch (error) {
    console.error('Erro ao fazer login:', error);
  }
};

axios.interceptors.request.use(config => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
}, error => {
  return Promise.reject(error);
});
</script>


  