<template>
  <div>
    <div class="container mx-auto mt-8 px-4">
      <form @submit.prevent="handleSubmit()">
        <div class="space-y-12">
          <div class="border-b border-gray-900/10 pb-12">
            <h2 class="text-base font-semibold leading-7 text-gray-900">Formulário de Envio</h2>
            <p class="mt-1 text-sm leading-6 text-gray-600">Por favor, preencha o formulário abaixo.</p>
            <div class="mt-10 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6">

              <!-- Nome Completo -->
              <div class="sm:col-span-3">
                <label for="full_name" class="block text-sm font-medium leading-6 text-gray-900">Nome Completo</label>
                <div class="mt-2">
                  <input type="text" name="full_name" id="full_name" maxlength="100" v-model="full_name"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <!-- Nome da Mãe -->
              <div class="sm:col-span-3">
                <label for="mother_name" class="block text-sm font-medium leading-6 text-gray-900">Nome da Mãe</label>
                <div class="mt-2">
                  <input type="text" name="mother_name" id="mother_name" maxlength="100" v-model="mother_name"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <!-- Nome do Pai -->
              <div class="sm:col-span-3">
                <label for="father_name" class="block text-sm font-medium leading-6 text-gray-900">Nome do Pai</label>
                <div class="mt-2">
                  <input type="text" name="father_name" id="father_name" maxlength="100" v-model="father_name"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <!-- Tipo Sanguíneo -->
              <div class="sm:col-span-3">
                <label for="blood_type" class="block text-sm font-medium leading-6 text-gray-900">Tipo Sanguíneo</label>
                <div class="mt-2">
                  <input type="text" name="blood_type" id="blood_type" maxlength="3" v-model="blood_type"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <!-- Fator RH -->
              <div class="sm:col-span-3">
                <label for="rh_factor" class="block text-sm font-medium leading-6 text-gray-900">Fator RH</label>
                <div class="mt-2">
                  <input type="text" name="rh_factor" id="rh_factor" maxlength="3" v-model="rh_factor"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <!-- Gênero -->
              <div class="sm:col-span-3">
                <label for="gender" class="block text-sm font-medium leading-6 text-gray-900">Gênero</label>
                <div class="mt-2">
                  <input type="text" name="gender" id="gender" maxlength="10" v-model="gender"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <!-- Raça -->
              <div class="sm:col-span-3">
                <label for="race" class="block text-sm font-medium leading-6 text-gray-900">Raça</label>
                <div class="mt-2">
                  <input type="text" name="race" id="race" maxlength="20" v-model="race"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <!-- Data de Nascimento -->
              <div class="sm:col-span-3">
                <label for="birth_date" class="block text-sm font-medium leading-6 text-gray-900">Data de
                  Nascimento</label>
                <div class="mt-2">
                  <input type="date" name="birth_date" id="birth_date" v-model="birth_date"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <!-- Nacionalidade -->
              <div class="sm:col-span-3">
                <label for="nationality" class="block text-sm font-medium leading-6 text-gray-900">Nacionalidade</label>
                <div class="mt-2">
                  <input type="text" name="nationality" id="nationality" maxlength="50" v-model="nationality"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <!-- Cidade de Nascimento -->
              <div class="sm:col-span-3">
                <label for="birth_city" class="block text-sm font-medium leading-6 text-gray-900">Cidade de
                  Nascimento</label>
                <div class="mt-2">
                  <input type="text" name="birth_city" id="birth_city" maxlength="50" v-model="birth_city"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <!-- Estado de Nascimento -->
              <div class="sm:col-span-3">
                <label for="birth_state" class="block text-sm font-medium leading-6 text-gray-900">Estado de
                  Nascimento</label>
                <div class="mt-2">
                  <input type="text" name="birth_state" id="birth_state" maxlength="2" v-model="birth_state"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <!-- País de Nascimento -->
              <div class="sm:col-span-3">
                <label for="birth_country" class="block text-sm font-medium leading-6 text-gray-900">País de
                  Nascimento</label>
                <div class="mt-2">
                  <input type="text" name="birth_country" id="birth_country" maxlength="50" v-model="birth_country"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <!-- Telefone -->
              <div class="sm:col-span-3">
                <label for="phone" class="block text-sm font-medium leading-6 text-gray-900">Telefone</label>
                <div class="mt-2">
                  <input type="text" name="phone" id="phone" maxlength="15" v-model="phone"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <!-- Email -->
              <div class="sm:col-span-3">
                <label for="email" class="block text-sm font-medium leading-6 text-gray-900">Email</label>
                <div class="mt-2">
                  <input type="email" name="email" id="email" v-model="email"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

            </div>
          </div>

          <!-- Botão de envio -->
          <div class="mt-6 flex items-center justify-end gap-x-6">
            <button type="button" class="text-sm font-semibold leading-6 text-gray-900">Cancelar</button>
            <button type="submit"
              class="rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Salvar</button>
          </div>
        </div>
      </form>

    </div>
  </div>
</template>

<script>
import { getUserData } from '../utils/auth';
import axios from 'axios';
import { notify } from 'notiwind';
import { API_BASE_URL } from '../environment/environment';

export default {
  name: 'Submission',
  data() {
    return {
      term_accepted: false,
      full_name: '',
      mother_name: '',
      father_name: '',
      blood_type: '',
      rh_factor: '',
      gender: '',
      race: '',
      birth_date: '',
      nationality: '',
      birth_city: '',
      birth_state: '',
      birth_country: '',
      phone: '',
      email: '',
      marital_status: '',
      cpf: '',
      rg_number: '',
      rg_issuer: '',
      rg_state: '',
      document: null,
      high_school_graduation_year: '',
      university_name: '',
      work_city: '',
      work_state: '',
      address: '',
      neighborhood: '',
      address_complement: '',
      address_city: '',
      address_state: '',
      address_zip_code: '',
      indigenous_ethnicity: '',
      disability: false,
      disability_degree: '',
      created_at: '',
    };
  },
  created() {
    this.loadFormData();
  },
  watch: {
    // Watch each form data property to save it in localStorage when it changes
    term_accepted(val) { this.saveFormData(); },
    full_name(val) { this.saveFormData(); },
    mother_name(val) { this.saveFormData(); },
    father_name(val) { this.saveFormData(); },
    blood_type(val) { this.saveFormData(); },
    rh_factor(val) { this.saveFormData(); },
    gender(val) { this.saveFormData(); },
    race(val) { this.saveFormData(); },
    birth_date(val) { this.saveFormData(); },
    nationality(val) { this.saveFormData(); },
    birth_city(val) { this.saveFormData(); },
    birth_state(val) { this.saveFormData(); },
    birth_country(val) { this.saveFormData(); },
    phone(val) { this.saveFormData(); },
    email(val) { this.saveFormData(); },
    marital_status(val) { this.saveFormData(); },
    cpf(val) { this.saveFormData(); },
    rg_number(val) { this.saveFormData(); },
    rg_issuer(val) { this.saveFormData(); },
    rg_state(val) { this.saveFormData(); },
    document(val) { this.saveFormData(); },
    high_school_graduation_year(val) { this.saveFormData(); },
    university_name(val) { this.saveFormData(); },
    work_city(val) { this.saveFormData(); },
    work_state(val) { this.saveFormData(); },
    address(val) { this.saveFormData(); },
    neighborhood(val) { this.saveFormData(); },
    address_complement(val) { this.saveFormData(); },
    address_city(val) { this.saveFormData(); },
    address_state(val) { this.saveFormData(); },
    address_zip_code(val) { this.saveFormData(); },
    indigenous_ethnicity(val) { this.saveFormData(); },
    disability(val) { this.saveFormData(); },
    disability_degree(val) { this.saveFormData(); },
    created_at(val) { this.saveFormData(); },
  },
  methods: {
    saveFormData() {
      // Save form data to localStorage
      const formData = {
        term_accepted: this.term_accepted,
        full_name: this.full_name,
        mother_name: this.mother_name,
        father_name: this.father_name,
        blood_type: this.blood_type,
        rh_factor: this.rh_factor,
        gender: this.gender,
        race: this.race,
        birth_date: this.birth_date,
        nationality: this.nationality,
        birth_city: this.birth_city,
        birth_state: this.birth_state,
        birth_country: this.birth_country,
        phone: this.phone,
        email: this.email,
        marital_status: this.marital_status,
        cpf: this.cpf,
        rg_number: this.rg_number,
        rg_issuer: this.rg_issuer,
        rg_state: this.rg_state,
        high_school_graduation_year: this.high_school_graduation_year,
        university_name: this.university_name,
        work_city: this.work_city,
        work_state: this.work_state,
        address: this.address,
        neighborhood: this.neighborhood,
        address_complement: this.address_complement,
        address_city: this.address_city,
        address_state: this.address_state,
        address_zip_code: this.address_zip_code,
        indigenous_ethnicity: this.indigenous_ethnicity,
        disability: this.disability,
        disability_degree: this.disability_degree,
        created_at: this.created_at,
      };
      localStorage.setItem('formData', JSON.stringify(formData));
    },
    loadFormData() {
      // Load form data from localStorage
      const formData = JSON.parse(localStorage.getItem('formData'));
      if (formData) {
        this.term_accepted = formData.term_accepted;
        this.full_name = formData.full_name;
        this.mother_name = formData.mother_name;
        this.father_name = formData.father_name;
        this.blood_type = formData.blood_type;
        this.rh_factor = formData.rh_factor;
        this.gender = formData.gender;
        this.race = formData.race;
        this.birth_date = formData.birth_date;
        this.nationality = formData.nationality;
        this.birth_city = formData.birth_city;
        this.birth_state = formData.birth_state;
        this.birth_country = formData.birth_country;
        this.phone = formData.phone;
        this.email = formData.email;
        this.marital_status = formData.marital_status;
        this.cpf = formData.cpf;
        this.rg_number = formData.rg_number;
        this.rg_issuer = formData.rg_issuer;
        this.rg_state = formData.rg_state;
        this.document = formData.document;
        this.high_school_graduation_year = formData.high_school_graduation_year;
        this.university_name = formData.university_name;
        this.work_city = formData.work_city;
        this.work_state = formData.work_state;
        this.address = formData.address;
        this.neighborhood = formData.neighborhood;
        this.address_complement = formData.address_complement;
        this.address_city = formData.address_city;
        this.address_state = formData.address_state;
        this.address_zip_code = formData.address_zip_code;
        this.indigenous_ethnicity = formData.indigenous_ethnicity;
        this.disability = formData.disability;
        this.disability_degree = formData.disability_degree;
        this.created_at = formData.created_at;
      }
    },
    async handleSubmit() {
      // Validate fields and prepare formData
      let user = await getUserData();
      const formData = new FormData();
      formData.append('student', user.id);
      formData.append('term_accepted', this.term_accepted ? 'True' : 'False');
      formData.append('full_name', this.full_name);
      formData.append('mother_name', this.mother_name);
      formData.append('father_name', this.father_name);
      formData.append('blood_type', this.blood_type);
      formData.append('rh_factor', this.rh_factor);
      formData.append('gender', this.gender);
      formData.append('race', this.race);
      formData.append('birth_date', this.birth_date);
      formData.append('nationality', this.nationality);
      formData.append('birth_city', this.birth_city);
      formData.append('birth_state', this.birth_state);
      formData.append('birth_country', this.birth_country);
      formData.append('phone', this.phone);
      formData.append('email', this.email);
      formData.append('marital_status', this.marital_status);
      formData.append('cpf', this.cpf);
      formData.append('rg_number', this.rg_number);
      formData.append('rg_issuer', this.rg_issuer);
      formData.append('rg_state', this.rg_state);
      formData.append('high_school_graduation_year', this.high_school_graduation_year);
      formData.append('university_name', this.university_name);
      formData.append('work_city', this.work_city);
      formData.append('work_state', this.work_state);
      formData.append('address', this.address);
      formData.append('neighborhood', this.neighborhood);
      formData.append('address_complement', this.address_complement);
      formData.append('address_city', this.address_city);
      formData.append('address_state', this.address_state);
      formData.append('address_zip_code', this.address_zip_code);
      formData.append('indigenous_ethnicity', this.indigenous_ethnicity);
      formData.append('disability', this.disability);
      formData.append('disability_degree', this.disability_degree);

      if (this.$refs.document && this.$refs.document.files.length > 0) {
        formData.append('document', this.$refs.document.files[0]);
      }

      try {
        const response = await axios.post(`${API_BASE_URL}/submissions/`, formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        });

        notify({
          group: 'foo',
          title: 'Sucesso',
          text: 'Inscrição criada com sucesso!',
        });

        // Clear form after successful submission
        this.clearForm();
      } catch (error) {
        notify({
          group: 'foo',
          title: 'Erro',
          text: 'Erro ao enviar a inscrição. Por favor, tente novamente.',
        });
      }
    },
    clearForm() {
      this.term_accepted = false;
      this.full_name = '';
      this.mother_name = '';
      this.father_name = '';
      this.blood_type = '';
      this.rh_factor = '';
      this.gender = '';
      this.race = '';
      this.birth_date = '';
      this.nationality = '';
      this.birth_city = '';
      this.birth_state = '';
      this.birth_country = '';
      this.phone = '';
      this.email = '';
      this.marital_status = '';
      this.cpf = '';
      this.rg_number = '';
      this.rg_issuer = '';
      this.rg_state = '';
      this.document = null;
      this.high_school_graduation_year = '';
      this.university_name = '';
      this.work_city = '';
      this.work_state = '';
      this.address = '';
      this.neighborhood = '';
      this.address_complement = '';
      this.address_city = '';
      this.address_state = '';
      this.address_zip_code = '';
      this.indigenous_ethnicity = '';
      this.disability = false;
      this.disability_degree = '';
      this.created_at = '';
      localStorage.removeItem('formData');
    },
  },
};

</script>
