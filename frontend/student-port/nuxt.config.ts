// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  devtools: { enabled: true },
  
  // API Configuration
  runtimeConfig: {
    public: {
      apiBase: import.meta.env.NUXT_PUBLIC_API_BASE || 'http://localhost:8000'
    }
  },

  // CSS
  css: [],

  // Auto imports
  imports: {
    autoImport: true
  }
})
