<template>
  <div v-if="isLoading">
    <Loader></Loader>
  </div>
  <div class="div">
    <div class="container mx-auto px-4 py-8">
      <h1 class="text-2xl font-semibold mb-4">Lista de Estudantes</h1>
      <div class="mb-4">
        <label for="searchInput" class="block text-sm font-medium text-gray-700">Pesquisar por nome:</label>
        <div class="mt-1 relative rounded-md shadow-sm flex">
          <input v-model="searchTerm" type="text" id="searchInput"
            class="focus:ring-indigo-500 focus:border-indigo-500 block w-full pr-10 sm:text-sm border-gray-300 rounded-md"
            placeholder="Digite o nome do estudante" />
          <button @click="searchStudents"
            class="ml-2 bg-indigo-500 text-white px-4 py-2 rounded-md hover:bg-indigo-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
            Pesquisar
          </button>
        </div>
      </div>
      <div class="mb-4">
        <label class="block text-sm font-medium text-gray-700">Filtrar por:</label>
        <div class="mt-1 flex space-x-2">
          <button @click="filterStudents('all')"
            :class="{'bg-indigo-500 text-white': filterType === 'all', 'bg-white text-indigo-500': filterType !== 'all'}"
            class="px-4 py-2 rounded-md border border-indigo-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
            Todos
          </button>
          <button @click="filterStudents('withSubmission')"
            :class="{'bg-indigo-500 text-white': filterType === 'withSubmission', 'bg-white text-indigo-500': filterType !== 'withSubmission'}"
            class="px-4 py-2 rounded-md border border-indigo-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
            Com Submissão
          </button>
          <button @click="filterStudents('withoutSubmission')"
            :class="{'bg-indigo-500 text-white': filterType === 'withoutSubmission', 'bg-white text-indigo-500': filterType !== 'withoutSubmission'}"
            class="px-4 py-2 rounded-md border border-indigo-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
            Sem Submissão
          </button>
        </div>
      </div>
      <ul role="list" class="divide-y divide-gray-200">
        <li v-for="student in students" :key="student.CPF" class="py-4">
          <router-link :to="{ name: 'StudentDetails', params: { cpf: student.CPF } }" class="flex items-center">
            <img :src="student.imageUrl" alt="" class="h-10 w-10 rounded-full bg-gray-100 flex-shrink-0" />
            <div class="ml-3">
              <p class="text-sm font-medium text-gray-900">{{ student.Name }}</p>
              <p class="text-sm text-gray-500">{{ student.Email }}</p>
            </div>
          </router-link>
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { API_BASE_URL } from '../environment/environment';
const students = ref([]);
const searchTerm = ref('');
const filterType = ref('all');
import Loader from './Loader.vue';
const isLoading = ref(true); // Estado de carregamento

const searchStudents = async () => {
  isLoading.value = true;
  try {
    let response;
    if (searchTerm.value.trim() === '') {
      if (filterType.value === 'withSubmission') {
        response = await axios.get(`${API_BASE_URL}/students/with-submissions/`);
      } else if (filterType.value === 'withoutSubmission') {
        response = await axios.get(`${API_BASE_URL}/students/all/`);
        response.data.students = response.data.students.filter(student => !student.hasSubmission);
      } else {
        response = await axios.get(`${API_BASE_URL}/students/all/`);
      }
    } else {
      response = await axios.get(`${API_BASE_URL}/students/search/?name=${searchTerm.value}`);
      if (filterType.value === 'withSubmission') {
        response.data.students = response.data.students.filter(student => student.hasSubmission);
      } else if (filterType.value === 'withoutSubmission') {
        response.data.students = response.data.students.filter(student => !student.hasSubmission);
      }
    }
    students.value = response.data.students;
  } catch (error) {
    console.error('Erro ao buscar estudantes:', error);
    students.value = [];
  }
  isLoading.value = false;
};

const loadStudents = async () => {
  try {
    const response = await axios.get(`${API_BASE_URL}/students/all/`);
    students.value = response.data.students;
  } catch (error) {
    console.error('Erro ao carregar todos os estudantes:', error);
    students.value = [];
  }
  isLoading.value = false;
};

const filterStudents = (filter) => {
  filterType.value = filter;
  searchStudents();
};

onMounted(loadStudents);
</script>

<style scoped>
</style>
