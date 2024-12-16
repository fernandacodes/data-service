<template>
  <div class="flex min-h-full flex-1 flex-col justify-center px-6 py-12 lg:px-8">
    <div class="sm:mx-auto sm:w-full sm:max-w-sm bg-[#1b2131] p-8 rounded-lg shadow-lg">
      <img class="mx-auto h-30 w-auto" src="../assets/unasus-ufam-logo.jpg" alt="UNASUS-UFAM" />
      <h2 class="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-white">Entrar na sua conta</h2>
      <form class="space-y-6 mt-6" @submit.prevent="login()">
        <div>
          <label for="cpf" class="block text-sm font-medium leading-6 text-white">CPF</label>
          <div class="mt-2">
            <input type="text" v-model="cpf" name="cpf" id="cpf" autocomplete="cpf"
              class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
              placeholder="000.000.000-00" />
          </div>
        </div>
        <div>
          <div class="flex items-center justify-between">
            <label for="password" class="block text-sm font-medium leading-6 text-white">Senha</label>
          </div>
          <div class="mt-2">
            <input type="password" v-model="password" name="password" id="password" autocomplete="current-password"
              class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
              placeholder="••••••••" />
          </div>
        </div>
        <div>
          <button 
            type="submit" 
            :disabled="isLoading"
            :class="{
              'bg-gray-400 cursor-not-allowed': isLoading,
              'bg-indigo-600 hover:bg-indigo-500': !isLoading
            }"
            class="flex w-full justify-center rounded-md px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">
            <span v-if="isLoading">Entrando...</span>
            <span v-else>Entrar</span>
          </button>
        </div>
      </form>
      <p class="mt-10 text-center text-sm text-gray-500">
      </p>
    </div>
  </div>
  <footer></footer>
</template>

<script setup>
import axios from 'axios';
import { ref } from 'vue';
import router from '../router';
import { notify } from 'notiwind';
import { API_BASE_URL } from '../environment/environment';
import Footer from './Footer.vue';
import { getUserData } from '../utils/auth';

const cpf = ref('');
const password = ref('');
const isLoading = ref(false);

const removeCpfFormatting = (cpf) => {
  return cpf.replace(/[.-]/g, '');
};

const login = async () => {
  if (isLoading.value) return;
  isLoading.value = true;

  const cpfFormatted = removeCpfFormatting(cpf.value);
  try {
    const response = await axios.post(`${API_BASE_URL}/token/`, {
      username: cpfFormatted,
      password: password.value,
    });

    sessionStorage.setItem('token', response.data.token);

    const user = await getUserData();
    sessionStorage.setItem("role", user.role);

    router.push('/');
    notify({
      group: 'foo',
      title: 'Sucesso',
      text: 'Logado com sucesso!',
    });
  } catch (error) {
    notify({
      group: 'error',
      title: 'Erro',
      text: 'Falha ao fazer login. Verifique suas credenciais.',
    });
  } finally {
    isLoading.value = false;
  }
};
</script>

<style>
img {
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
  /* Sombras suaves */
}

.bg-[#1b2131] {
  background-color: #1b2131;
}
</style>
