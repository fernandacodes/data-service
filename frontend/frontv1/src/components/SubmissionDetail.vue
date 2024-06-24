<template>
  <div v-if="submission" class="flex min-h-full flex-1 flex-col justify-center px-6 py-12 lg:px-8">
    <div class="px-4 sm:px-0">
      <h3 class="text-base font-semibold leading-7 text-gray-900">Detalhes da Submissão</h3>
      <p class="mt-1 max-w-2xl text-sm leading-6 text-gray-500">Detalhes pessoais e da submissão.</p>
    </div>
    <div class="mt-6 border-t border-gray-100">
      <dl class="divide-y divide-gray-100">
        <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
          <dt class="text-sm font-medium leading-6 text-gray-900">Nome Completo</dt>
          <dd class="mt-1 text-sm leading-6 text-gray-700 sm:col-span-2 sm:mt-0">{{ submission.student.Name }}</dd>
        </div>
        <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
          <dt class="text-sm font-medium leading-6 text-gray-900">Email</dt>
          <dd class="mt-1 text-sm leading-6 text-gray-700 sm:col-span-2 sm:mt-0">{{ submission.student.Email }}</dd>
        </div>
        <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
          <dt class="text-sm font-medium leading-6 text-gray-900">Telefone</dt>
          <dd class="mt-1 text-sm leading-6 text-gray-700 sm:col-span-2 sm:mt-0">{{ submission.student.Phone }}</dd>
        </div>
        <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
          <dt class="text-sm font-medium leading-6 text-gray-900">Data de Nascimento</dt>
          <dd class="mt-1 text-sm leading-6 text-gray-700 sm:col-span-2 sm:mt-0">{{ submission.birth_date }}</dd>
        </div>
        <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
          <dt class="text-sm font-medium leading-6 text-gray-900">Cidade</dt>
          <dd class="mt-1 text-sm leading-6 text-gray-700 sm:col-span-2 sm:mt-0">{{ submission.city }}</dd>
        </div>
        <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
          <dt class="text-sm font-medium leading-6 text-gray-900">Estado</dt>
          <dd class="mt-1 text-sm leading-6 text-gray-700 sm:col-span-2 sm:mt-0">{{ submission.state }}</dd>
        </div>
        <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
          <dt class="text-sm font-medium leading-6 text-gray-900">Documento</dt>
          <dd class="mt-2 text-sm text-gray-900 sm:col-span-2 sm:mt-0">
            <ul role="list" class="divide-y divide-gray-100 rounded-md border border-gray-200">
              <li class="flex items-center justify-between py-4 pl-4 pr-5 text-sm leading-6">
                <div class="flex w-0 flex-1 items-center">
                  <PaperClipIcon class="h-5 w-5 flex-shrink-0 text-gray-400" aria-hidden="true" />
                  <div class="ml-4 flex min-w-0 flex-1 gap-2">
                    <a :href="submission.document" class="truncate font-medium text-indigo-600 hover:text-indigo-500">submission_document.pdf</a>
                  </div>
                </div>
              </li>
            </ul>
          </dd>
        </div>
      </dl>
    </div>
  </div>
  <div v-else-if="noSubmission" class="flex min-h-full flex-1 flex-col justify-center px-6 py-12 lg:px-8">
    <div class="bg-red-50 border-l-4 border-red-400 p-4">
      <div class="flex">
        <div class="flex-shrink-0">
          <svg class="h-5 w-5 text-red-400" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
            <path fill-rule="evenodd" d="M8.257 3.099c.366-.446.998-.446 1.364 0l5.51 6.684A1 1 0 0115.11 11H4.89a1 1 0 01-.82-1.217l5.51-6.684zM11 13a1 1 0 10-2 0v2a1 1 0 102 0v-2z" clip-rule="evenodd"/>
          </svg>
        </div>
        <div class="ml-3">
          <p class="text-sm text-red-700">
            Nenhuma submissão encontrada para este estudante.
          </p>
        </div>
      </div>
    </div>
  </div>
  <div v-else class="flex min-h-full flex-1 flex-col justify-center px-6 py-12 lg:px-8">
    <div class="text-center">
      <svg class="mx-auto h-12 w-12 text-gray-400" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 15a4 4 0 004 4h10a4 4 0 004-4M3 9a4 4 0 014-4h10a4 4 0 014 4M8 9v4m8-4v4m-4-4v4" />
      </svg>
      <h3 class="mt-2 text-sm font-medium text-gray-900">Carregando detalhes da submissão...</h3>
      <p class="mt-1 text-sm text-gray-500">Por favor, aguarde enquanto os detalhes da submissão estão sendo carregados.</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import axios from 'axios';
import { PaperClipIcon } from '@heroicons/vue/20/solid';
import { API_BASE_URL } from '../environment/environment';

const route = useRoute();
const cpf = route.params.cpf;
const submission = ref(null);
const noSubmission = ref(false);

const fetchSubmissionDetails = async () => {
  try {
    const response = await axios.get(`${API_BASE_URL}/submissions/cpf/${cpf}/`);
    submission.value = response.data.submission;
  } catch (error) {
    if (error.response && error.response.status === 404) {
      noSubmission.value = true;
    } else {
      console.error('Erro ao buscar detalhes da submissão:', error);
    }
  }
};

onMounted(fetchSubmissionDetails);
</script>

<style scoped>
</style>
