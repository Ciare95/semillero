<template>
  <div class="space-y-8">
    <!-- Header -->
    <section class="card">
      <div class="flex items-start justify-between gap-4">
        <div>
          <h1 class="text-2xl font-semibold tracking-tight text-slate-900">
            Gestión de Compras
          </h1>
          <p class="mt-2 text-slate-600">
            Administra proveedores, facturas de compra y gastos desde un solo lugar.
          </p>
        </div>
      </div>
    </section>

    <!-- Tabs Navigation -->
    <div class="border-b border-slate-200 mt-4 mb-6 pt-3 pb-3">
      <nav class="flex flex-wrap gap-x-10 gap-y-2">
        <button
          @click="activeTab = 'proveedores'"
          :class="[
            'whitespace-nowrap border-b-2 px-3 pt-2 pb-3 text-sm font-medium transition-colors',
            activeTab === 'proveedores'
              ? 'border-sky-500 text-sky-600'
              : 'border-transparent text-slate-500 hover:border-slate-300 hover:text-slate-700'
          ]"
        >
          Proveedores
        </button>
        <button
          @click="activeTab = 'facturas'"
          :class="[
            'whitespace-nowrap border-b-2 px-3 pt-2 pb-3 text-sm font-medium transition-colors',
            activeTab === 'facturas'
              ? 'border-sky-500 text-sky-600'
              : 'border-transparent text-slate-500 hover:border-slate-300 hover:text-slate-700'
          ]"
        >
          Facturas Compra
        </button>
        <button
          @click="activeTab = 'gastos'"
          :class="[
            'whitespace-nowrap border-b-2 px-3 pt-2 pb-3 text-sm font-medium transition-colors',
            activeTab === 'gastos'
              ? 'border-sky-500 text-sky-600'
              : 'border-transparent text-slate-500 hover:border-slate-300 hover:text-slate-700'
          ]"
        >
          Gastos
        </button>
      </nav>
    </div>

    <!-- Proveedores -->
    <div v-if="activeTab === 'proveedores'" class="space-y-6">
      <!-- Header with Actions -->
      <div class="flex items-center justify-between">
        <h2 class="text-xl font-semibold text-slate-900">Proveedores</h2>
        <button 
          @click="showForm = 'proveedores'" 
          class="btn btn-primary flex items-center gap-2"
        >
          <span>+</span>
          Agregar Proveedor
        </button>
      </div>

      <!-- Providers Table -->
      <div class="card overflow-hidden">
        <div class="overflow-x-auto">
          <table class="min-w-full divide-y divide-slate-200">
            <thead class="bg-slate-50">
              <tr>
                <th class="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">ID</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">Nombre</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">Contacto</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">Acciones</th>
              </tr>
            </thead>
            <tbody class="bg-white divide-y divide-slate-200">
              <tr v-for="prov in proveedores" :key="prov.id" class="hover:bg-slate-50 transition-colors">
                <td class="px-6 py-4 whitespace-nowrap text-sm text-slate-900">{{ prov.id }}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-slate-900">{{ prov.nombre }}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-slate-900">{{ prov.contacto }}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm font-medium">
                  <div class="flex items-center gap-2">
                    <button 
                      @click="editarProveedor(prov)" 
                      class="text-sky-600 hover:text-sky-800 transition-colors"
                    >
                      Editar
                    </button>
                    <span class="text-slate-300">|</span>
                    <button 
                      @click="eliminarProveedor(prov.id)" 
                      class="text-rose-600 hover:text-rose-800 transition-colors"
                    >
                      Eliminar
                    </button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- Facturas Compra -->
    <div v-if="activeTab === 'facturas'" class="space-y-6">
      <!-- Header with Actions -->
      <div class="flex items-center justify-between">
        <h2 class="text-xl font-semibold text-slate-900">Facturas Compra</h2>
        <button 
          @click="showForm = 'facturas'" 
          class="btn btn-primary flex items-center gap-2"
        >
          <span>+</span>
          Agregar Factura
        </button>
      </div>

      <!-- Invoices Table -->
      <div class="card overflow-hidden">
        <div class="overflow-x-auto">
          <table class="min-w-full divide-y divide-slate-200">
            <thead class="bg-slate-50">
              <tr>
                <th class="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">ID</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">Proveedor</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">Total</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">Acciones</th>
              </tr>
            </thead>
            <tbody class="bg-white divide-y divide-slate-200">
              <tr v-for="fact in facturasCompra" :key="fact.id" class="hover:bg-slate-50 transition-colors">
                <td class="px-6 py-4 whitespace-nowrap text-sm text-slate-900">{{ fact.id }}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-slate-900">{{ fact.proveedor }}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-slate-900">{{ fact.total }}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm font-medium">
                  <div class="flex items-center gap-2">
                    <button 
                      @click="editarFacturaCompra(fact)" 
                      class="text-sky-600 hover:text-sky-800 transition-colors"
                    >
                      Editar
                    </button>
                    <span class="text-slate-300">|</span>
                    <button 
                      @click="eliminarFacturaCompra(fact.id)" 
                      class="text-rose-600 hover:text-rose-800 transition-colors"
                    >
                      Eliminar
                    </button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- Gastos -->
    <div v-if="activeTab === 'gastos'" class="space-y-6">
      <!-- Header with Actions -->
      <div class="flex items-center justify-between">
        <h2 class="text-xl font-semibold text-slate-900">Gastos</h2>
        <button 
          @click="showForm = 'gastos'" 
          class="btn btn-primary flex items-center gap-2"
        >
          <span>+</span>
          Agregar Gasto
        </button>
      </div>

      <!-- Expenses Table -->
      <div class="card overflow-hidden">
        <div class="overflow-x-auto">
          <table class="min-w-full divide-y divide-slate-200">
            <thead class="bg-slate-50">
              <tr>
                <th class="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">ID</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">Descripción</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">Monto</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">Acciones</th>
              </tr>
            </thead>
            <tbody class="bg-white divide-y divide-slate-200">
              <tr v-for="gasto in gastos" :key="gasto.id" class="hover:bg-slate-50 transition-colors">
                <td class="px-6 py-4 whitespace-nowrap text-sm text-slate-900">{{ gasto.id }}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-slate-900">{{ gasto.descripcion }}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-slate-900">{{ gasto.monto }}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm font-medium">
                  <div class="flex items-center gap-2">
                    <button 
                      @click="editarGasto(gasto)" 
                      class="text-sky-600 hover:text-sky-800 transition-colors"
                    >
                      Editar
                    </button>
                    <span class="text-slate-300">|</span>
                    <button 
                      @click="eliminarGasto(gasto.id)" 
                      class="text-rose-600 hover:text-rose-800 transition-colors"
                    >
                      Eliminar
                    </button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- Form Modal -->
    <div v-if="showForm" class="fixed inset-0 bg-slate-900/50 backdrop-blur-sm flex items-center justify-center p-4 z-50">
      <div class="bg-white rounded-xl shadow-xl max-w-md w-full max-h-[90vh] overflow-y-auto">
        <div class="p-6 border-b border-slate-200">
          <h3 class="text-lg font-semibold text-slate-900">
            {{ showForm === 'proveedores' ? (editing ? 'Editar Proveedor' : 'Agregar Proveedor') : 
               showForm === 'facturas' ? (editing ? 'Editar Factura' : 'Agregar Factura') : 
               (editing ? 'Editar Gasto' : 'Agregar Gasto') }}
          </h3>
        </div>
        <form @submit.prevent="submitForm" class="p-6 space-y-4">
          <!-- Proveedores -->
          <div v-if="showForm === 'proveedores'" class="space-y-4">
            <div>
              <label class="block text-sm font-medium text-slate-700 mb-1">Nombre</label>
              <input 
                v-model="formData.nombre" 
                placeholder="Nombre" 
                required
                class="w-full px-3 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-500 focus:border-sky-500 transition-colors"
              >
            </div>
            <div>
              <label class="block text-sm font-medium text-slate-700 mb-1">Contacto</label>
              <input 
                v-model="formData.contacto" 
                placeholder="Contacto" 
                required
                class="w-full px-3 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-500 focus:border-sky-500 transition-colors"
              >
            </div>
          </div>

          <!-- Facturas -->
          <div v-if="showForm === 'facturas'" class="space-y-4">
            <div>
              <label class="block text-sm font-medium text-slate-700 mb-1">Proveedor ID</label>
              <input 
                v-model="formData.proveedor" 
                placeholder="ID del proveedor" 
                required
                class="w-full px-3 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-500 focus:border-sky-500 transition-colors"
              >
            </div>
            <div>
              <label class="block text-sm font-medium text-slate-700 mb-1">Total</label>
              <input 
                v-model="formData.total" 
                placeholder="0.00" 
                type="number" 
                step="0.01" 
                required
                class="w-full px-3 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-500 focus:border-sky-500 transition-colors"
              >
            </div>
          </div>

          <!-- Gastos -->
          <div v-if="showForm === 'gastos'" class="space-y-4">
            <div>
              <label class="block text-sm font-medium text-slate-700 mb-1">Descripción</label>
              <input 
                v-model="formData.descripcion" 
                placeholder="Descripción" 
                required
                class="w-full px-3 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-500 focus:border-sky-500 transition-colors"
              >
            </div>
            <div>
              <label class="block text-sm font-medium text-slate-700 mb-1">Monto</label>
              <input 
                v-model="formData.monto" 
                placeholder="0.00" 
                type="number" 
                step="0.01" 
                required
                class="w-full px-3 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-500 focus:border-sky-500 transition-colors"
              >
            </div>
          </div>

          <div class="flex gap-3 pt-4">
            <button 
              type="submit" 
              class="btn btn-primary flex-1"
            >
              {{ editing ? 'Actualizar' : 'Guardar' }}
            </button>
            <button 
              type="button" 
              @click="showForm = null" 
              class="btn btn-ghost flex-1"
            >
              Cancelar
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import api from '../../services/api.js'

export default {
  name: 'Compras',
  data() {
    return {
      activeTab: 'proveedores',
      proveedores: [],
      facturasCompra: [],
      gastos: [],
      showForm: null,
      formData: {
        nombre: '',
        contacto: '',
        proveedor: '',
        total: '',
        descripcion: '',
        monto: ''
      },
      editing: null
    }
  },
  mounted() {
    this.loadData()
  },
  methods: {
    async loadData() {
      await Promise.all([
        this.obtenerProveedores(),
        this.obtenerFacturasCompra(),
        this.obtenerGastos()
      ])
    },
    async obtenerProveedores() {
      try {
        const response = await api.get('proveedores')
        this.proveedores = response.data
      } catch (error) {
        console.error('Error obteniendo proveedores:', error)
      }
    },
    async obtenerFacturasCompra() {
      try {
        const response = await api.get('facturas_compra')
        this.facturasCompra = response.data
      } catch (error) {
        console.error('Error obteniendo facturas:', error)
      }
    },
    async obtenerGastos() {
      try {
        const response = await api.get('gastos')
        this.gastos = response.data
      } catch (error) {
        console.error('Error obteniendo gastos:', error)
      }
    },
    editarProveedor(prov) {
      this.editing = prov
      this.formData = { ...prov }
      this.showForm = 'proveedores'
    },
    editarFacturaCompra(fact) {
      this.editing = fact
      this.formData = { ...fact }
      this.showForm = 'facturas'
    },
    editarGasto(gasto) {
      this.editing = gasto
      this.formData = { ...gasto }
      this.showForm = 'gastos'
    },
    async submitForm() {
      try {
        if (this.editing) {
          if (this.showForm === 'proveedores') {
            await api.put(`actualizar_proveedor/${this.editing.id}`, this.formData)
          } else if (this.showForm === 'facturas') {
            await api.put(`actualizar_factura_compra/${this.editing.id}`, this.formData)
          } else {
            await api.put(`actualizar_gasto/${this.editing.id}`, this.formData)
          }
        } else {
          if (this.showForm === 'proveedores') {
            await api.post('crear_proveedor', this.formData)
          } else if (this.showForm === 'facturas') {
            await api.post('crear_factura_compra', this.formData)
          } else {
            await api.post('crear_gasto', this.formData)
          }
        }
        this.showForm = null
        this.formData = { nombre: '', contacto: '', proveedor: '', total: '', descripcion: '', monto: '' }
        this.editing = null
        this.loadData()
      } catch (error) {
        console.error('Error guardando:', error)
      }
    },
    async eliminarProveedor(id) {
      if (confirm('¿Eliminar proveedor?')) {
        try {
          await api.delete(`eliminar_proveedor/${id}`)
          this.loadData()
        } catch (error) {
          console.error('Error eliminando:', error)
        }
      }
    },
    async eliminarFacturaCompra(id) {
      if (confirm('¿Eliminar factura?')) {
        try {
          await api.delete(`eliminar_factura_compra/${id}`)
          this.loadData()
        } catch (error) {
          console.error('Error eliminando:', error)
        }
      }
    },
    async eliminarGasto(id) {
      if (confirm('¿Eliminar gasto?')) {
        try {
          await api.delete(`eliminar_gasto/${id}`)
          this.loadData()
        } catch (error) {
          console.error('Error eliminando:', error)
        }
      }
    }
  }
}
</script>
