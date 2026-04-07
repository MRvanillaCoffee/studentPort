<template>
  <div>
    <NuxtRouteAnnouncer />
    <NuxtPage />
  </div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue'
import { useAuth } from '../composables/useAuth'

// Initialize auth on mount
const { loadAuth } = useAuth()

onMounted(() => {
  loadAuth()
})
</script>
