<template>
  <div>
    <div class="container mx-auto mt-8 px-4">
      <form @submit.prevent="handleSubmit()">
        <div class="space-y-12">
          <div class="border-b border-gray-900/10 pb-12">
            <h2 class="text-base font-semibold leading-7 text-gray-900">Submission Form</h2>
            <p class="mt-1 text-sm leading-6 text-gray-600">Please fill out the form below.</p>
            <div class="mt-10 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6">
              
              <div class="sm:col-span-3">
                <label for="guardian_name" class="block text-sm font-medium leading-6 text-gray-900">Guardian Name</label>
                <div class="mt-2">
                  <input type="text" name="guardian_name" id="guardian_name" maxlength="100"
                    v-model="guardian_name"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <div class="sm:col-span-3">
                <label for="mother_name" class="block text-sm font-medium leading-6 text-gray-900">Mother's Name</label>
                <div class="mt-2">
                  <input type="text" name="mother_name" id="mother_name" maxlength="100"
                    v-model="mother_name"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <div class="sm:col-span-3">
                <label for="father_name" class="block text-sm font-medium leading-6 text-gray-900">Father's Name</label>
                <div class="mt-2">
                  <input type="text" name="father_name" id="father_name" maxlength="100"
                    v-model="father_name"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <div class="sm:col-span-3">
                <label for="birth_date" class="block text-sm font-medium leading-6 text-gray-900">Birth Date</label>
                <div class="mt-2">
                  <input type="date" name="birth_date" id="birth_date"
                    v-model="birth_date"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <div class="sm:col-span-3">
                <label for="phone" class="block text-sm font-medium leading-6 text-gray-900">Phone</label>
                <div class="mt-2">
                  <input type="text" name="phone" id="phone" maxlength="15"
                    v-model="phone"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <div class="sm:col-span-3">
                <label for="email" class="block text-sm font-medium leading-6 text-gray-900">Email</label>
                <div class="mt-2">
                  <input type="email" name="email" id="email"
                    v-model="email"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <div class="sm:col-span-3">
                <label for="cpf" class="block text-sm font-medium leading-6 text-gray-900">CPF</label>
                <div class="mt-2">
                  <input type="text" name="cpf" id="cpf" maxlength="11"
                    v-model="cpf"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <div class="sm:col-span-3">
                <label for="rg_number" class="block text-sm font-medium leading-6 text-gray-900">RG Number</label>
                <div class="mt-2">
                  <input type="text" name="rg_number" id="rg_number" maxlength="20"
                    v-model="rg_number"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <div class="sm:col-span-3">
                <label for="rg_issuer" class="block text-sm font-medium leading-6 text-gray-900">RG Issuer</label>
                <div class="mt-2">
                  <input type="text" name="rg_issuer" id="rg_issuer" maxlength="50"
                    v-model="rg_issuer"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <div class="sm:col-span-3">
                <label for="state" class="block text-sm font-medium leading-6 text-gray-900">State</label>
                <div class="mt-2">
                  <input type="text" name="state" id="state" maxlength="2"
                    v-model="state"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <div class="sm:col-span-3">
                <label for="university" class="block text-sm font-medium leading-6 text-gray-900">University</label>
                <div class="mt-2">
                  <input type="text" name="university" id="university" maxlength="100"
                    v-model="university"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <div class="sm:col-span-3">
                <label for="neighborhood" class="block text-sm font-medium leading-6 text-gray-900">Neighborhood</label>
                <div class="mt-2">
                  <input type="text" name="neighborhood" id="neighborhood" maxlength="100"
                    v-model="neighborhood"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <div class="sm:col-span-3">
                <label for="city" class="block text-sm font-medium leading-6 text-gray-900">City</label>
                <div class="mt-2">
                  <input type="text" name="city" id="city" maxlength="50"
                    v-model="city"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <div class="sm:col-span-3">
                <label for="uf" class="block text-sm font-medium leading-6 text-gray-900">UF</label>
                <div class="mt-2">
                  <input type="text" name="uf" id="uf" maxlength="2"
                    v-model="uf"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>
            </div>
          </div>
          <div class="sm:col-span-3">
                <label for="total_score" class="block text-sm font-medium leading-6 text-gray-900">Total Score</label>
                <div class="mt-2">
                  <input type="text" name="total_score" id="total_score"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>
              <div class="sm:col-span-3">
                <label for="partial_score" class="block text-sm font-medium leading-6 text-gray-900">Partial Score</label>
                <div class="mt-2">
                  <input type="text" name="partial_score" id="partial_score"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
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
        <div class="sm:col-span-2">
                <label for="term_accepted" class="block text-sm font-medium leading-6 text-gray-900">Term Accepted</label>
                <div class="mt-2">
                  <input type="checkbox" id="term_accepted" name="term_accepted"
                    class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600" />
                </div>
              </div>
        <div class="mt-6 flex items-center justify-end gap-x-6">
          <button type="button" class="text-sm font-semibold leading-6 text-gray-900">Cancel</button>
          <button type="submit" class="rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Save</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import { getUserData } from '../utils/auth';
import axios from 'axios';
import { notify } from 'notiwind';

export default {
  name: 'Submission',
  data() {
    return {
      term_accepted: false,
      guardian_name: '',
      mother_name: '',
      father_name: '',
      birth_date: '',
      phone: '',
      email: '',
      rg_number: '',
      rg_issuer: '',
      state: '',
      university: '',
      neighborhood: '',
      city: '',
      uf: '',
      total_score: '',
      partial_score: '',
    };
  },
  methods: {
    async handleSubmit() {
      // Validar campos e preparar formData
      let user = await getUserData();
      const formData = new FormData();
      formData.append('cpf', user.cpf);
      formData.append('term_accepted', this.term_accepted ? 'True' : 'False');
      formData.append('guardian_name', this.guardian_name);
      formData.append('mother_name', this.mother_name);
      formData.append('father_name', this.father_name);
      formData.append('birth_date', this.birth_date);
      formData.append('phone', this.phone);
      formData.append('email', this.email);
      formData.append('rg_number', this.rg_number);
      formData.append('rg_issuer', this.rg_issuer);
      formData.append('state', this.state);
      formData.append('university', this.university);
      formData.append('neighborhood', this.neighborhood);
      formData.append('city', this.city);
      formData.append('uf', this.uf);
      formData.append('total_score', this.total_score);
      formData.append('partial_score', this.partial_score);

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

        // Limpar formulário após o envio
        this.clearForm();
      } catch (error) {
        if (error.response && error.response.data && error.response.data.error === "['allready submited']") {
          notify({
            group: 'error',
            title: 'Error',
            text: 'You have already submitted the form.',
            type: 'error',
          });
        } else {
          console.error('Erro ao criar submissão:', error);
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
      // Limpar todos os campos do formulário após a submissão bem-sucedida
      this.term_accepted = false;
      this.guardian_name = '';
      this.mother_name = '';
      this.father_name = '';
      this.birth_date = '';
      this.phone = '';
      this.email = '';
      this.rg_number = '';
      this.rg_issuer = '';
      this.state = '';
      this.university = '';
      this.neighborhood = '';
      this.city = '';
      this.uf = '';
      this.total_score = '';
      this.partial_score = '';
      // Limpar o campo de arquivo se estiver definido
      if (this.$refs.document) {
        this.$refs.document.value = null;
      }
    },
  },
};

</script>
<style scoped>
/* Add any additional styles if necessary */
</style>
