<template>
  <div class="min-h-screen bg-gray-100">
    <!-- Header -->
    <header class="bg-white shadow">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4 flex justify-between items-center">
        <div>
          <h1 class="text-3xl font-bold text-gray-900">Student Portfolio</h1>
          <p class="text-gray-600 mt-1">Welcome, {{ user?.username }}</p>
        </div>
        <button
          @click="handleLogout"
          class="bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded-lg transition"
        >
          Logout
        </button>
      </div>
    </header>

    <!-- Main Content -->
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <!-- Profile Card -->
      <div class="bg-white rounded-lg shadow p-6 mb-8">
        <div class="flex items-center justify-between">
          <div>
            <h2 class="text-2xl font-bold text-gray-900 mb-2">{{ user?.username }}</h2>
            <p class="text-gray-600 mb-1">
              <span class="font-medium">Email:</span> {{ user?.email }}
            </p>
            <p class="text-gray-600 mb-3">
              <span class="font-medium">Role:</span>
              <span
                :class="[
                  'ml-2 px-3 py-1 rounded-full text-xs font-medium',
                  user?.role === 'admin'
                    ? 'bg-blue-100 text-blue-800'
                    : 'bg-green-100 text-green-800'
                ]"
              >
                {{ user?.role }}
              </span>
            </p>
            <p class="text-gray-600">
              <span class="font-medium">Member since:</span>
              {{ user?.created_at ? new Date(user.created_at).toLocaleDateString() : '-' }}
            </p>
          </div>
          <div class="text-right">
            <div class="w-16 h-16 bg-gradient-to-br from-blue-400 to-purple-500 rounded-full flex items-center justify-center text-white text-2xl font-bold">
              {{ user?.username?.charAt(0)?.toUpperCase() || '?' }}
            </div>
          </div>
        </div>
      </div>

      <!-- Portfolio Section -->
      <div class="bg-white rounded-lg shadow">
        <div class="px-6 py-4 border-b border-gray-200">
          <h2 class="text-xl font-bold text-gray-900">My Portfolio Items</h2>
        </div>

        <div v-if="items.length === 0" class="px-6 py-8 text-center text-gray-500">
          <p>No portfolio items yet</p>
        </div>

        <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 p-6">
          <div
            v-for="item in items"
            :key="item.id"
            class="border border-gray-200 rounded-lg p-4 hover:shadow-lg transition"
          >
            <h3 class="text-lg font-semibold text-gray-900 mb-2">{{ item.title }}</h3>
            <p class="text-gray-600 text-sm mb-4">{{ item.description }}</p>
            <div class="flex gap-2">
              <button class="flex-1 bg-blue-500 hover:bg-blue-600 text-white font-medium py-2 px-3 rounded transition text-sm">
                View
              </button>
              <button class="flex-1 bg-gray-300 hover:bg-gray-400 text-gray-800 font-medium py-2 px-3 rounded transition text-sm">
                Edit
              </button>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue'
import type { Ref } from 'vue'
import { useRouter } from 'nuxt/app'
import { $fetch } from 'ofetch'
import { useAuth } from '../../composables/useAuth'

const { user, logout, apiBase, token } = useAuth()
const router = useRouter()

const items: Ref<any[]> = ref([])

const fetchItems = async () => {
  try {
    const response = await $fetch(`${apiBase}/api/items/`, {
      headers: {
        'Authorization': `Bearer ${token.value}`
      }
    })
    items.value = response
  } catch (error) {
    console.error('Failed to fetch items:', error)
  }
}

const handleLogout = () => {
  logout()
  router.push('/login')
}

onMounted(() => {
  fetchItems()
})
</script>
