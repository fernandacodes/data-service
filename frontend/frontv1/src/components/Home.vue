<template>
  <div>
    <header class="bg-white shadow">
      <div class="mx-auto max-w-7xl px-4 py-6 sm:px-6 lg:px-8">
        <h1 class="text-3xl font-bold tracking-tight text-gray-900">Painel de Controle</h1>
      </div>
    </header>
    <main>
      <div class="mx-auto max-w-7xl px-4 py-6 sm:px-6 lg:px-8">
        <!-- Exibe o mapa de calor diretamente como HTML -->
        <div v-html="mapHtml"></div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { API_BASE_URL } from '../environment/environment'

const mapHtml = ref('')

onMounted(async () => {
  try {
    const response = await fetch(`${API_BASE_URL}/generate_heatmap/`)
    const data = await response.text() // Obtém o HTML completo
    mapHtml.value = data // Define o HTML gerado diretamente no DOM
  } catch (error) {
    console.error('Error fetching the heatmap:', error)
  }
})
</script>
