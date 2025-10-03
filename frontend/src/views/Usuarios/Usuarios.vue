<template>
  <div class="space-y-8">
    <!-- Header -->
    <section class="card">
      <div class="flex items-start justify-between gap-4">
        <div>
          <h1 class="text-2xl font-semibold tracking-tight text-slate-900">
            Gestión de Usuarios
          </h1>
          <p class="mt-2 text-slate-600">
            Administra usuarios y clientes desde un solo lugar.
          </p>
        </div>
      </div>
    </section>

    <!-- Tabs Navigation -->
    <div class="border-b border-slate-200 mt-4 mb-6 pt-3 pb-3">
      <nav class="flex flex-wrap gap-x-10 gap-y-2">
        <button
          @click="activeTab = 'usuarios'"
          :class="[
            'whitespace-nowrap border-b-2 px-3 pt-2 pb-3 text-sm font-medium transition-colors',
            activeTab === 'usuarios'
              ? 'border-sky-500 text-sky-600'
              : 'border-transparent text-slate-500 hover:border-slate-300 hover:text-slate-700'
          ]"
        >
          Usuarios
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
      </nav>
    </div>

    <!-- Usuarios -->
    <div v-if="activeTab === 'usuarios'" class="space-y-6">
      <!-- Header with Actions -->
      <div class="flex items-center justify-between">
        <h2 class="text-xl font-semibold text-slate-900">Usuarios</h2>
        <button 
          @click="showForm = 'usuarios'" 
          class="btn btn-primary flex items-center gap-2"
        >
          <span>+</span>
          Agregar Usuario
        </button>
      </div>

      <!-- Users Table -->
      <div class="card overflow-hidden">
        <div class="overflow-x-auto">
          <table class="min-w-full divide-y divide-slate-200">
            <thead class="bg-slate-50">
              <tr>
                <th class="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">ID</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">Nombre</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">Email</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">Acciones</th>
              </tr>
            </thead>
            <tbody class="bg-white divide-y divide-slate-200">
              <tr v-for="usuario in usuarios" :key="usuario.id" class="hover:bg-slate-50 transition-colors">
                <td class="px-6 py-4 whitespace-nowrap text-sm text-slate-900">{{ usuario.id }}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-slate-900">{{ usuario.nombre }}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-slate-900">{{ usuario.email }}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm font-medium">
                  <div class="flex items-center gap-2">
                    <button 
                      @click="editarUsuario(usuario)" 
                      class="text-sky-600 hover:text-sky-800 transition-colors"
                    >
                      Editar
                    </button>
                    <span class="text-slate-300">|</span>
                    <button 
                      @click="eliminarUsuario(usuario.id)" 
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

    <!-- Clientes -->
    <div v-if="activeTab === 'clientes'" class="space-y-6">
      <!-- Header with Actions -->
      <div class="flex items-center justify-between">
        <h2 class="text-xl font-semibold text-slate-900">Clientes</h2>
        <button 
          @click="showForm = 'clientes'" 
          class="btn btn-primary flex items-center gap-2"
        >
          <span>+</span>
          Agregar Cliente
        </button>
      </div>

      <!-- Clients Table -->
      <div class="card overflow-hidden">
        <div class="overflow-x-auto">
          <table class="min-w-full divide-y divide-slate-200">
            <thead class="bg-slate-50">
              <tr>
                <th class="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">ID</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">Nombre</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">Email</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">Teléfono</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">Acciones</th>
              </tr>
            </thead>
            <tbody class="bg-white divide-y divide-slate-200">
              <tr v-for="cliente in clientes" :key="cliente.id" class="hover:bg-slate-50 transition-colors">
                <td class="px-6 py-4 whitespace-nowrap text-sm text-slate-900">{{ cliente.id }}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-slate-900">{{ cliente.nombre }}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-slate-900">{{ cliente.email }}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-slate-900">{{ cliente.telefono }}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm font-medium">
                  <div class="flex items-center gap-2">
                    <button 
                      @click="editarCliente(cliente)" 
                      class="text-sky-600 hover:text-sky-800 transition-colors"
                    >
                      Editar
                    </button>
                    <span class="text-slate-300">|</span>
                    <button 
                      @click="eliminarCliente(cliente.id)" 
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
            {{ showForm === 'usuarios' 
              ? (editing ? 'Editar Usuario' : 'Agregar Usuario') 
              : (editing ? 'Editar Cliente' : 'Agregar Cliente') }}
          </h3>
        </div>
        <form @submit.prevent="submitForm" class="p-6 space-y-4">
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
            <label class="block text-sm font-medium text-slate-700 mb-1">Email</label>
            <input 
              v-model="formData.email" 
              placeholder="Email" 
              type="email" 
              required
              class="w-full px-3 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-500 focus:border-sky-500 transition-colors"
            >
          </div>

          <div v-if="showForm === 'clientes'">
            <label class="block text-sm font-medium text-slate-700 mb-1">Teléfono</label>
            <input 
              v-model="formData.telefono" 
              placeholder="Teléfono"
              class="w-full px-3 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-500 focus:border-sky-500 transition-colors"
            >
          </div>

          <div v-if="showForm === 'usuarios'">
            <label class="block text-sm font-medium text-slate-700 mb-1">Contraseña</label>
            <input 
              v-model="formData.password" 
              placeholder="Contraseña" 
              type="password" 
              required
              class="w-full px-3 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-500 focus:border-sky-500 transition-colors"
            >
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
  name: 'Usuarios',
  data() {
    return {
      activeTab: 'usuarios',
      usuarios: [],
      clientes: [],
      showForm: null,
      formData: {
        nombre: '',
        email: '',
        telefono: '',
        password: ''
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
        this.obtenerUsuarios(),
        this.obtenerClientes()
      ])
    },
    async obtenerUsuarios() {
      try {
        const response = await api.get('usuarios')
        this.usuarios = response.data
      } catch (error) {
        console.error('Error obteniendo usuarios:', error)
      }
    },
    async obtenerClientes() {
      try {
        const response = await api.get('clientes')
        this.clientes = response.data
      } catch (error) {
        console.error('Error obteniendo clientes:', error)
      }
    },
    editarUsuario(usuario) {
      this.editing = usuario
      this.formData = { ...usuario }
      this.showForm = 'usuarios'
    },
    editarCliente(cliente) {
      this.editing = cliente
      this.formData = { ...cliente }
      this.showForm = 'clientes'
    },
    async submitForm() {
      try {
        if (this.editing) {
          if (this.showForm === 'usuarios') {
            await api.put(`actualizar_usuario/${this.editing.id}`, this.formData)
          } else {
            await api.put(`actualizar_cliente/${this.editing.id}`, this.formData)
          }
        } else {
          if (this.showForm === 'usuarios') {
            await api.post('crear_usuario', this.formData)
          } else {
            await api.post('crear_cliente', this.formData)
          }
        }
        this.showForm = null
        this.formData = { nombre: '', email: '', telefono: '', password: '' }
        this.editing = null
        this.loadData()
      } catch (error) {
        console.error('Error guardando:', error)
      }
    },
    async eliminarUsuario(id) {
      if (confirm('¿Eliminar usuario?')) {
        try {
          await api.delete(`eliminar_usuario/${id}`)
          this.loadData()
        } catch (error) {
          console.error('Error eliminando:', error)
        }
      }
    },
    async eliminarCliente(id) {
      if (confirm('¿Eliminar cliente?')) {
        try {
          await api.delete(`eliminar_cliente/${id}`)
          this.loadData()
        } catch (error) {
          console.error('Error eliminando:', error)
        }
      }
    }
  }
}
</script>
