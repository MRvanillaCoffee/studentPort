import { createRouter, createWebHistory } from "vue-router"

import Home from "../pages/Home.vue"
import Login from "../pages/Login.vue"
import Score from "../pages/Score.vue"

const routes = [
  { path: "/", component: Home },
  { path: "/login", component: Login },
  {
    path: "/score",
    component: Score,
    meta: { requiresAuth: true }
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

router.beforeEach((to, _from, next) => {
  const user = JSON.parse(localStorage.getItem("user") || "null")

  if (to.meta.requiresAuth && !user) {
    next("/login")
    return
  }

  next()
})

export default router