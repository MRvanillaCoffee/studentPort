import { defineNuxtRouteMiddleware, navigateTo } from 'nuxt/app'
import { useAuth } from '../composables/useAuth'

export default defineNuxtRouteMiddleware((to, from) => {
  const { user, isAuthenticated } = useAuth()
  const role = user.value?.role

  // Allow login and register pages without authentication
  if (to.path === '/login' || to.path === '/register') {
    if (isAuthenticated.value) {
      return navigateTo('/')
    }
    return
  }

  // Check if user is authenticated
  if (!isAuthenticated.value) {
    return navigateTo('/login')
  }

  // Check role-based access
  if (to.path.startsWith('/admin') && role !== 'admin') {
    return navigateTo('/')
  }

  if (to.path.startsWith('/viewer') && role !== 'admin' && role !== 'viewer') {
    return navigateTo('/')
  }
})
