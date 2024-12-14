<template>
  <div>
    <header class="bg-white shadow">
      <div class="mx-auto max-w-7xl px-4 py-6 sm:px-6 lg:px-8">
        <h1 class="text-3xl font-bold tracking-tight text-gray-900">Painel de Controle</h1>
      </div>
    </header>
    <main>
      <div class="mx-auto max-w-7xl px-4 py-6 sm:px-6 lg:px-8">
        <div class="flex justify-center space-x-4">
          <div>
            <label for="state">Estado:</label>
            <select id="state" v-model="selectedState" @change="updateCities">
              <option value="">Selecione um estado</option>
              <option v-for="state in states" :key="state.sigla" :value="state.sigla">{{ state.nome }}</option>
            </select>
          </div>

          <div>
            <label for="city">Cidade:</label>
            <select id="city" v-model="selectedCity" @change="updateUbs">
              <option value="">Selecione uma cidade</option>
              <option v-for="city in cities" :key="city.id" :value="city.nome">{{ city.nome }}</option>
            </select>
          </div>

          <div>
            <label for="ubs">UBS:</label>
            <select id="ubs" v-model="selectedUbs">
              <option value="">Selecione uma UBS</option>
              <option v-for="ubs in ubsList" :key="ubs.id" :value="ubs.id">{{ ubs.name }}</option>
            </select>
          </div>

          <div>
            <label for="year">Ano:</label>
            <input type="number" id="year" v-model.number="selectedYear" placeholder="Ano" />
          </div>

          <div>
            <label for="month">Mês:</label>
            <input type="number" id="month" v-model.number="selectedMonth" placeholder="Mês" />
          </div>

          <button @click="showUbsOnMap" class="ml-2 px-4 py-2 bg-blue-500 text-white rounded">Pesquisar</button>
        </div>

        <div id="map" class="h-96 mt-6"></div>

        <div class="mt-6 grid grid-cols-3 gap-4">
          <div class="bg-gray-100 p-4 rounded">
            <h2 class="font-bold text-lg">Total de Alunos</h2>
            <p>{{ totalStudents }}</p>
          </div>
          <div class="bg-gray-100 p-4 rounded">
            <h2 class="font-bold text-lg">UBS Selecionada</h2>
            <p>{{ selectedUbsData?.name || 'Nenhuma UBS Selecionada' }}</p>
          </div>
          <div class="bg-gray-100 p-4 rounded">
            <h2 class="font-bold text-lg">Tipo de UBS</h2>
            <p>{{ selectedUbsData?.ubs_type || 'N/D' }}</p>
          </div>
        </div>

        <div class="mt-6">
          <canvas id="teleconsultationsChart"></canvas>
        </div>

        <div class="mt-6">
          <h2 class="text-xl font-bold">Chamados</h2>
          <canvas id="callsChart"></canvas>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue';
import Chart from 'chart.js/auto';
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
const callsData = ref([]);
const totalStudents = ref(0);
const selectedUbsData = ref(null);

const loadGoogleMapsScript = (callback) => {
  if (window.google && window.google.maps) {
    callback(null); 
    return;
  }

  const script = document.createElement('script');
  script.src = `https://maps.googleapis.com/maps/api/js?key=${GOOGLE_MAPS_API_KEY}&libraries=places`;

  script.onload = () => callback(null);
  script.onerror = () => callback(new Error('Failed to load Google Maps script')); // Indica erro

  document.head.appendChild(script);
};


const loadStates = async () => {
  try {
    const response = await fetch('https://servicodados.ibge.gov.br/api/v1/localidades/estados');
    const data = await response.json();
    states.value = data;
  } catch (error) {
    console.error('Error fetching states:', error);
  }
};

const loadCities = async (stateCode) => {
  try {
    const response = await fetch(`https://servicodados.ibge.gov.br/api/v1/localidades/estados/${stateCode}/municipios`);
    const data = await response.json();
    cities.value = data;
  } catch (error) {
    console.error('Error fetching cities:', error);
  }
};

const loadUbs = async (cityName) => {
  try {
    const response = await fetch(`${API_BASE_URL}/ubs/city/${cityName}/`);
    const data = await response.json();
    ubsList.value = data.ubs_list;
  } catch (error) {
    console.error('Error fetching UBSs:', error);
  }
};

const initializeMap = () => {
  if (!window.google) return;

  const map = new google.maps.Map(document.getElementById('map'), {
    center: { lat: -23.550520, lng: -46.633308 },
    zoom: 12,
  });

  window.map = map;
};

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

          fetch(`${API_BASE_URL}/teleconsultations_by_month/${selectedUbs.value}/${selectedYear.value}/${selectedMonth.value}/`)
            .then((response) => response.json())
            .then((data) => {
              teleconsultationsData.value = data;
              renderTeleconsultationsChart(data);
            });

          fetch(`${API_BASE_URL}/calls/report/overall/${selectedYear.value}/${selectedMonth.value}/`)
            .then((response) => response.json())
            .then((data) => {
              callsData.value = data;
              renderCallsChart(data);
            });
        }
      });
  }
};


const renderTeleconsultationsChart = (data) => {
  const ctx = document.getElementById('teleconsultationsChart').getContext('2d');
  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: data.map(item => new Date(item.month).toLocaleString('default', { month: 'long', year: 'numeric' })), 
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

const renderCallsChart = (data) => {
  const ctx = document.getElementById('callsChart').getContext('2d');

  const statuses = Object.keys(data.report);
  const totals = statuses.map(status => data.report[status]);

  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: statuses, 
      datasets: [
        {
          label: 'Total de Chamados',
          data: totals, 
          backgroundColor: 'rgba(255, 99, 132, 0.2)',
          borderColor: 'rgba(255, 99, 132, 1)',
          borderWidth: 1,
        },
      ],
    },
    options: {
      responsive: true,
      scales: {
        x: {
          title: {
            display: true,
            text: 'Status do Chamado',
          },
        },
        y: {
          beginAtZero: true,
          title: {
            display: true,
            text: 'Número de Chamados',
          },
        },
      },
    },
  });
};


const updateCities = () => {
  if (selectedState.value) {
    loadCities(selectedState.value);
  }
};

const updateUbs = () => {
  if (selectedCity.value) {
    loadUbs(selectedCity.value);
  }
};

onMounted(async () => {
  await loadStates();
  await loadGoogleMapsScript();
  initializeMap();
});
</script>

<style scoped>
select, input {
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
  margin-bottom: 8px;
  width: 100%;
}

button {
  background-color: #007bff;
  color: white;
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}

#map {
  height: 400px;
}

header {
  background-color: #f8f9fa;
}

h1 {
  color: #333;
}
</style>
