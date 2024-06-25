<template>
  <div>
    <div class="container mx-auto mt-8 px-4">
      <form @submit.prevent="handleSubmit()">
        <div class="space-y-12">
          <div class="border-b border-gray-900/10 pb-12">
            <h2 class="text-base font-semibold leading-7 text-gray-900">Submission Form</h2>
            <p class="mt-1 text-sm leading-6 text-gray-600">Please fill out the form below.</p>
            <div class="mt-10 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6">

              <!-- Full Name -->
              <div class="sm:col-span-3">
                <label for="full_name" class="block text-sm font-medium leading-6 text-gray-900">Full Name</label>
                <div class="mt-2">
                  <input type="text" name="full_name" id="full_name" maxlength="100" v-model="full_name"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <!-- Mother Name -->
              <div class="sm:col-span-3">
                <label for="mother_name" class="block text-sm font-medium leading-6 text-gray-900">Mother's Name</label>
                <div class="mt-2">
                  <input type="text" name="mother_name" id="mother_name" maxlength="100" v-model="mother_name"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <!-- Father Name -->
              <div class="sm:col-span-3">
                <label for="father_name" class="block text-sm font-medium leading-6 text-gray-900">Father's Name</label>
                <div class="mt-2">
                  <input type="text" name="father_name" id="father_name" maxlength="100" v-model="father_name"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <!-- Blood Type -->
              <div class="sm:col-span-3">
                <label for="blood_type" class="block text-sm font-medium leading-6 text-gray-900">Blood Type</label>
                <div class="mt-2">
                  <input type="text" name="blood_type" id="blood_type" maxlength="3" v-model="blood_type"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <!-- RH Factor -->
              <div class="sm:col-span-3">
                <label for="rh_factor" class="block text-sm font-medium leading-6 text-gray-900">RH Factor</label>
                <div class="mt-2">
                  <input type="text" name="rh_factor" id="rh_factor" maxlength="3" v-model="rh_factor"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <!-- Gender -->
              <div class="sm:col-span-3">
                <label for="gender" class="block text-sm font-medium leading-6 text-gray-900">Gender</label>
                <div class="mt-2">
                  <input type="text" name="gender" id="gender" maxlength="10" v-model="gender"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <!-- Race -->
              <div class="sm:col-span-3">
                <label for="race" class="block text-sm font-medium leading-6 text-gray-900">Race</label>
                <div class="mt-2">
                  <input type="text" name="race" id="race" maxlength="20" v-model="race"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <!-- Birth Date -->
              <div class="sm:col-span-3">
                <label for="birth_date" class="block text-sm font-medium leading-6 text-gray-900">Birth Date</label>
                <div class="mt-2">
                  <input type="date" name="birth_date" id="birth_date" v-model="birth_date"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <!-- Nationality -->
              <div class="sm:col-span-3">
                <label for="nationality" class="block text-sm font-medium leading-6 text-gray-900">Nationality</label>
                <div class="mt-2">
                  <input type="text" name="nationality" id="nationality" maxlength="50" v-model="nationality"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <!-- Birth City -->
              <div class="sm:col-span-3">
                <label for="birth_city" class="block text-sm font-medium leading-6 text-gray-900">Birth City</label>
                <div class="mt-2">
                  <input type="text" name="birth_city" id="birth_city" maxlength="50" v-model="birth_city"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <!-- Birth State -->
              <div class="sm:col-span-3">
                <label for="birth_state" class="block text-sm font-medium leading-6 text-gray-900">Birth State</label>
                <div class="mt-2">
                  <input type="text" name="birth_state" id="birth_state" maxlength="2" v-model="birth_state"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <!-- Birth Country -->
              <div class="sm:col-span-3">
                <label for="birth_country" class="block text-sm font-medium leading-6 text-gray-900">Birth
                  Country</label>
                <div class="mt-2">
                  <input type="text" name="birth_country" id="birth_country" maxlength="50" v-model="birth_country"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <!-- Phone -->
              <div class="sm:col-span-3">
                <label for="phone" class="block text-sm font-medium leading-6 text-gray-900">Phone</label>
                <div class="mt-2">
                  <input type="text" name="phone" id="phone" maxlength="15" v-model="phone"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <!-- Email -->
              <div class="sm:col-span-3">
                <label for="email" class="block text-sm font-medium leading-6 text-gray-900">Email</label>
                <div class="mt-2">
                  <input type="email" name="email" id="email" maxlength="100" v-model="email"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <!-- Address -->
              <div class="sm:col-span-6">
                <label for="address" class="block text-sm font-medium leading-6 text-gray-900">Address</label>
                <div class="mt-2">
                  <input type="text" name="address" id="address" maxlength="255" v-model="address"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <!-- Neighborhood -->
              <div class="sm:col-span-3">
                <label for="neighborhood" class="block text-sm font-medium leading-6 text-gray-900">Neighborhood</label>
                <div class="mt-2">
                  <input type="text" name="neighborhood" id="neighborhood" maxlength="100" v-model="neighborhood"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <!-- Address Complement -->
              <div class="sm:col-span-3">
                <label for="address_complement" class="block text-sm font-medium leading-6 text-gray-900">Address
                  Complement</label>
                <div class="mt-2">
                  <input type="text" name="address_complement" id="address_complement" maxlength="255"
                    v-model="address_complement"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <!-- Address City -->
              <div class="sm:col-span-3">
                <label for="address_city" class="block text-sm font-medium leading-6 text-gray-900">Address City</label>
                <div class="mt-2">
                  <input type="text" name="address_city" id="address_city" maxlength="50" v-model="address_city"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <div class="sm:col-span-3">
                <label for="marital_status" class="block text-sm font-medium leading-6 text-gray-900">Marital
                  Status</label>
                <div class="mt-2">
                  <input type="text" name="marital_status" id="marital_status" maxlength="20" v-model="marital_status"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <!-- CPF -->
              <div class="sm:col-span-3">
                <label for="cpf" class="block text-sm font-medium leading-6 text-gray-900">CPF</label>
                <div class="mt-2">
                  <input type="text" name="cpf" id="cpf" maxlength="11" v-model="cpf"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <!-- RG Number -->
              <div class="sm:col-span-3">
                <label for="rg_number" class="block text-sm font-medium leading-6 text-gray-900">RG Number</label>
                <div class="mt-2">
                  <input type="text" name="rg_number" id="rg_number" maxlength="20" v-model="rg_number"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <!-- RG Issuer -->
              <div class="sm:col-span-3">
                <label for="rg_issuer" class="block text-sm font-medium leading-6 text-gray-900">RG Issuer</label>
                <div class="mt-2">
                  <input type="text" name="rg_issuer" id="rg_issuer" maxlength="50" v-model="rg_issuer"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <!-- RG State -->
              <div class="sm:col-span-3">
                <label for="rg_state" class="block text-sm font-medium leading-6 text-gray-900">RG State</label>
                <div class="mt-2">
                  <input type="text" name="rg_state" id="rg_state" maxlength="2" v-model="rg_state"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <!-- High School Graduation Year -->
              <div class="sm:col-span-3">
                <label for="high_school_graduation_year" class="block text-sm font-medium leading-6 text-gray-900">High
                  School Graduation Year</label>
                <div class="mt-2">
                  <input type="text" name="high_school_graduation_year" id="high_school_graduation_year" maxlength="4"
                    v-model="high_school_graduation_year"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <!-- University Name -->
              <div class="sm:col-span-3">
                <label for="university_name" class="block text-sm font-medium leading-6 text-gray-900">University
                  Name</label>
                <div class="mt-2">
                  <input type="text" name="university_name" id="university_name" maxlength="100"
                    v-model="university_name"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <!-- Work City -->
              <div class="sm:col-span-3">
                <label for="work_city" class="block text-sm font-medium leading-6 text-gray-900">Work City</label>
                <div class="mt-2">
                  <input type="text" name="work_city" id="work_city" maxlength="50" v-model="work_city"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <!-- Work State -->
              <div class="sm:col-span-3">
                <label for="work_state" class="block text-sm font-medium leading-6 text-gray-900">Work State</label>
                <div class="mt-2">
                  <input type="text" name="work_state" id="work_state" maxlength="2" v-model="work_state"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <!-- Address State -->
              <div class="sm:col-span-3">
                <label for="address_state" class="block text-sm font-medium leading-6 text-gray-900">Address
                  State</label>
                <div class="mt-2">
                  <input type="text" name="address_state" id="address_state" maxlength="2" v-model="address_state"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <!-- Address Zip Code -->
              <div class="sm:col-span-3">
                <label for="address_zip_code" class="block text-sm font-medium leading-6 text-gray-900">Address Zip
                  Code</label>
                <div class="mt-2">
                  <input type="text" name="address_zip_code" id="address_zip_code" maxlength="10"
                    v-model="address_zip_code"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <!-- Indigenous Ethnicity -->
              <div class="sm:col-span-3">
                <label for="indigenous_ethnicity" class="block text-sm font-medium leading-6 text-gray-900">Indigenous
                  Ethnicity</label>
                <div class="mt-2">
                  <input type="text" name="indigenous_ethnicity" id="indigenous_ethnicity" maxlength="50"
                    v-model="indigenous_ethnicity"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <!-- Disability Degree -->
              <div>
                <div class="sm:col-span-3">
                  <label for="disability" class="block text-sm font-medium leading-6 text-gray-900">Do you have a
                    disability?</label>
                  <div class="mt-2">
                    <input type="checkbox" id="disability" v-model="disability" @change="toggleDisability">
                    <label for="disability" class="ml-2">Yes</label>
                  </div>
                </div>

                <div class="sm:col-span-3" v-if="disability">
                  <label for="disability_degree" class="block text-sm font-medium leading-6 text-gray-900">Disability
                    Degree</label>
                  <div class="mt-2">
                    <select name="disability_degree" id="disability_degree" v-model="disability_degree"
                      class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                      <option value="total">Total Disability</option>
                      <option value="partial">Partial Disability</option>
                    </select>
                  </div>
                </div>
              </div>

              <div class="sm:col-span-6">
                <label for="document" class="block text-sm font-medium leading-6 text-gray-900">Document</label>
                <div class="mt-2">
                  <input type="file" name="document" id="document" ref="document"
                    class="block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 focus:outline-none" />
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="sm:col-span-2">
          <label for="term_accepted" class="block text-sm font-medium leading-6 text-gray-900">Term Accepted</label>
          <div class="mt-2">
            <input type="checkbox" id="term_accepted" name="term_accepted"
              class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600" />
          </div>
        </div>
        <div class="mt-6 flex items-center justify-end gap-x-6">
          <button type="button" @click="handleCancel()"
            class="text-sm font-semibold leading-6 text-gray-900">Cancel</button>
          <button type="submit"
            class="rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Save</button>
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
          title: 'Success',
          text: 'Submission created successfully!',
        });

        // Clear form after successful submission
        this.clearForm();
      } catch (error) {
        if (error.response && error.response.data && error.response.data.error === "['Student has already submitted']") {
          notify({
            group: 'error',
            title: 'Error',
            text: 'You have already submitted the form.',
            type: 'error',
          });
        } else {
          notify({
            group: 'error',
            title: 'Error',
            text: 'Failed to create submission.',
            type: 'error',
          });
        }
      }
    },

    clearForm() {
      // Clear all form fields after successful submission
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

      // Remove form data from localStorage
      localStorage.removeItem('formData');
    },
  },
};
</script>
