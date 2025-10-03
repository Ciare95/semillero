<template>
  <div class="space-y-8">
    <!-- Header -->
    <section class="card">
      <div class="flex items-start justify-between gap-4">
        <div>
          <h1 class="text-2xl font-semibold tracking-tight text-slate-900">
            Gestión de Reportes
          </h1>
          <p class="mt-2 text-slate-600">
            Genera y consulta reportes del sistema desde un solo lugar.
          </p>
        </div>
      </div>
    </section>

    <!-- Tabs Navigation -->
    <div class="border-b border-slate-200 mt-4 mb-6 pt-3 pb-3">
      <nav class="flex flex-wrap gap-x-10 gap-y-2">
        <button
          @click="activeTab = 'general'"
          :class="[
            'whitespace-nowrap border-b-2 px-3 pt-2 pb-3 text-sm font-medium transition-colors',
            activeTab === 'general'
              ? 'border-sky-500 text-sky-600'
              : 'border-transparent text-slate-500 hover:border-slate-300 hover:text-slate-700'
          ]"
        >
          Generales
        </button>
        <button
          @click="activeTab = 'ventas'"
          :class="[
            'whitespace-nowrap border-b-2 px-3 pt-2 pb-3 text-sm font-medium transition-colors',
            activeTab === 'ventas'
              ? 'border-sky-500 text-sky-600'
              : 'border-transparent text-slate-500 hover:border-slate-300 hover:text-slate-700'
          ]"
        >
          Ventas
        </button>
        <button
          @click="activeTab = 'productos'"
          :class="[
            'whitespace-nowrap border-b-2 px-3 pt-2 pb-3 text-sm font-medium transition-colors',
            activeTab === 'productos'
              ? 'border-sky-500 text-sky-600'
              : 'border-transparent text-slate-500 hover:border-slate-300 hover:text-slate-700'
          ]"
        >
          Productos
        </button>
        <button
          @click="activeTab = 'clientes'"
          :class="[
            'whitespace-nowrap border-b-2 px-3 pt-2 pb-3 text-sm font-medium transition-colors',
            activeTab === 'clientes'
              ? 'border-sky-500 text-sky-600'
              : 'border-transparent text-slate-500 hover:border-slate-300 hover:text-slate-700'
          ]"
        >
          Clientes
        </button>
        <button
          @click="activeTab = 'ingresos'"
          :class="[
            'whitespace-nowrap border-b-2 px-3 pt-2 pb-3 text-sm font-medium transition-colors',
            activeTab === 'ingresos'
              ? 'border-sky-500 text-sky-600'
              : 'border-transparent text-slate-500 hover:border-slate-300 hover:text-slate-700'
          ]"
        >
          Ingresos y Gastos
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
          Crear Reporte
        </button>
      </nav>
    </div>

    <!-- Generales -->
    <div v-if="activeTab === 'general'" class="space-y-6">
      <div class="flex items-center justify-between">
        <h2 class="text-xl font-semibold text-slate-900">Reportes Generales</h2>
        <button @click="obtenerReportes" class="btn btn-primary flex items-center gap-2">
          <span>↻</span>
          Obtener Reportes
        </button>
      </div>

      <div v-if="reportData" class="card overflow-auto">
        <h3 class="text-sm font-medium text-slate-700 mb-2">Resultado</h3>
        <pre class="text-xs bg-slate-50 rounded-lg p-4 overflow-x-auto">{{ JSON.stringify(reportData, null, 2) }}</pre>
      </div>
    </div>

    <!-- Ventas -->
    <div v-if="activeTab === 'ventas'" class="space-y-6">
      <div class="flex items-center justify-between">
        <h2 class="text-xl font-semibold text-slate-900">Reporte de Ventas</h2>
        <button @click="reporteVentas" class="btn btn-primary flex items-center gap-2">
          <span>📈</span>
          Generar Reporte
        </button>
      </div>

      <div v-if="reportData" class="card overflow-auto">
        <h3 class="text-sm font-medium text-slate-700 mb-2">Resultado</h3>
        <pre class="text-xs bg-slate-50 rounded-lg p-4 overflow-x-auto">{{ JSON.stringify(reportData, null, 2) }}</pre>
      </div>
    </div>

    <!-- Productos -->
    <div v-if="activeTab === 'productos'" class="space-y-6">
      <div class="flex items-center justify-between">
        <h2 class="text-xl font-semibold text-slate-900">Reporte de Productos</h2>
        <button @click="reporteProductos" class="btn btn-primary flex items-center gap-2">
          <span>📦</span>
          Generar Reporte
        </button>
      </div>

      <div v-if="reportData" class="card overflow-auto">
        <h3 class="text-sm font-medium text-slate-700 mb-2">Resultado</h3>
        <pre class="text-xs bg-slate-50 rounded-lg p-4 overflow-x-auto">{{ JSON.stringify(reportData, null, 2) }}</pre>
      </div>
    </div>

    <!-- Clientes -->
    <div v-if="activeTab === 'clientes'" class="space-y-6">
      <div class="flex items-center justify-between">
        <h2 class="text-xl font-semibold text-slate-900">Reporte de Clientes</h2>
        <button @click="reporteClientes" class="btn btn-primary flex items-center gap-2">
          <span>👥</span>
          Generar Reporte
        </button>
      </div>

      <div v-if="reportData" class="card overflow-auto">
        <h3 class="text-sm font-medium text-slate-700 mb-2">Resultado</h3>
        <pre class="text-xs bg-slate-50 rounded-lg p-4 overflow-x-auto">{{ JSON.stringify(reportData, null, 2) }}</pre>
      </div>
    </div>

    <!-- Ingresos y Gastos -->
    <div v-if="activeTab === 'ingresos'" class="space-y-6">
      <div class="flex items-center justify-between">
        <h2 class="text-xl font-semibold text-slate-900">Ingresos y Gastos</h2>
        <button @click="ingresosGastos" class="btn btn-primary flex items-center gap-2">
          <span>💰</span>
          Generar Reporte
        </button>
      </div>

      <div v-if="reportData" class="card overflow-auto">
        <h3 class="text-sm font-medium text-slate-700 mb-2">Resultado</h3>
        <pre class="text-xs bg-slate-50 rounded-lg p-4 overflow-x-auto">{{ JSON.stringify(reportData, null, 2) }}</pre>
      </div>
    </div>

    <!-- Crear Reporte -->
    <div v-if="activeTab === 'crear'" class="space-y-6">
      <div class="flex items-center justify-between">
        <h2 class="text-xl font-semibold text-slate-900">Crear Reporte</h2>
        <button @click="crearReporte" class="btn btn-primary flex items-center gap-2">
          <span>＋</span>
          Crear Reporte
        </button>
      </div>

      <div v-if="reportData" class="card overflow-auto">
        <h3 class="text-sm font-medium text-slate-700 mb-2">Resultado</h3>
        <pre class="text-xs bg-slate-50 rounded-lg p-4 overflow-x-auto">{{ JSON.stringify(reportData, null, 2) }}</pre>
      </div>
    </div>
  </div>
</template>

<script>
import api from '../../services/api.js'

export default {
  name: 'Reportes',
  data() {
    return {
      activeTab: 'general',
      reportData: null
    }
  },
  methods: {
    async obtenerReportes() {
      try {
        const response = await api.get('reportes')
        this.reportData = response.data
      } catch (error) {
        console.error('Error obteniendo reportes:', error)
      }
    },
    async crearReporte() {
      try {
        const response = await api.post('crear_reporte', {})
        this.reportData = response.data
      } catch (error) {
        console.error('Error creando reporte:', error)
      }
    },
    async reporteVentas() {
      try {
        const response = await api.get('reporte_ventas')
        this.reportData = response.data
      } catch (error) {
        console.error('Error reporte ventas:', error)
      }
    },
    async reporteProductos() {
      try {
        const response = await api.get('reporte_productos')
        this.reportData = response.data
      } catch (error) {
        console.error('Error reporte productos:', error)
      }
    },
    async reporteClientes() {
      try {
        const response = await api.get('reporte_clientes')
        this.reportData = response.data
      } catch (error) {
        console.error('Error reporte clientes:', error)
      }
    },
    async ingresosGastos() {
      try {
        const response = await api.get('ingresos_gastos')
        this.reportData = response.data
      } catch (error) {
        console.error('Error ingresos gastos:', error)
      }
    }
  }
}
</script>
