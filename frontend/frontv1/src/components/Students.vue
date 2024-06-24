<template>
  <div class="div">
    <Header></Header>
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

      <!-- Lista de estudantes filtrada por pesquisa -->
      <ul role="list" class="divide-y divide-gray-200">
        <li v-for="student in students" :key="student.id" class="py-4">
          <div class="flex items-center">
            <img :src="student.imageUrl" alt="" class="h-10 w-10 rounded-full bg-gray-100 flex-shrink-0" />
            <div class="ml-3">
              <p class="text-sm font-medium text-gray-900">{{ student.Name }}</p>
              <p class="text-sm text-gray-500">{{ student.Email }}</p>
            </div>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import Header from './Header.vue';

const students = ref([]);
const searchTerm = ref('');

const searchStudents = async () => {
  try {
    let response;
    if (searchTerm.value.trim() === '') {
      response = await axios.get('http://localhost:8000/students/all/');
    } else {
      response = await axios.get(`http://localhost:8000/students/search/?name=${searchTerm.value}`);
    }
    students.value = response.data.students;
  } catch (error) {
    console.error('Erro ao buscar estudantes:', error);
    students.value = [];
  }
};

// Função inicial para carregar todos os estudantes
const loadStudents = async () => {
  try {
    const response = await axios.get('http://localhost:8000/students/all/');
    students.value = response.data.students;
  } catch (error) {
    console.error('Erro ao carregar todos os estudantes:', error);
    students.value = [];
  }
};

onMounted(loadStudents);
</script>

<style scoped>
</style>
