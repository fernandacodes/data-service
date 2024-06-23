<template>
    <form>
      <div class="space-y-12">
        <div class="border-b border-gray-900/10 pb-12">
          <h2 class="text-base font-semibold leading-7 text-gray-900">Login</h2>
          <p class="mt-1 text-sm leading-6 text-gray-600">Insira seu CPF e senha para acessar sua conta.</p>
  
          <div class="mt-10 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6">
            <div class="sm:col-span-4">
              <label for="cpf" class="block text-sm font-medium leading-6 text-gray-900">CPF</label>
              <div class="mt-2">
                <div class="flex rounded-md shadow-sm ring-1 ring-inset ring-gray-300 focus-within:ring-2 focus-within:ring-inset focus-within:ring-indigo-600 sm:max-w-md">
                  <input type="text" name="cpf" id="cpf" autocomplete="cpf" class="block flex-1 border-0 bg-transparent py-1.5 pl-1 text-gray-900 placeholder:text-gray-400 focus:ring-0 sm:text-sm sm:leading-6" placeholder="000.000.000-00" />
                </div>
              </div>
            </div>
  
            <div class="sm:col-span-4">
              <label for="password" class="block text-sm font-medium leading-6 text-gray-900">Senha</label>
              <div class="mt-2">
                <input type="password" name="password" id="password" autocomplete="current-password" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" placeholder="••••••••" />
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
  import { ref } from 'vue'
  const cpf = ref('')
  const password = ref('')
  </script>
  