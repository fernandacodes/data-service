<template>
    <div class="container mx-auto px-4 py-8">
      <h1 class="text-2xl font-semibold mb-4">Lista de Estudantes</h1>
  
      <!-- Campo de pesquisa por nome -->
      <div class="mb-4">
        <label for="searchInput" class="block text-sm font-medium text-gray-700">Pesquisar por nome:</label>
        <div class="mt-1 relative rounded-md shadow-sm">
          <input
            v-model="searchTerm"
            @input="searchStudents"
            type="text"
            id="searchInput"
            class="focus:ring-indigo-500 focus:border-indigo-500 block w-full pr-10 sm:text-sm border-gray-300 rounded-md"
            placeholder="Digite o nome do estudante"
          />
        </div>
      </div>
  
      <!-- Lista de estudantes filtrada por pesquisa -->
      <ul role="list" class="divide-y divide-gray-200">
        <li v-for="student in filteredStudents" :key="student.id" class="py-4">
          <div class="flex items-center">
            <img
              :src="student.imageUrl"
              alt=""
              class="h-10 w-10 rounded-full bg-gray-100 flex-shrink-0"
            />
            <div class="ml-3">
              <p class="text-sm font-medium text-gray-900">{{ student.Name }}</p>
              <p class="text-sm text-gray-500">{{ student.Email }}</p>
            </div>
          </div>
        </li>
      </ul>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import axios from 'axios';
  
  // Dados de estudantes (inicialmente vazio)
  const students = ref([]);
  
  // Termo de pesquisa
  const searchTerm = ref('');
  
  // Função para buscar estudantes por nome
  const searchStudents = async () => {
    try {
      const response = await axios.get(`/students/search/?name=${searchTerm.value}`);
      students.value = response.data.students;
    } catch (error) {
      console.error('Erro ao buscar estudantes:', error);
      students.value = []; // Limpa a lista de estudantes em caso de erro
    }
  };
  
  // Função inicial para carregar todos os estudantes (opcional)
  const loadStudents = async () => {
    try {
      const response = await axios.get('/students/all/');
      students.value = response.data.students;
    } catch (error) {
      console.error('Erro ao carregar todos os estudantes:', error);
      students.value = []; // Limpa a lista de estudantes em caso de erro
    }
  };
  
  // Chama a função inicial para carregar todos os estudantes
  loadStudents();
  </script>
  
  <style scoped>
  /* Estilos opcionais */
  </style>
  