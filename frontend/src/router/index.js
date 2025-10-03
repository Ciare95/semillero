import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('../views/Home.vue')
  },
  {
    path: '/productos',
    name: 'Productos',
    component: () => import('../views/Productos/Productos.vue')
  },
  {
    path: '/usuarios',
    name: 'Usuarios',
    component: () => import('../views/Usuarios/Usuarios.vue')
  },
  {
    path: '/ventas',
    name: 'Ventas',
    component: () => import('../views/Ventas/Ventas.vue')
  },
  {
    path: '/compras',
    name: 'Compras',
    component: () => import('../views/Compras/Compras.vue')
  },
  {
    path: '/inventario',
    name: 'Inventario',
    component: () => import('../views/Inventario/Inventario.vue')
  },
  {
    path: '/reportes',
    name: 'Reportes',
    component: () => import('../views/Reportes/Reportes.vue')
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

export default router