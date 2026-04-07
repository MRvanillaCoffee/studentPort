import { defineNuxtRouteMiddleware, navigateTo } from 'nuxt/app'
import { useAuth } from '../composables/useAuth'

export default defineNuxtRouteMiddleware((to) => {
  const { user, isAuthenticated } = useAuth()

  // Allow public pages without authentication
  if (to.path === '/' || to.path === '/login' || to.path === '/register') {
    if (isAuthenticated.value && (to.path === '/login' || to.path === '/register')) {
      return navigateTo('/')
    }
    return
  }

  // Check if user is authenticated
  if (!isAuthenticated.value) {
    return navigateTo('/login')
  }

  // Check role-based access
  const role = user.value?.role

  if (to.path.startsWith('/admin') && role !== 'admin') {
    return navigateTo('/')
  }

  if (to.path.startsWith('/viewer') && role !== 'admin' && role !== 'viewer') {
    return navigateTo('/')
  }
})
