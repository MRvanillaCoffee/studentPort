<template>
  <div class="min-h-screen bg-gray-100">
    <!-- Header -->
    <header class="bg-white shadow">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4 flex justify-between items-center">
        <div>
          <h1 class="text-3xl font-bold text-gray-900">Admin Dashboard</h1>
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
      <!-- Stats Cards -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
        <div class="bg-white rounded-lg shadow p-6">
          <h3 class="text-gray-500 text-sm font-medium">Total Users</h3>
          <p class="text-3xl font-bold text-gray-900 mt-2">{{ stats.totalUsers }}</p>
        </div>
        <div class="bg-white rounded-lg shadow p-6">
          <h3 class="text-gray-500 text-sm font-medium">Admins</h3>
          <p class="text-3xl font-bold text-blue-600 mt-2">{{ stats.adminCount }}</p>
        </div>
        <div class="bg-white rounded-lg shadow p-6">
          <h3 class="text-gray-500 text-sm font-medium">Viewers</h3>
          <p class="text-3xl font-bold text-green-600 mt-2">{{ stats.viewerCount }}</p>
        </div>
      </div>

      <!-- Users Management Section -->
      <div class="bg-white rounded-lg shadow">
        <div class="px-6 py-4 border-b border-gray-200 flex justify-between items-center">
          <h2 class="text-xl font-bold text-gray-900">Users Management</h2>
          <button
            @click="showAddUserForm = true"
            class="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded-lg transition"
          >
            Add New User
          </button>
        </div>

        <!-- Add User Form -->
        <div v-if="showAddUserForm" class="px-6 py-4 border-b border-gray-200 bg-gray-50">
          <form @submit.prevent="handleAddUser" class="grid grid-cols-1 md:grid-cols-4 gap-4">
            <input
              v-model="newUser.username"
              type="text"
              placeholder="Username"
              class="px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
              required
            />
            <input
              v-model="newUser.email"
              type="email"
              placeholder="Email"
              class="px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
              required
            />
            <select
              v-model="newUser.role"
              class="px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
            >
              <option value="viewer">Viewer</option>
              <option value="admin">Admin</option>
            </select>
            <div class="flex gap-2">
              <button
                type="submit"
                class="bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded-lg transition flex-1"
              >
                Add User
              </button>
              <button
                type="button"
                @click="showAddUserForm = false"
                class="bg-gray-400 hover:bg-gray-500 text-white font-bold py-2 px-4 rounded-lg transition flex-1"
              >
                Cancel
              </button>
            </div>
          </form>
        </div>

        <!-- Users Table -->
        <div class="overflow-x-auto">
          <table class="w-full">
            <thead class="bg-gray-50 border-b border-gray-200">
              <tr>
                <th class="px-6 py-3 text-left text-sm font-semibold text-gray-900">Username</th>
                <th class="px-6 py-3 text-left text-sm font-semibold text-gray-900">Email</th>
                <th class="px-6 py-3 text-left text-sm font-semibold text-gray-900">Role</th>
                <th class="px-6 py-3 text-left text-sm font-semibold text-gray-900">Joined Date</th>
                <th class="px-6 py-3 text-left text-sm font-semibold text-gray-900">Actions</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-gray-200">
              <tr v-for="u in users" :key="u.id" class="hover:bg-gray-50">
                <td class="px-6 py-4 text-sm text-gray-900">{{ u.username }}</td>
                <td class="px-6 py-4 text-sm text-gray-900">{{ u.email }}</td>
                <td class="px-6 py-4 text-sm">
                  <span
                    :class="[
                      'px-3 py-1 rounded-full text-xs font-medium',
                      u.role === 'admin'
                        ? 'bg-blue-100 text-blue-800'
                        : 'bg-green-100 text-green-800'
                    ]"
                  >
                    {{ u.role }}
                  </span>
                </td>
                <td class="px-6 py-4 text-sm text-gray-900">
                  {{ new Date(u.created_at).toLocaleDateString() }}
                </td>
                <td class="px-6 py-4 text-sm">
                  <button
                    @click="deleteUser(u.id)"
                    class="text-red-600 hover:text-red-800 font-medium"
                  >
                    Delete
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
import { onMounted, reactive, ref } from 'vue'
import type { Ref } from 'vue'
import { useRouter } from 'nuxt/app'
import { $fetch } from 'ofetch'
import { useAuth } from '../../composables/useAuth'

const { user, logout, apiBase, token } = useAuth()
const router = useRouter()

const stats = reactive({
  totalUsers: 0,
  adminCount: 0,
  viewerCount: 0
})

const users: Ref<any[]> = ref([])
const showAddUserForm = ref(false)

const newUser = reactive({
  username: '',
  email: '',
  role: 'viewer',
  password: 'TempPassword123!'
})

const fetchUsers = async () => {
  try {
    const response = await $fetch(`${apiBase}/api/users/`, {
      headers: {
        'Authorization': `Bearer ${token.value}`
      }
    })
    users.value = response
    
    stats.totalUsers = response.length
    stats.adminCount = response.filter((u: any) => u.role === 'admin').length
    stats.viewerCount = response.filter((u: any) => u.role === 'viewer').length
  } catch (error) {
    console.error('Failed to fetch users:', error)
  }
}

const handleAddUser = async () => {
  try {
    await $fetch(`${apiBase}/api/register`, {
      method: 'POST',
      body: newUser,
      headers: {
        'Authorization': `Bearer ${token.value}`
      }
    })
    
    showAddUserForm.value = false
    newUser.username = ''
    newUser.email = ''
    newUser.role = 'viewer'
    
    await fetchUsers()
  } catch (error) {
    console.error('Failed to add user:', error)
    alert('Failed to add user')
  }
}

const deleteUser = async (userId: number) => {
  if (confirm('Are you sure you want to delete this user?')) {
    try {
      await $fetch(`${apiBase}/api/users/${userId}`, {
        method: 'DELETE',
        headers: {
          'Authorization': `Bearer ${token.value}`
        }
      })
      await fetchUsers()
    } catch (error) {
      console.error('Failed to delete user:', error)
      alert('Failed to delete user')
    }
  }
}

const handleLogout = () => {
  logout()
  router.push('/login')
}

onMounted(() => {
  fetchUsers()
})
</script>
