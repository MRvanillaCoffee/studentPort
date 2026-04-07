<template>
  <div class="min-h-screen bg-gradient-to-br from-blue-500 to-purple-600 flex items-center justify-center">
    <div class="bg-white rounded-lg shadow-2xl p-8 w-full max-w-md">
      <div class="text-center mb-8">
        <h1 class="text-3xl font-bold text-gray-800">Student Portfolio</h1>
        <p class="text-gray-500 mt-2">Login to your account</p>
      </div>

      <form @submit.prevent="handleLogin" class="space-y-6">
        <!-- Username Field -->
        <div>
          <label for="username" class="block text-sm font-medium text-gray-700 mb-2">
            Username
          </label>
          <input
            id="username"
            v-model="formData.username"
            type="text"
            placeholder="Enter your username"
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
            placeholder="Enter your password"
            class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
            required
          />
        </div>

        <!-- Error Message -->
        <div v-if="errorMessage" class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded-lg">
          {{ errorMessage }}
        </div>

        <!-- Loading State -->
        <div v-if="loading" class="bg-blue-100 border border-blue-400 text-blue-700 px-4 py-3 rounded-lg">
          Logging in...
        </div>

        <!-- Submit Button -->
        <button
          type="submit"
          :disabled="loading"
          class="w-full bg-blue-500 hover:bg-blue-600 disabled:bg-gray-400 text-white font-bold py-2 px-4 rounded-lg transition duration-200"
        >
          {{ loading ? 'Logging in...' : 'Login' }}
        </button>
      </form>

      <!-- Register Link -->
      <p class="text-center text-gray-600 mt-6">
        Don't have an account?
        <NuxtLink to="/register" class="text-blue-500 hover:text-blue-600 font-medium">
          Register here
        </NuxtLink>
      </p>

      <!-- Demo Credentials -->
      <div class="mt-8 p-4 bg-gray-100 rounded-lg">
        <p class="text-xs font-semibold text-gray-600 mb-2">Demo Credentials:</p>
        <p class="text-xs text-gray-600">Admin: admin / password123</p>
        <p class="text-xs text-gray-600">Viewer: viewer / password123</p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { reactive, ref } from 'vue'
import { useRouter } from 'nuxt/app'
import { useAuth } from '../composables/useAuth'

const { login } = useAuth()
const router = useRouter()

const formData = reactive({
  username: '',
  password: ''
})

const loading = ref(false)
const errorMessage = ref('')

const handleLogin = async () => {
  loading.value = true
  errorMessage.value = ''

  const result = await login(formData.username, formData.password)
  
  if (result.success) {
    // Redirect based on role
    if (result.user?.role === 'admin') {
      router.push('/admin')
    } else {
      router.push('/viewer')
    }
  } else {
    errorMessage.value = result.error || 'Login failed'
  }

  loading.value = false
}
</script>
