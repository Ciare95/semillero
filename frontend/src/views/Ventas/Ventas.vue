<template>
  <div class="space-y-8">
    <!-- Header -->
    <section class="card">
      <div class="flex items-start justify-between gap-4">
        <div>
          <h1 class="text-2xl font-semibold tracking-tight text-slate-900">
            Gestión de Ventas
          </h1>
          <p class="mt-2 text-slate-600">
            Crea nuevas ventas, revisa el historial y gestiona acciones rápidas desde un solo lugar.
          </p>
        </div>
      </div>
    </section>

    <!-- Tabs Navigation -->
    <div class="border-b border-slate-200 mt-4 mb-6 pt-3 pb-3">
      <nav class="flex flex-wrap gap-x-10 gap-y-2">
        <button
          @click="activeTab = 'ventas'"
          :class="[
            'whitespace-nowrap border-b-2 px-3 pt-2 pb-3 text-sm font-medium transition-colors',
            activeTab === 'ventas'
              ? 'border-sky-500 text-sky-600'
              : 'border-transparent text-slate-500 hover:border-slate-300 hover:text-slate-700'
          ]"
        >
          Listar Ventas
        </button>
        <button
          @click="activeTab = 'crear'"
          :class="[
            'whitespace-nowrap border-b-2 px-3 pt-2 pb-3 text-sm font-medium transition-colors',
            activeTab === 'crear'
              ? 'border-sky-500 text-sky-600'
              : 'border-transparent text-slate-500 hover:border-slate-300 hover:text-slate-700'
          ]"
        >
          Crear Venta
        </button>
      </nav>
    </div>

    <!-- Listado de Ventas -->
    <div v-if="activeTab === 'ventas'" class="space-y-6">
      <!-- Header with Actions -->
      <div class="flex items-center justify-between">
        <h2 class="text-xl font-semibold text-slate-900">Lista de Ventas</h2>
        <button 
          @click="activeTab = 'crear'" 
          class="btn btn-primary flex items-center gap-2"
        >
          <span>+</span>
          Crear Venta
        </button>
      </div>

      <!-- Sales Table -->
      <div class="card overflow-hidden">
        <div class="overflow-x-auto">
          <table class="min-w-full divide-y divide-slate-200">
            <thead class="bg-slate-50">
              <tr>
                <th class="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">ID</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">Fecha</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">Total</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">Acciones</th>
              </tr>
            </thead>
            <tbody class="bg-white divide-y divide-slate-200">
              <tr v-for="venta in ventas" :key="venta.id" class="hover:bg-slate-50 transition-colors">
                <td class="px-6 py-4 whitespace-nowrap text-sm text-slate-900">{{ venta.id }}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-slate-900">{{ venta.fecha }}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-slate-900">{{ venta.total }}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm font-medium">
                  <div class="flex items-center gap-2">
                    <button 
                      @click="verVenta(venta.id)" 
                      class="text-sky-600 hover:text-sky-800 transition-colors"
                    >
                      Ver
                    </button>
                    <span class="text-slate-300">|</span>
                    <button 
                      @click="anularVenta(venta.id)" 
                      class="text-rose-600 hover:text-rose-800 transition-colors"
                    >
                      Anular
                    </button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- Crear Venta (pestaña) -->
    <div v-if="activeTab === 'crear'" class="space-y-6">
      <!-- Header with Actions -->
      <div class="flex items-center justify-between">
        <h2 class="text-xl font-semibold text-slate-900">Crear Venta</h2>
        <button 
          @click="activeTab = 'ventas'" 
          class="btn btn-ghost"
        >
          Volver al Listado
        </button>
      </div>

      <!-- Form Card -->
      <div class="card">
        <form @submit.prevent="crearVenta" class="space-y-4">
          <!-- Placeholder para items de venta (a completar más adelante) -->
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div>
              <label class="block text-sm font-medium text-slate-700 mb-1">Cliente</label>
              <input
                placeholder="Nombre del cliente (opcional)"
                class="w-full px-3 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-500 focus:border-sky-500 transition-colors"
              />
            </div>
            <div>
              <label class="block text-sm font-medium text-slate-700 mb-1">Fecha</label>
              <input
                type="date"
                class="w-full px-3 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-500 focus:border-sky-500 transition-colors"
              />
            </div>
          </div>

          <div>
            <label class="block text-sm font-medium text-slate-700 mb-1">Notas</label>
            <textarea
              placeholder="Agregar detalles o notas de la venta (opcional)"
              class="w-full px-3 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-500 focus:border-sky-500 transition-colors min-h-[96px]"
            ></textarea>
          </div>

          <p class="text-sm text-slate-600">
            Próximamente: formulario para agregar productos, cantidades y precios.
          </p>

          <div class="flex gap-3 pt-2">
            <button type="submit" class="btn btn-primary flex-1">Crear</button>
            <button type="button" @click="activeTab = 'ventas'" class="btn btn-ghost flex-1">Cancelar</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import api from '../../services/api.js'

export default {
  name: 'Ventas',
  data() {
    return {
      ventas: [],
      activeTab: 'ventas'
    }
  },
  mounted() {
    this.listarVentas()
  },
  methods: {
    async listarVentas() {
      try {
        const response = await api.get('listar_ventas/')
        this.ventas = response.data
      } catch (error) {
        console.error('Error listando ventas:', error)
      }
    },
    async verVenta(id) {
      try {
        const response = await api.get(`obtener_venta/${id}/`)
        alert('Detalles: ' + JSON.stringify(response.data))
      } catch (error) {
        console.error('Error obteniendo venta:', error)
      }
    },
    async crearVenta() {
      // Implementar datos reales del formulario cuando se agreguen los items
      try {
        await api.post('crear_venta/', {})
        this.activeTab = 'ventas'
        this.listarVentas()
      } catch (error) {
        console.error('Error creando venta:', error)
      }
    },
    async anularVenta(id) {
      if (confirm('¿Anular venta?')) {
        try {
          await api.get(`anular_venta/${id}/`)
          this.listarVentas()
        } catch (error) {
          console.error('Error anulando venta:', error)
        }
      }
    }
  }
}
</script>
