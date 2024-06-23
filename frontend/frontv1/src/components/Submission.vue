<template>
    <form>
      <div class="space-y-12">
        <div class="border-b border-gray-900/10 pb-12">
          <h2 class="text-base font-semibold leading-7 text-gray-900">Submission Form</h2>
          <p class="mt-1 text-sm leading-6 text-gray-600">Please fill out the form below.</p>
  
          <div class="mt-10 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6">
            <div class="sm:col-span-4">
              <label for="student" class="block text-sm font-medium leading-6 text-gray-900">Student</label>
              <div class="mt-2">
                <select id="student" name="student" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6">
                  <!-- Options will be dynamically loaded -->
                </select>
              </div>
            </div>
  
            <div class="sm:col-span-2">
              <label for="term_accepted" class="block text-sm font-medium leading-6 text-gray-900">Term Accepted</label>
              <div class="mt-2">
                <input type="checkbox" id="term_accepted" name="term_accepted" class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600" />
              </div>
            </div>
  
            <div class="sm:col-span-3">
              <label for="guardian_name" class="block text-sm font-medium leading-6 text-gray-900">Guardian Name</label>
              <div class="mt-2">
                <input type="text" name="guardian_name" id="guardian_name" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
              </div>
            </div>
  
            <div class="sm:col-span-3">
              <label for="mother_name" class="block text-sm font-medium leading-6 text-gray-900">Mother's Name</label>
              <div class="mt-2">
                <input type="text" name="mother_name" id="mother_name" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
              </div>
            </div>
  
            <div class="sm:col-span-3">
              <label for="father_name" class="block text-sm font-medium leading-6 text-gray-900">Father's Name</label>
              <div class="mt-2">
                <input type="text" name="father_name" id="father_name" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
              </div>
            </div>
  
            <div class="sm:col-span-3">
              <label for="birth_date" class="block text-sm font-medium leading-6 text-gray-900">Birth Date</label>
              <div class="mt-2">
                <input type="date" name="birth_date" id="birth_date" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
              </div>
            </div>
  
            <div class="sm:col-span-3">
              <label for="phone" class="block text-sm font-medium leading-6 text-gray-900">Phone</label>
              <div class="mt-2">
                <input type="text" name="phone" id="phone" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
              </div>
            </div>
  
            <div class="sm:col-span-3">
              <label for="email" class="block text-sm font-medium leading-6 text-gray-900">Email</label>
              <div class="mt-2">
                <input type="email" name="email" id="email" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
              </div>
            </div>
  
            <div class="sm:col-span-3">
              <label for="cpf" class="block text-sm font-medium leading-6 text-gray-900">CPF</label>
              <div class="mt-2">
                <input type="text" name="cpf" id="cpf" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
              </div>
            </div>
  
            <div class="sm:col-span-3">
              <label for="rg_number" class="block text-sm font-medium leading-6 text-gray-900">RG Number</label>
              <div class="mt-2">
                <input type="text" name="rg_number" id="rg_number" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
              </div>
            </div>
  
            <div class="sm:col-span-3">
              <label for="rg_issuer" class="block text-sm font-medium leading-6 text-gray-900">RG Issuer</label>
              <div class="mt-2">
                <input type="text" name="rg_issuer" id="rg_issuer" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
              </div>
            </div>
  
            <div class="sm:col-span-3">
              <label for="state" class="block text-sm font-medium leading-6 text-gray-900">State</label>
              <div class="mt-2">
                <input type="text" name="state" id="state" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
              </div>
            </div>
  
            <div class="sm:col-span-3">
              <label for="university" class="block text-sm font-medium leading-6 text-gray-900">University</label>
              <div class="mt-2">
                <input type="text" name="university" id="university" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
              </div>
            </div>
  
            <div class="sm:col-span-3">
              <label for="neighborhood" class="block text-sm font-medium leading-6 text-gray-900">Neighborhood</label>
              <div class="mt-2">
                <input type="text" name="neighborhood" id="neighborhood" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
              </div>
            </div>
  
            <div class="sm:col-span-3">
              <label for="city" class="block text-sm font-medium leading-6 text-gray-900">City</label>
              <div class="mt-2">
                <input type="text" name="city" id="city" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
              </div>
            </div>
  
            <div class="sm:col-span-3">
              <label for="uf" class="block text-sm font-medium leading-6 text-gray-900">UF</label>
              <div class="mt-2">
                <input type="text" name="uf" id="uf" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
              </div>
            </div>
  
            <div class="sm:col-span-3">
              <label for="total_score" class="block text-sm font-medium leading-6 text-gray-900">Total Score</label>
              <div class="mt-2">
                <input type="text" name="total_score" id="total_score" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
              </div>
            </div>
  
            <div class="sm:col-span-3">
              <label for="partial_score" class="block text-sm font-medium leading-6 text-gray-900">Partial Score</label>
              <div class="mt-2">
                <input type="text" name="partial_score" id="partial_score" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
              </div>
            </div>
  
            <div class="sm:col-span-6">
              <label for="document" class="block text-sm font-medium leading-6 text-gray-900">Document</label>
              <div class="mt-2">
                <input type="file" name="document" id="document" class="block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 focus:outline-none" />
              </div>
            </div>
          </div>
        </div>
  
        <div class="mt-6 flex items-center justify-end gap-x-6">
          <button type="button" class="text-sm font-semibold leading-6 text-gray-900">Cancel</button>
          <button type="submit" class="rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Save</button>
        </div>
      </div>
    </form>
  </template>
  
  <script>
  export default {
    name: 'SubmissionForm',
    data() {
      return {
        // Data properties for the form fields can be added here if needed
      };
    },
    methods: {
      // Methods for form submission and other actions can be added here
    }
  };
  </script>
  
  <style scoped>
  /* Add any additional styles if necessary */
  </style>
  