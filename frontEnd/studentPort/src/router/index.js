import { createRouter, createWebHistory } from "vue-router"

import Home from "../pages/Home.vue"
import Login from "../pages/Login.vue"
import Score from "../pages/Score.vue"

const routes = [
  { path: "/", component: Home },
  { path: "/login", component: Login },
  { path: "/score", component: Score }
]

export default createRouter({
  history: createWebHistory(),
  routes
})