<template>
  <div class="min-h-full">
    <Disclosure as="nav" class="bg-gray-800" v-slot="{ open }">
      <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <div class="flex h-16 items-center justify-between">
          <div class="flex items-center">
            <div class="hidden md:block">
              <div class="ml-10 flex items-baseline space-x-4">
                <router-link to="/" :class="isActive('/')">Painel</router-link>
                <router-link to="/submission" :class="isActive('/submission')">Submissão</router-link>
                <router-link to="/profile" :class="isActive('/profile')">Perfil</router-link>
                <router-link v-if="showStudentsLink" to="/students"
                  :class="isActive('/students')">Estudantes</router-link>
              </div>
            </div>
          </div>
          <div class="hidden md:block">
            <div class="ml-4 flex items-center md:ml-6">
              <button type="button"
                class="relative rounded-full bg-gray-800 p-1 text-gray-400 hover:text-white focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-gray-800">
                <span class="absolute -inset-1.5"></span>
                <span class="sr-only">Ver notificações</span>
                <BellIcon class="h-6 w-6" aria-hidden="true" />
              </button>

              <Menu as="div" class="relative ml-3">
                <div>
                  <MenuButton
                    class="relative flex rounded-full bg-gray-800 text-sm focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-gray-800">
                    <span class="absolute -inset-1.5" />
                    <span class="sr-only">Abrir menu de usuário</span>
                    <span class="ml-2 text-sm font-medium text-gray-300 truncate"> {{ user.first_name }} {{
                      user.last_name }}</span>
                  </MenuButton>
                </div>
                <transition enter-active-class="transition ease-out duration-100"
                  enter-from-class="transform opacity-0 scale-95" enter-to-class="transform opacity-100 scale-100"
                  leave-active-class="transition ease-in duration-75" leave-from-class="transform opacity-100 scale-100"
                  leave-to-class="transform opacity-0 scale-95">
                  <MenuItems
                    class="absolute right-0 z-10 mt-2 w-48 origin-top-right rounded-md bg-white py-1 shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none">
                   
                    <MenuItem v-slot="{ active }">
                    <a  :class="[active ? 'bg-gray-100' : '', 'block px-4 py-2 text-sm text-gray-700']"
                      @click.prevent="handleLogout()">Sair</a>
                    </MenuItem>
                  </MenuItems>
                </transition>
              </Menu>
            </div>
          </div>
          <div class="-mr-2 flex md:hidden">
            <!-- Botão de menu mobile -->
            <DisclosureButton
              class="relative inline-flex items-center justify-center rounded-md bg-gray-800 p-2 text-gray-400 hover:bg-gray-700 hover:text-white focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-gray-800">
              <span class="absolute -inset-0.5"></span>
              <span class="sr-only">Abrir menu principal</span>
              <Bars3Icon v-if="!open" class="block h-6 w-6" aria-hidden="true" />
              <XMarkIcon v-else class="block h-6 w-6" aria-hidden="true" />
            </DisclosureButton>
          </div>
        </div>
      </div>

      <DisclosurePanel class="md:hidden">
        <div class="space-y-1 px-2 pb-3 pt-2 sm:px-3">
          <router-link to="/" :class="isActive('/')">Painel</router-link>
          <router-link to="/submission" :class="isActive('/submission')">Submissão</router-link>
          <router-link v-if="showStudentsLink" to="/students" :class="isActive('/students')">Estudantes</router-link>
        </div>
        <div class="border-t border-gray-700 pb-3 pt-4">
          <div class="flex items-center px-5">
            <div class="ml-3">
              <div class="text-base font-medium leading-none text-white">{{ user.name }}</div>
              <div class="text-sm font-medium leading-none text-gray-400">{{ user.email }}</div>
            </div>
            <button type="button"
              class="relative ml-auto flex-shrink-0 rounded-full bg-gray-800 p-1 text-gray-400 hover:text-white focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-gray-800">
              <span class="absolute -inset-1.5"></span>
              <span class="sr-only">Ver notificações</span>
              <BellIcon class="h-6 w-6" aria-hidden="true" />
            </button>
          </div>
          <div class="mt-3 space-y-1 px-2">
            <router-link to="/logout" :class="isActive('/logout')" @click.prevent="handleLogout">Sair</router-link>
          </div>
        </div>
      </DisclosurePanel>
    </Disclosure>
  </div>
</template>

<script setup>
import { Disclosure, DisclosureButton, DisclosurePanel, Menu, MenuButton, MenuItem, MenuItems } from '@headlessui/vue';
import { Bars3Icon, BellIcon, XMarkIcon } from '@heroicons/vue/24/outline';
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import router from '../router';
import { isAuthenticated, getUserData, logout } from '../utils/auth';

// Variável reativa para controlar a exibição do link de Estudantes
const showStudentsLink = ref(false);

let user = {
  name: '',
  email: '',
  first_name: '',
  last_name: ''
};

// Função para carregar dados do usuário ao montar o componente
onMounted(async () => {
  const auth = await isAuthenticated();
  if (auth) {
    try {
      const userData = await getUserData();
      user.name = userData.name;
      user.email = userData.email;
      user.first_name = userData.first_name;
      user.last_name = userData.last_name;

      // Verificar se o usuário tem permissão de admin (role === 'admin')
      if (userData.role === 'admin') {
        showStudentsLink.value = true; // Mostrar o link de Estudantes apenas para administradores
      }
    } catch (error) {
    }
  }
});

function isActive(path) {
  return {
    'bg-gray-900 text-white': router.currentRoute.value.path === path,
    'text-gray-300 hover:bg-gray-700 hover:text-white': router.currentRoute.value.path !== path,
    'rounded-md px-3 py-2 text-sm font-medium': true,
  };
}

function handleLogout() {
  logout();
  router.push('/login');
}
</script>

<style>
/* Estilos opcionais */
</style>
