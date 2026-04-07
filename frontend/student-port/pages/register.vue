<template>
  <div class="min-h-screen bg-gradient-to-br from-blue-500 to-purple-600 flex items-center justify-center">
    <div class="bg-white rounded-lg shadow-2xl p-8 w-full max-w-md">
      <div class="text-center mb-8">
        <h1 class="text-3xl font-bold text-gray-800">Join Us</h1>
        <p class="text-gray-500 mt-2">Create your student portfolio account</p>
      </div>

      <form @submit.prevent="handleRegister" class="space-y-4">
        <!-- Username Field -->
        <div>
          <label for="username" class="block text-sm font-medium text-gray-700 mb-2">
            Username
          </label>
          <input
            id="username"
            v-model="formData.username"
            type="text"
            placeholder="Choose a username"
            class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
            required
          />
        </div>

        <!-- Email Field -->
        <div>
          <label for="email" class="block text-sm font-medium text-gray-700 mb-2">
            Email
          </label>
          <input
            id="email"
            v-model="formData.email"
            type="email"
            placeholder="Enter your email"
            class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
            required
          />
        </div>

        <!-- Password Field -->
        <div>
          <label for="password" class="block text-sm font-medium text-gray-700 mb-2">
            Password
          </label>
          <input
            id="password"
            v-model="formData.password"
            type="password"
            placeholder="Enter a password"
            class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
            required
          />
        </div>

        <!-- Confirm Password Field -->
        <div>
          <label for="confirm_password" class="block text-sm font-medium text-gray-700 mb-2">
            Confirm Password
          </label>
          <input
            id="confirm_password"
            v-model="formData.confirmPassword"
            type="password"
            placeholder="Confirm your password"
            class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
            required
          />
        </div>

        <!-- Error Message -->
        <div v-if="errorMessage" class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded-lg text-sm">
          {{ errorMessage }}
        </div>

        <!-- Success Message -->
        <div v-if="successMessage" class="bg-green-100 border border-green-400 text-green-700 px-4 py-3 rounded-lg text-sm">
          {{ successMessage }}
        </div>

        <!-- Loading State -->
        <div v-if="loading" class="bg-blue-100 border border-blue-400 text-blue-700 px-4 py-3 rounded-lg text-sm">
          Creating account...
        </div>

        <!-- Submit Button -->
        <button
          type="submit"
          :disabled="loading"
          class="w-full bg-blue-500 hover:bg-blue-600 disabled:bg-gray-400 text-white font-bold py-2 px-4 rounded-lg transition duration-200"
        >
          {{ loading ? 'Creating account...' : 'Register' }}
        </button>
      </form>

      <!-- Login Link -->
      <p class="text-center text-gray-600 mt-6">
        Already have an account?
        <NuxtLink to="/login" class="text-blue-500 hover:text-blue-600 font-medium">
          Login here
        </NuxtLink>
      </p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { reactive, ref } from 'vue'
import { useRouter, useRuntimeConfig } from 'nuxt/app'
import { $fetch } from 'ofetch'

const router = useRouter()
const runtimeConfig = useRuntimeConfig()
const apiBase = runtimeConfig.public.apiBase

const formData = reactive({
  username: '',
  email: '',
  password: '',
  confirmPassword: '',
  role: 'viewer'
})

const loading = ref(false)
const errorMessage = ref('')
const successMessage = ref('')

const handleRegister = async () => {
  // Validate passwords match
  if (formData.password !== formData.confirmPassword) {
    errorMessage.value = 'Passwords do not match'
    return
  }

  if (formData.password.length < 6) {
    errorMessage.value = 'Password must be at least 6 characters'
    return
  }

  loading.value = true
  errorMessage.value = ''
  successMessage.value = ''

  try {
    await $fetch(`${apiBase}/api/register`, {
      method: 'POST',
      body: {
        username: formData.username,
        email: formData.email,
        password: formData.password,
        role: formData.role
      }
    })

    successMessage.value = 'Account created! Redirecting to login...'
    
    setTimeout(() => {
      router.push('/login')
    }, 2000)
  } catch (error: any) {
    errorMessage.value = error.data?.detail || 'Registration failed'
  }

  loading.value = false
}
</script>
