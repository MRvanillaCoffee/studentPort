import { computed, readonly } from 'vue'
import { useRuntimeConfig, useState } from 'nuxt/app'
import { $fetch } from 'ofetch'

type UserRole = 'admin' | 'viewer'

type AuthUser = {
  id: number
  username: string
  email: string
  role: UserRole
  created_at: string
}

type LoginResponse = {
  access_token: string
  token_type: string
  user: AuthUser
}

export const useAuth = () => {
  const runtimeConfig = useRuntimeConfig()
  const apiBase = runtimeConfig.public.apiBase

  const user = useState<AuthUser | null>('user', () => null)
  const token = useState<string | null>('token', () => null)
  const isAuthenticated = computed(() => !!token.value)

  // Load token from localStorage on mount
  const loadAuth = () => {
    if (typeof window !== 'undefined') {
      const stored = localStorage.getItem('auth_token')
      const storedUser = localStorage.getItem('auth_user')
      if (stored && storedUser) {
        token.value = stored
        user.value = JSON.parse(storedUser) as AuthUser
      }
    }
  }

  const login = async (username: string, password: string) => {
    try {
      const response = await $fetch<LoginResponse>(`${apiBase}/api/login`, {
        method: 'POST',
        body: {
          username,
          password
        }
      })
      
      token.value = response.access_token
      user.value = response.user
      
      if (typeof window !== 'undefined') {
        localStorage.setItem('auth_token', response.access_token)
        localStorage.setItem('auth_user', JSON.stringify(response.user))
      }
      
      return { success: true, user: response.user }
    } catch (error: any) {
      return { success: false, error: error.data?.detail || 'Login failed' }
    }
  }

  const logout = () => {
    token.value = null
    user.value = null
    if (typeof window !== 'undefined') {
      localStorage.removeItem('auth_token')
      localStorage.removeItem('auth_user')
    }
  }

  return {
    user: readonly(user),
    token: readonly(token),
    isAuthenticated,
    login,
    logout,
    loadAuth,
    apiBase
  }
}

