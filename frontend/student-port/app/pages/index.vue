<template>
  <div class="min-h-screen bg-gradient-to-br from-blue-500 to-purple-600">
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-20 text-center">
      <h1 class="text-5xl font-bold text-white mb-4">Student Portfolio</h1>
      <p class="text-xl text-blue-100 mb-8">
        Showcase your academic achievements and projects in one place
      </p>

      <div class="flex gap-4 justify-center">
        <NuxtLink
          to="/login"
          class="bg-white text-blue-600 font-bold py-3 px-8 rounded-lg hover:bg-gray-100 transition"
        >
          Login
        </NuxtLink>
        <NuxtLink
          to="/register"
          class="bg-blue-700 text-white font-bold py-3 px-8 rounded-lg hover:bg-blue-800 transition"
        >
          Register
        </NuxtLink>
      </div>

      <!-- Features Section -->
      <div class="mt-20 grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="bg-white bg-opacity-10 backdrop-blur-lg rounded-lg p-6 text-white">
          <div class="text-4xl mb-4">📚</div>
          <h3 class="text-xl font-bold mb-2">Organize</h3>
          <p class="text-blue-100">Manage your portfolio with ease</p>
        </div>

        <div class="bg-white bg-opacity-10 backdrop-blur-lg rounded-lg p-6 text-white">
          <div class="text-4xl mb-4">🔐</div>
          <h3 class="text-xl font-bold mb-2">Secure</h3>
          <p class="text-blue-100">Role-based access control</p>
        </div>

        <div class="bg-white bg-opacity-10 backdrop-blur-lg rounded-lg p-6 text-white">
          <div class="text-4xl mb-4">✨</div>
          <h3 class="text-xl font-bold mb-2">Professional</h3>
          <p class="text-blue-100">Impress educators and employers</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
</script>
