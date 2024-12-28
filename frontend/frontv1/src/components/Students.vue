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
      <div class="mb-4 flex items-center space-x-2">
        <div>
          <label class="block text-sm font-medium text-gray-700">Filtrar por:</label>
          <div class="mt-1 flex space-x-2">
            <button @click="filterStudents('all')"
              :class="{ 'bg-indigo-500 text-white': filterType === 'all', 'bg-white text-indigo-500': filterType !== 'all' }"
              class="px-4 py-2 rounded-md border border-indigo-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
              Todos
            </button>
            <button @click="filterStudents('withSubmission')"
              :class="{ 'bg-indigo-500 text-white': filterType === 'withSubmission', 'bg-white text-indigo-500': filterType !== 'withSubmission' }"
              class="px-4 py-2 rounded-md border border-indigo-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
              Com Submissão
            </button>
            <button @click="filterStudents('withoutSubmission')"
              :class="{ 'bg-indigo-500 text-white': filterType === 'withoutSubmission', 'bg-white text-indigo-500': filterType !== 'withoutSubmission' }"
              class="px-4 py-2 rounded-md border border-indigo-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
              Sem Submissão
            </button>
            <button @click="downloadSubmitted"
              class="bg-green-500 text-white px-4 py-2 rounded-md hover:bg-green-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500">
              Download Submetidos
            </button>
            <button @click="downloadNotSubmitted"
              class="bg-green-500 text-white px-4 py-2 rounded-md hover:bg-green-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500">
              Download Não Submetidos
            </button>
          </div>
        </div>

      </div>
      <ul role="list" class="divide-y divide-gray-200">
        <li v-for="student in paginatedStudents" :key="student.CPF" class="py-4">
          <router-link :to="{ name: 'StudentDetails', params: { cpf: student.CPF } }" class="flex items-center">
            <div class="ml-3">
              <p class="text-sm font-medium text-gray-900">{{ student.Name }}</p>
              <p class="text-sm text-gray-500">{{ student.Email }}</p>
            </div>
          </router-link>
        </li>
      </ul>
      <div class="flex justify-center mt-4">
        <button :disabled="currentPage === 1" @click="changePage(currentPage - 1)"
          class="px-4 py-2 mx-1 rounded-md bg-gray-200 hover:bg-gray-300 disabled:opacity-50">
          Anterior
        </button>
        <button v-for="page in visiblePages" :key="page" @click="changePage(page)"
          :class="{ 'bg-indigo-500 text-white': page === currentPage, 'bg-gray-200': page !== currentPage }"
          class="px-4 py-2 mx-1 rounded-md">
          {{ page }}
        </button>
        <button :disabled="currentPage === totalPages" @click="changePage(currentPage + 1)"
          class="px-4 py-2 mx-1 rounded-md bg-gray-200 hover:bg-gray-300 disabled:opacity-50">
          Próximo
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import axios from 'axios';
import { API_BASE_URL } from '../environment/environment';
import Loader from './Loader.vue';

const students = ref([]);
const searchTerm = ref('');
const filterType = ref('all');
const isLoading = ref(true);
const currentPage = ref(1);
const itemsPerPage = ref(10);

const totalPages = computed(() => Math.ceil(students.value.length / itemsPerPage.value));

const visiblePages = computed(() => {
  const maxVisible = 5;
  let pages = [];
  if (totalPages.value <= maxVisible) {
    for (let i = 1; i <= totalPages.value; i++) {
      pages.push(i);
    }
  } else if (currentPage.value <= 3) {
    pages = [1, 2, 3, 4, 5];
  } else if (currentPage.value > totalPages.value - 3) {
    pages = [totalPages.value - 4, totalPages.value - 3, totalPages.value - 2, totalPages.value - 1, totalPages.value];
  } else {
    pages = [currentPage.value - 2, currentPage.value - 1, currentPage.value, currentPage.value + 1, currentPage.value + 2];
  }
  return pages;
});

const paginatedStudents = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage.value;
  const end = start + itemsPerPage.value;
  return students.value.slice(start, end);
});

const changePage = (page) => {
  if (page >= 1 && page <= totalPages.value) {
    currentPage.value = page;
  }
};

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
    currentPage.value = 1;
  } catch {
    students.value = [];
  }
  isLoading.value = false;
};

const filterStudents = (filter) => {
  filterType.value = filter;
  searchStudents();
};

const downloadSubmitted = async () => {
  try {
    const response = await axios.get(`${API_BASE_URL}/students/with-submissions/export/`, {
      responseType: 'blob',
    });
    const url = window.URL.createObjectURL(new Blob([response.data]));
    const link = document.createElement('a');
    link.href = url;
    link.setAttribute('download', 'alunos-submetidos.csv');
    document.body.appendChild(link);
    link.click();
  } catch (error) {
    console.error('Erro ao baixar os alunos submetidos:', error);
  }
};

const downloadNotSubmitted = async () => {
  try {
    const response = await axios.get(`${API_BASE_URL}/students/without-submissions/export/`, {
      responseType: 'blob',
    });
    const url = window.URL.createObjectURL(new Blob([response.data]));
    const link = document.createElement('a');
    link.href = url;
    link.setAttribute('download', 'alunos-nao-submetidos.csv');
    document.body.appendChild(link);
    link.click();
  } catch (error) {
    console.error('Erro ao baixar os alunos não submetidos:', error);
  }
};

const loadStudents = async () => {
  try {
    const response = await axios.get(`${API_BASE_URL}/students/all/`);
    students.value = response.data.students;
  } catch {
    students.value = [];
  }
  isLoading.value = false;
};

onMounted(loadStudents);
</script>
