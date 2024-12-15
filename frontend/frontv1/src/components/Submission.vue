<template>
  <div>
    <div class="container mx-auto mt-8 px-4">
      <form @submit.prevent="handleSubmit()">
        <div class="space-y-12">
          <div class="border-b border-gray-900/10 pb-12">
            <h2 class="text-base font-semibold leading-7 text-gray-900">Formulário de Envio</h2>
            <p class="mt-1 text-sm leading-6 text-gray-600">Por favor, preencha o formulário abaixo.</p>
            <div class="mt-10 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6">

              <div class="sm:col-span-3">
                <label for="birth_city" class="block text-sm font-medium leading-6 text-gray-900">Cidade de
                  Nascimento</label>
                <div class="mt-2">
                  <input type="text" name="birth_city" id="birth_city" maxlength="100" v-model="birth_city"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <div class="sm:col-span-3">
                <label for="nationality" class="block text-sm font-medium leading-6 text-gray-900">Nacionalidade</label>
                <div class="mt-2">
                  <select name="nationality" id="nationality" v-model="nationality"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                    <option value="" disabled selected>Selecione a Nacionalidade</option>
                    <option v-for="(label, value) in Nationalities" :key="value" :value="value">{{ label }}</option>
                  </select>
                </div>
              </div>


              <div class="sm:col-span-3">
                <label for="birth_date" class="block text-sm font-medium leading-6 text-gray-900">Data de
                  Nascimento</label>
                <div class="mt-2">
                  <input type="date" name="birth_date" id="birth_date" v-model="birth_date"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <div class="sm:col-span-3">
                <label for="marital_status" class="block text-sm font-medium leading-6 text-gray-900">Estado
                  Civil</label>
                <div class="mt-2">
                  <select name="marital_status" id="marital_status" v-model="marital_status"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                    <option value="" disabled selected>Selecione o estado civil</option>
                    <option v-for="(label, value) in MaritalStatus" :key="value" :value="value">{{ label }}</option>
                  </select>
                </div>
              </div>
              <div class="sm:col-span-3">
                <label for="mother_name" class="block text-sm font-medium leading-6 text-gray-900">Nome da Mãe</label>
                <div class="mt-2">
                  <input type="text" name="mother_name" id="mother_name" maxlength="100" v-model="mother_name"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <div class="sm:col-span-3">
                <label for="father_name" class="block text-sm font-medium leading-6 text-gray-900">Nome do Pai</label>
                <div class="mt-2">
                  <input type="text" name="father_name" id="father_name" maxlength="100" v-model="father_name"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <div class="sm:col-span-3">
                <label for="gender" class="block text-sm font-medium leading-6 text-gray-900">Gênero</label>
                <div class="mt-2">
                  <select name="gender" id="gender" v-model="gender"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                    <option value="" disabled selected>Selecione o Gênero</option>
                    <option v-for="(label, value) in Gender" :key="value" :value="value">{{ label }}</option>
                  </select>
                </div>
              </div>

              <div class="sm:col-span-3">
                <label for="blood_type" class="block text-sm font-medium leading-6 text-gray-900">Tipo Sanguíneo</label>
                <div class="mt-2">
                  <select name="blood_type" id="blood_type" v-model="blood_type"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                    <option value="" disabled selected>Selecione o tipo sanguíneo</option>
                    <option v-for="(label, value) in BloodType" :key="value" :value="value">{{ label }}</option>
                  </select>
                </div>
              </div>


              <div class="sm:col-span-3">
                <label for="rh_factor" class="block text-sm font-medium leading-6 text-gray-900">Fator RH</label>
                <div class="mt-2">
                  <select name="rh_factor" id="rh_factor" v-model="rh_factor"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                    <option value="" disabled selected>Selecione o Fator RH</option>
                    <option v-for="(label, value) in RhFactor" :key="value" :value="value">{{ label }}</option>
                  </select>
                </div>
              </div>


              <div class="sm:col-span-3">
                <label for="ethnicity" class="block text-sm font-medium leading-6 text-gray-900">Etnia</label>
                <div class="mt-2">
                  <select name="ethnicity" id="ethnicity" v-model="ethnicity"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                    <option value="" disabled selected>Selecione a etnia</option>
                    <option v-for="(label, value) in Ethnicity" :key="value" :value="value">{{ label }}</option>
                  </select>
                </div>
              </div>


              <div class="sm:col-span-3">
                <label for="physical_disability" class="block text-sm font-medium leading-6 text-gray-900">Deficiência
                  Física</label>
                <div class="mt-2">
                  <select name="physical_disability" id="physical_disability" v-model="physical_disability"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                    <option value="" disabled selected>Selecione</option>
                    <option value='true'>Sim</option>
                    <option value='false'>Não</option>
                  </select>
                </div>
              </div>

              <div class="sm:col-span-3" v-if="physical_disability === 'true'">
                <label for="disability_details" class="block text-sm font-medium leading-6 text-gray-900">Detalhes da
                  Deficiência</label>
                <div class="mt-2">
                  <input type="text" name="disability_details" id="disability_details" maxlength="100"
                    v-model="disability_details"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <div class="sm:col-span-3" v-if="physical_disability === 'true'">
                <label for="disability_degree" class="block text-sm font-medium leading-6 text-gray-900">Grau de
                  Deficiência</label>
                <div class="mt-2">
                  <select name="disability_degree" id="disability_degree" v-model="disability_degree"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                    <option value="" disabled selected>Selecione o Grau</option>
                    <option value="leve">Leve</option>
                    <option value="moderado">Moderado</option>
                    <option value="grave">Grave</option>
                  </select>
                </div>
              </div>

              <div class="sm:col-span-3">
                <label for="psychological_disorder" class="block text-sm font-medium leading-6 text-gray-900">Transtorno
                  Psicológico</label>
                <div class="mt-2">
                  <input type="text" name="psychological_disorder" id="psychological_disorder" maxlength="100"
                    v-model="psychological_disorder"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>


              <div class="sm:col-span-3">
                <label for="street_address" class="block text-sm font-medium leading-6 text-gray-900">Endereço</label>
                <div class="mt-2">
                  <input type="text" name="street_address" id="street_address" maxlength="255" v-model="street_address"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <div class="sm:col-span-3">
                <label for="number" class="block text-sm font-medium leading-6 text-gray-900">Número</label>
                <div class="mt-2">
                  <input type="text" name="number" id="number" maxlength="10" v-model="number"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <div class="sm:col-span-3">
                <label for="complement" class="block text-sm font-medium leading-6 text-gray-900">Complemento</label>
                <div class="mt-2">
                  <input type="text" name="complement" id="complement" maxlength="100" v-model="complement"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <div class="sm:col-span-3">
                <label for="neighborhood" class="block text-sm font-medium leading-6 text-gray-900">Bairro</label>
                <div class="mt-2">
                  <input type="text" name="neighborhood" id="neighborhood" maxlength="100" v-model="neighborhood"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <div class="sm:col-span-3">
                <label for="city" class="block text-sm font-medium leading-6 text-gray-900">Cidade</label>
                <div class="mt-2">
                  <input type="text" name="city" id="city" maxlength="100" v-model="city"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <div class="sm:col-span-3">
                <label for="state" class="block text-sm font-medium leading-6 text-gray-900">Estado</label>
                <div class="mt-2">
                  <select name="state" id="state" v-model="state"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                    <option value="" disabled selected>Selecione o Estado</option>
                    <option v-for="(label, value) in States" :key="value" :value="value">{{ label }}</option>
                  </select>
                </div>
              </div>


              <div class="sm:col-span-3">
                <label for="postal_code" class="block text-sm font-medium leading-6 text-gray-900">CEP</label>
                <div class="mt-2">
                  <input type="text" name="postal_code" id="postal_code" maxlength="10" v-model="postal_code"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <div class="sm:col-span-3">
                <label for="rg" class="block text-sm font-medium leading-6 text-gray-900">RG</label>
                <div class="mt-2">
                  <input type="text" name="rg" id="rg" maxlength="20" v-model="rg"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <div class="sm:col-span-3">
                <label for="birth_city" class="block text-sm font-medium leading-6 text-gray-900">Cidade de
                  Nascimento</label>
                <div class="mt-2">
                  <input type="text" name="birth_city" id="birth_city" maxlength="100" v-model="birth_city"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <div class="sm:col-span-3">
                <label for="state" class="block text-sm font-medium leading-6 text-gray-900">Estado</label>
                <div class="mt-2">
                  <select name="state" id="state" v-model="birth_state"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                    <option value="" disabled selected>Selecione o Estado</option>
                    <option v-for="(label, value) in States" :key="value" :value="value">{{ label }}</option>
                  </select>
                </div>
              </div>

              <div class="sm:col-span-3">
                <label for="high_school_graduation_year" class="block text-sm font-medium leading-6 text-gray-900">Ano
                  de Conclusão do Ensino Médio</label>
                <div class="mt-2">
                  <input type="text" name="high_school_graduation_year" id="high_school_graduation_year" maxlength="4"
                    v-model="high_school_graduation_year"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <div class="sm:col-span-3">
                <label for="university_name" class="block text-sm font-medium leading-6 text-gray-900">Nome da
                  Universidade</label>
                <div class="mt-2">
                  <input type="text" name="university_name" id="university_name" maxlength="100"
                    v-model="university_name"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <div class="sm:col-span-3">
                <label for="graduation_year" class="block text-sm font-medium leading-6 text-gray-900">Ano de Conclusão
                  da Graduação</label>
                <div class="mt-2">
                  <input type="text" name="graduation_year" id="graduation_year" maxlength="4" v-model="graduation_year"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <div class="sm:col-span-3">
                <label for="graduation_course" class="block text-sm font-medium leading-6 text-gray-900">Curso de
                  Graduação</label>
                <div class="mt-2">
                  <input type="text" name="graduation_course" id="graduation_course" maxlength="100"
                    v-model="graduation_course"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <div class="sm:col-span-3">
                <label for="current_ubs_name" class="block text-sm font-medium leading-6 text-gray-900">Nome da UBS
                  Atual</label>
                <div class="mt-2">
                  <input type="text" name="current_ubs_name" id="current_ubs_name" maxlength="100"
                    v-model="current_ubs_name"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <div class="sm:col-span-3">
                <label for="ubs_type" class="block text-sm font-medium leading-6 text-gray-900">Tipo de UBS</label>
                <div class="mt-2">
                  <select name="ubs_type" id="ubs_type" v-model="ubs_type"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                    <option value="" disabled selected>Selecione o tipo de UBS</option>
                    <option v-for="(label, value) in UbsType" :key="value" :value="value">{{ label }}</option>
                  </select>
                </div>
              </div>


              <div class="sm:col-span-3">
                <label class="block text-sm font-medium leading-6 text-gray-900">Documentos</label>
                <div class="mt-2 space-y-4">
                  <div>
                    <label for="rg_cpf_copy" class="block text-sm font-medium leading-6 text-gray-900">Cópia do
                      RG/CPF</label>
                    <input type="file" name="rg_cpf_copy" id="rg_cpf_copy" accept=".pdf" ref="rg_cpf_copy"
                      class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                  </div>

                  <div>
                    <label for="reservista_cert_copy"
                      class="block text-sm font-medium leading-6 text-gray-900">Certificado de Reservista</label>
                    <input type="file" name="reservista_cert_copy" id="reservista_cert_copy" accept=".pdf"
                      ref="reservista_cert_copy"
                      class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                  </div>

                  <div>
                    <label for="diploma_copy" class="block text-sm font-medium leading-6 text-gray-900">Diploma</label>
                    <input type="file" name="diploma_copy" id="diploma_copy" accept=".pdf" ref="diploma_copy"
                      class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                  </div>

                  <div>
                    <label for="marriage_certificate_copy"
                      class="block text-sm font-medium leading-6 text-gray-900">Certidão de Casamento</label>
                    <input type="file" name="marriage_certificate_copy" id="marriage_certificate_copy" accept=".pdf"
                      ref="marriage_certificate_copy"
                      class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                  </div>

                  <div>
                    <label for="address_proof_copy"
                      class="block text-sm font-medium leading-6 text-gray-900">Comprovante de Endereço</label>
                    <input type="file" name="address_proof_copy" id="address_proof_copy" accept=".pdf"
                      ref="address_proof_copy"
                      class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                  </div>

                  <div>
                    <label for="residence_internet_copy"
                      class="block text-sm font-medium leading-6 text-gray-900">Comprovante de Residência e
                      Internet</label>
                    <input type="file" name="residence_internet_copy" id="residence_internet_copy" accept=".pdf"
                      ref="residence_internet_copy"
                      class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                  </div>

                  <div>
                    <label for="ubs_internet_copy" class="block text-sm font-medium leading-6 text-gray-900">Comprovante
                      de UBS</label>
                    <input type="file" name="ubs_internet_copy" id="ubs_internet_copy" accept=".pdf"
                      ref="ubs_internet_copy"
                      class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                  </div>
                </div>
              </div>

              <div class="sm:col-span-3">
                <label for="internet_speed" class="block text-sm font-medium leading-6 text-gray-900">Velocidade da
                  Internet</label>
                <div class="mt-2">
                  <input type="text" name="internet_speed" id="internet_speed" maxlength="10" v-model="internet_speed"
                    class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                </div>
              </div>

              <div class="sm:col-span-3">
                <label for="internet_availability">Disponibilidade de Internet:</label>
                <select v-model="internet_availability" id="internet_availability">
                  <option v-for="(label, value) in InternetAvailabilityOptions" :key="value" :value="value">
                    {{ label }}
                  </option>
                </select>
              </div>

              <div class="sm:col-span-3">
                <label for="energy_availability">Disponibilidade de Energia:</label>
                <select v-model="energy_availability" id="energy_availability">
                  <option v-for="(label, value) in EnergyAvailabilityOptions" :key="value" :value="value">
                    {{ label }}
                  </option>
                </select>
              </div>

              <div class="sm:col-span-3">
                <div class="flex items-center gap-x-3">
                  <input id="terms_accepted" name="terms_accepted" type="checkbox" v-model="terms_accepted"
                    class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600" />
                  <label for="terms_accepted" class="text-sm font-medium leading-6 text-gray-900">Aceito os termos e
                    condições</label>
                </div>
              </div>
            </div>
          </div>

          <div class="pt-5">
            <button type="submit"
              class="inline-block rounded-md bg-indigo-600 px-3.5 py-1.5 text-sm font-semibold leading-6 text-white ring-1 ring-gray-900/10 hover:ring-gray-900/20">Enviar</button>
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
import { UbsType } from '../enums/submission.enum';

export default {
  name: 'Submission',
  data() {
    return {
      term_accepted: false,
      mother_name: '',
      father_name: '',
      blood_type: '',
      rh_factor: '',
      gender: '',
      ethnicity: '',
      birth_date: '',
      nationality: '',
      birth_city: '',
      birth_state: '',
      street_address: '',
      number: '',
      complement: '',
      neighborhood: '',
      city: '',
      state: '',
      postal_code: '',
      rg: '',
      high_school_graduation_year: '',
      university_name: '',
      graduation_year: '',
      graduation_course: '',
      current_ubs_name: '',
      ubs_type: '',
      marital_status: '',
      physical_disability: '',
      disability_details: '',
      disability_degree: '',
      psychological_disorder: '',
      internet_availability: '',
      energy_availability: '',
      internet_availability: '',
      energy_availability: '',
      internet_speed: '',
      rg_cpf_copy: null,
      marriage_certificate_copy: null,
      reservista_cert_copy: null,
      address_proof_copy: null,
      military_certificate_copy: null,
      ubs_internet_copy: null,
      residence_internet_copy: null,
    };
  },
  created() {
    this.loadFormData();
  },
  watch: {
    term_accepted(val) { this.saveFormData(); },
    mother_name(val) { this.saveFormData(); },
    father_name(val) { this.saveFormData(); },
    blood_type(val) { this.saveFormData(); },
    rh_factor(val) { this.saveFormData(); },
    gender(val) { this.saveFormData(); },
    ethnicity(val) { this.saveFormData(); },
    birth_date(val) { this.saveFormData(); },
    nationality(val) { this.saveFormData(); },
    birth_city(val) { this.saveFormData(); },
    birth_state(val) { this.saveFormData(); },
    street_address(val) { this.saveFormData(); },
    number(val) { this.saveFormData(); },
    complement(val) { this.saveFormData(); },
    neighborhood(val) { this.saveFormData(); },
    city(val) { this.saveFormData(); },
    state(val) { this.saveFormData(); },
    postal_code(val) { this.saveFormData(); },
    rg(val) { this.saveFormData(); },
    high_school_graduation_year(val) { this.saveFormData(); },
    university_name(val) { this.saveFormData(); },
    graduation_year(val) { this.saveFormData(); },
    graduation_course(val) { this.saveFormData(); },
    current_ubs_name(val) { this.saveFormData(); },
    ubs_type(val) { this.saveFormData(); },
    marital_status(val) { this.saveFormData(); },
    physical_disability(val) { this.saveFormData(); },
    disability_details(val) { this.saveFormData(); },
    disability_degree(val) { this.saveFormData(); },
    psychological_disorder(val) { this.saveFormData(); },
    rg_cpf_copy(val) { this.saveFormData(); },
    internet_speed(val) { this.saveFormData(); },
    marriage_certificate_copy(val) { this.saveFormData(); },
    residence_internet_copy(val) { this.saveFormData(); },
    diploma_copy(val) { this.saveFormData(); },
    address_proof_copy(val) { this.saveFormData(); },
    ubs_internet_copy(val) { this.saveFormData(); },
    reservista_cert_copy(val) { this.saveFormData(); },
    military_certificate_copy(val) { this.saveFormData(); },
  },
  methods: {
    saveFormData() {
      const formData = {
        term_accepted: this.term_accepted,
        mother_name: this.mother_name,
        father_name: this.father_name,
        blood_type: this.blood_type,
        rh_factor: this.rh_factor,
        gender: this.gender,
        ethnicity: this.ethnicity,
        birth_date: this.birth_date,
        nationality: this.nationality,
        birth_city: this.birth_city,
        birth_state: this.birth_state,
        street_address: this.street_address,
        number: this.number,
        complement: this.complement,
        neighborhood: this.neighborhood,
        city: this.city,
        state: this.state,
        postal_code: this.postal_code,
        rg: this.rg,
        high_school_graduation_year: this.high_school_graduation_year,
        university_name: this.university_name,
        graduation_year: this.graduation_year,
        graduation_course: this.graduation_course,
        current_ubs_name: this.current_ubs_name,
        ubs_type: this.ubs_type,
        diploma_copy: this.diploma_copy,
        marital_status: this.marital_status,
        physical_disability: this.physical_disability,
        disability_details: this.disability_details,
        disability_degree: this.disability_degree,
        psychological_disorder: this.psychological_disorder,
      };
      localStorage.setItem('formData', JSON.stringify(formData));
    },
    loadFormData() {
      const formData = JSON.parse(localStorage.getItem('formData'));
      if (formData) {
        this.term_accepted = formData.term_accepted;
        this.mother_name = formData.mother_name;
        this.father_name = formData.father_name;
        this.blood_type = formData.blood_type;
        this.rh_factor = formData.rh_factor;
        this.gender = formData.gender;
        this.ethnicity = formData.ethnicity;
        this.birth_date = formData.birth_date;
        this.nationality = formData.nationality;
        this.birth_city = formData.birth_city;
        this.birth_state = formData.birth_state;
        this.street_address = formData.street_address;
        this.number = formData.number;
        this.complement = formData.complement;
        this.neighborhood = formData.neighborhood;
        this.city = formData.city;
        this.state = formData.state;
        this.postal_code = formData.postal_code;
        this.rg = formData.rg;
        this.high_school_graduation_year = formData.high_school_graduation_year;
        this.university_name = formData.university_name;
        this.graduation_year = formData.graduation_year;
        this.graduation_course = formData.graduation_course;
        this.current_ubs_name = formData.current_ubs_name;
        this.ubs_type = formData.ubs_type;
        this.marital_status = formData.marital_status;
        this.physical_disability = formData.physical_disability;
        this.disability_details = formData.disability_details;
        this.disability_degree = formData.disability_degree;
        this.psychological_disorder = formData.psychological_disorder;
        this.internet_availability = formData.internet_availability;
        this.energy_availability = formData.energy_availability;
      }
    },
    async handleSubmit() {
      try {
        let user = await getUserData();

        const token = localStorage.getItem('token');
        const profileResponse = await axios.get(`${API_BASE_URL}/user/`, {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });
        const cpf = profileResponse.data.cpf;

        const formData = new FormData();
        formData.append('student', user.id);
        formData.append('term_accepted', this.term_accepted ? 'True' : 'False');
        formData.append('mother_name', this.mother_name);
        formData.append('father_name', this.father_name);
        formData.append('blood_type', this.blood_type);
        formData.append('rh_factor', this.rh_factor);
        formData.append('gender', this.gender);
        formData.append('ethnicity', this.ethnicity);
        formData.append('birth_date', this.birth_date);
        formData.append('nationality', this.nationality);
        formData.append('birth_city', this.birth_city);
        formData.append('birth_state', this.birth_state);
        formData.append('street_address', this.street_address);
        formData.append('number', this.number);
        formData.append('complement', this.complement);
        formData.append('neighborhood', this.neighborhood);
        formData.append('city', this.city);
        formData.append('state', this.state);
        formData.append('postal_code', this.postal_code);
        formData.append('rg', this.rg);
        formData.append('high_school_graduation_year', this.high_school_graduation_year);
        formData.append('university_name', this.university_name);
        formData.append('graduation_year', this.graduation_year);
        formData.append('graduation_course', this.graduation_course);
        formData.append('current_ubs_name', this.current_ubs_name);
        formData.append('ubs_type', this.ubs_type);
        formData.append('internet_speed', this.internet_speed);
        formData.append('internet_availability', this.internet_availability);
        formData.append('energy_availability', this.energy_availability);
        formData.append('marital_status', this.marital_status);
        formData.append('physical_disability', this.physical_disability);
        formData.append('disability_details', this.disability_details);
        formData.append('disability_degree', this.disability_degree);
        formData.append('psychological_disorder', this.psychological_disorder);
        formData.append('cpf', cpf);

        if (this.$refs.rg_cpf_copy && this.$refs.rg_cpf_copy.files.length > 0) {
          formData.append('rg_cpf_copy', this.$refs.rg_cpf_copy.files[0]);
        }
        if (this.$refs.marriage_certificate_copy && this.$refs.marriage_certificate_copy.files.length > 0) {
          formData.append('marriage_certificate_copy', this.$refs.marriage_certificate_copy.files[0]);
        }
        if (this.$refs.diploma_copy && this.$refs.diploma_copy.files.length > 0) {
          formData.append('diploma_copy', this.$refs.diploma_copy.files[0]);
        }
        if (this.$refs.residence_internet_copy && this.$refs.residence_internet_copy.files.length > 0) {
          formData.append('residence_internet_copy', this.$refs.residence_internet_copy.files[0]);
        }
        if (this.$refs.ubs_internet_copy && this.$refs.ubs_internet_copy.files.length > 0) {
          formData.append('ubs_internet_copy', this.$refs.ubs_internet_copy.files[0]);
        }
        if (this.$refs.reservista_cert_copy && this.$refs.reservista_cert_copy.files.length > 0) {
          formData.append('reservista_cert_copy', this.$refs.reservista_cert_copy.files[0]);
        }
        if (this.$refs.military_certificate_copy && this.$refs.military_certificate_copy.files.length > 0) {
          formData.append('military_certificate_copy', this.$refs.military_certificate_copy.files[0]);
        }
        if (this.$refs.address_proof_copy && this.$refs.address_proof_copy.files.length > 0) {
          formData.append('address_proof_copy', this.$refs.address_proof_copy.files[0]);
        }

        const response = await axios.post(`${API_BASE_URL}/submissions/`, formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
            'Authorization': `Bearer ${token}`
          },
        });

        notify({
          group: 'foo',
          title: 'Sucesso',
          text: 'Inscrição criada com sucesso!',
        });

        this.clearForm();
      } catch (error) {
        let errorMessage = 'Erro ao enviar a inscrição. Por favor, tente novamente.';
        if (error.response) {
          errorMessage = `Erro: ${error.response.status} - ${error.response.data.message || errorMessage}`;
          console.error('Erro na resposta do servidor:', error.response);
        } else if (error.request) {
          errorMessage = 'Não foi possível obter resposta do servidor.';
          console.error('Erro na requisição:', error.request);
        } else {
          errorMessage = `Erro: ${error.message}`;
          console.error('Erro desconhecido:', error.message);
        }

        notify({
          group: 'error',
          title: 'Erro',
          text: errorMessage,
        });
      }
    },
    clearForm() {
      this.term_accepted = false;
      this.mother_name = '';
      this.father_name = '';
      this.blood_type = '';
      this.rh_factor = '';
      this.gender = '';
      this.ethnicity = '';
      this.birth_date = null;
      this.nationality = '';
      this.birth_city = '';
      this.birth_state = '';
      this.street_address = '';
      this.number = '';
      this.complement = '';
      this.neighborhood = '';
      this.city = '';
      this.state = '';
      this.postal_code = '';
      this.rg = '';
      this.high_school_graduation_year = '';
      this.university_name = '';
      this.graduation_year = '';
      this.graduation_course = '';
      this.current_ubs_name = '';
      this.ubs_type = '';
      this.marital_status = '';
      this.physical_disability = false;
      this.disability_details = '';
      this.disability_degree = '';
      this.psychological_disorder = '';
      this.rg_cpf_copy = null;
      this.reservista_cert_copy = null;
      this.military_certificate_copy = null;
      this.address_proof_copy = null;
      localStorage.removeItem('formData');
    },
  },
  computed: {
    States() {
      return {
        'AC': 'Acre',
        'AL': 'Alagoas',
        'AP': 'Amapá',
        'AM': 'Amazonas',
        'BA': 'Bahia',
        'CE': 'Ceará',
        'DF': 'Distrito Federal',
        'ES': 'Espírito Santo',
        'GO': 'Goiás',
        'MA': 'Maranhão',
        'MT': 'Mato Grosso',
        'MS': 'Mato Grosso do Sul',
        'MG': 'Minas Gerais',
        'PA': 'Pará',
        'PB': 'Paraíba',
        'PR': 'Paraná',
        'PE': 'Pernambuco',
        'PI': 'Piauí',
        'RJ': 'Rio de Janeiro',
        'RN': 'Rio Grande do Norte',
        'RS': 'Rio Grande do Sul',
        'RO': 'Rondônia',
        'RR': 'Roraima',
        'SC': 'Santa Catarina',
        'SP': 'São Paulo',
        'SE': 'Sergipe',
        'TO': 'Tocantins',
      };
    },

    InternetAvailabilityOptions() {
      return {
        'available': 'Disponível',
        'not_available': 'Não Disponível',
        'unknown': 'Desconhecido',
      };
    },
    EnergyAvailabilityOptions() {
      return {
        'available': 'Disponível',
        'not_available': 'Não Disponível',
        'unknown': 'Desconhecido',
      };
    },

    MaritalStatus() {
      return {
        'solteiro': 'Solteiro',
        'casado': 'Casado',
        'divorciado': 'Divorciado',
        'viuvo': 'Viúvo',
        'separado': 'Separado',
      };
    },
    Nationalities() {
      return {
        'Brasileiro': 'Brasileira',
        'Estrangeira': 'Estrangeira',
      };
    },
    BloodType() {
      return {
        'A+': 'A Positivo',
        'A-': 'A Negativo',
        'B+': 'B Positivo',
        'B-': 'B Negativo',
        'AB+': 'AB Positivo',
        'AB-': 'AB Negativo',
        'O+': 'O Positivo',
        'O-': 'O Negativo',
      };
    },
    RhFactor() {
      return {
        '+': 'Positivo',
        '-': 'Negativo',
      };
    },
    Gender() {
      return {
        'M': 'Masculino',
        'F': 'Feminino',
        'O': 'Outro',
      };
    },
    Ethnicity() {
      return {
        'W': 'Branco',
        'B': 'Negro',
        'P': 'Pardo',
        'A': 'Amarelo',
        'I': 'Indígena',
      };
    },
    State() {
      return {
        'SP': 'São Paulo',
        'RJ': 'Rio de Janeiro',
        'MG': 'Minas Gerais',
        'ES': 'Espírito Santo',
      };
    },
    UbsType() {
      return {
        "PRIMARY": 'Unidade Básica de Saúde',
        "SECONDARY": 'Unidade de Saúde Secundária',
        "TERTIARY": 'Unidade de Saúde Terciária',
      };
    },
  },
};
</script>