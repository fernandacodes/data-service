<template>
  <div>
    <header class="bg-white shadow">
      <div class="mx-auto max-w-7xl px-4 py-6 sm:px-6 lg:px-8">
        <h1 class="text-3xl font-bold tracking-tight text-gray-900">Painel de Controle</h1>
      </div>
    </header>
    <main>
      <div class="mx-auto max-w-7xl px-4 py-6 sm:px-6 lg:px-8">
        <div>
          <label for="state">Estado:</label>
          <select id="state" v-model="selectedState" @change="updateCities">
            <option value="">Selecione um estado</option>
            <option v-for="state in states" :key="state.sigla" :value="state.sigla">{{ state.nome }}</option>
          </select>

          <label for="city">Cidade:</label>
          <select id="city" v-model="selectedCity" @change="updateUbs">
            <option value="">Selecione uma cidade</option>
            <option v-for="city in cities" :key="city.id" :value="city.nome">{{ city.nome }}</option>
          </select>

          <label for="ubs">UBS:</label>
          <select id="ubs" v-model="selectedUbs">
            <option value="">Selecione uma UBS</option>
            <option v-for="ubs in ubsList" :key="ubs.id" :value="ubs.id">{{ ubs.name }}</option>
          </select>

          <label for="year">Ano:</label>
          <input type="number" id="year" v-model.number="selectedYear" placeholder="Ano" />

          <label for="month">Mês:</label>
          <input type="number" id="month" v-model.number="selectedMonth" placeholder="Mês" />

          <!-- Botão de pesquisar ao lado do select -->
          <button @click="showUbsOnMap" class="ml-2 px-4 py-2 bg-blue-500 text-white rounded">Pesquisar</button>
        </div>

        <div id="map" class="h-96 mt-6"></div>

        <!-- Gráfico de teleconsultas -->
        <div class="mt-6">
          <canvas id="teleconsultationsChart"></canvas>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue';
import { API_BASE_URL, GOOGLE_MAPS_API_KEY } from '../environment/environment';
const selectedState = ref('');
const selectedCity = ref('');
const selectedUbs = ref('');
const selectedYear = ref(null);
const selectedMonth = ref(null);
const states = ref([]);
const cities = ref([]);
const ubsList = ref([]);
const teleconsultationsData = ref([]);
import Chart from 'chart.js/auto'; // Importando Chart.js

// Função para carregar o script do Google Maps
const loadGoogleMapsScript = () => {
  return new Promise((resolve, reject) => {
    if (window.google && window.google.maps) {
      resolve();
      return;
    }
    const script = document.createElement('script');
    script.src = `https://maps.googleapis.com/maps/api/js?key=${GOOGLE_MAPS_API_KEY}&libraries=places`;
    script.onload = () => resolve();
    script.onerror = () => reject(new Error('Failed to load Google Maps script'));
    document.head.appendChild(script);
  });
};

// Função para carregar os estados
const loadStates = async () => {
  try {
    const response = await fetch('https://servicodados.ibge.gov.br/api/v1/localidades/estados');
    const data = await response.json();
    states.value = data;
  } catch (error) {
    console.error('Error fetching states:', error);
  }
};

// Função para carregar as cidades de um estado
const loadCities = async (stateCode) => {
  try {
    const response = await fetch(`https://servicodados.ibge.gov.br/api/v1/localidades/estados/${stateCode}/municipios`);
    const data = await response.json();
    cities.value = data;
  } catch (error) {
    console.error('Error fetching cities:', error);
  }
};

// Função para carregar UBSs de uma cidade
const loadUbs = async (cityName) => {
  try {
    const response = await fetch(`${API_BASE_URL}/ubs/city/${cityName}/`);
    const data = await response.json();
    ubsList.value = data.ubs_list;
  } catch (error) {
    console.error('Error fetching UBSs:', error);
  }
};

// Função para inicializar o mapa do Google Maps
const initializeMap = () => {
  if (!window.google) return;

  const map = new google.maps.Map(document.getElementById('map'), {
    center: { lat: -23.550520, lng: -46.633308 },
    zoom: 12,
  });

  window.map = map;
};

// Função para exibir a UBS no mapa ao clicar no botão de pesquisar
const showUbsOnMap = () => {
  if (!window.google) return;

  const ubs = ubsList.value.find((ubs) => ubs.id === selectedUbs.value);
  if (ubs) {
    fetch(`https://maps.googleapis.com/maps/api/geocode/json?address=${ubs.city},${ubs.state}&key=${GOOGLE_MAPS_API_KEY}`)
      .then((response) => response.json())
      .then((data) => {
        if (data.results.length > 0) {
          const location = data.results[0].geometry.location;
          window.map.setCenter(location);

          new google.maps.Marker({
            position: location,
            map: window.map,
            title: ubs.name,
          });

          // Buscar dados de teleconsultas para o gráfico
          fetch(`${API_BASE_URL}/teleconsultations_by_month/${selectedUbs.value}/${selectedYear.value}/${selectedMonth.value}/`)
            .then((response) => response.json())
            .then((data) => {
              teleconsultationsData.value = data;
              renderTeleconsultationsChart(data);
            });
        }
      });
  }
};

// Função para renderizar o gráfico de teleconsultas
const renderTeleconsultationsChart = (data) => {
  const ctx = document.getElementById('teleconsultationsChart').getContext('2d');
  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: data.map(item => new Date(item.month).toLocaleString('default', { month: 'long', year: 'numeric' })), // Formatando a data
      datasets: [
        {
          label: 'Teleconsultas por Mês',
          data: data.map(item => item.total),
          backgroundColor: 'rgba(75, 192, 192, 0.2)',
          borderColor: 'rgba(75, 192, 192, 1)',
          borderWidth: 1,
        },
      ],
    },
    options: {
      scales: {
        x: {
          beginAtZero: true,
        },
      },
    },
  });
};

onMounted(async () => {
  try {
    await loadGoogleMapsScript();
    loadStates();
    initializeMap();
  } catch (error) {
    console.error('Error loading Google Maps:', error);
  }
});

watch(selectedState, (newState) => {
  if (newState) {
    loadCities(newState);
  }
});

watch(selectedCity, (newCity) => {
  if (newCity) {
    loadUbs(newCity);
  }
});
</script>

<style scoped>
.modal-content {
  width: 100%;
  height: 60%;
  max-width: 1000px;
}
</style>
