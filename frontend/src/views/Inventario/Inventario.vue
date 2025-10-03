<template>
  <div class="space-y-8">
    <!-- Header -->
    <section class="card">
      <div class="flex items-start justify-between gap-4">
        <div>
          <h1 class="text-2xl font-semibold tracking-tight text-slate-900">
            Gestión de Inventario
          </h1>
          <p class="mt-2 text-slate-600">
            Administra secciones, ubicaciones, categorías, subcategorías e items de inventario.
          </p>
        </div>
      </div>
    </section>

    <!-- Tabs Navigation -->
    <div class="border-b border-slate-200 mt-4 mb-6 pt-3 pb-3">
      <nav class="flex flex-wrap gap-x-10 gap-y-2">
        <button
          @click="activeTab = 'secciones'"
          :class="[
            'whitespace-nowrap border-b-2 px-3 pt-2 pb-3 text-sm font-medium transition-colors',
            activeTab === 'secciones'
              ? 'border-sky-500 text-sky-600'
              : 'border-transparent text-slate-500 hover:border-slate-300 hover:text-slate-700'
          ]"
        >
          Secciones
        </button>
        <button
          @click="activeTab = 'ubicaciones'"
          :class="[
            'whitespace-nowrap border-b-2 px-3 pt-2 pb-3 text-sm font-medium transition-colors',
            activeTab === 'ubicaciones'
              ? 'border-sky-500 text-sky-600'
              : 'border-transparent text-slate-500 hover:border-slate-300 hover:text-slate-700'
          ]"
        >
          Ubicaciones
        </button>
        <button
          @click="activeTab = 'categorias'"
          :class="[
            'whitespace-nowrap border-b-2 px-3 pt-2 pb-3 text-sm font-medium transition-colors',
            activeTab === 'categorias'
              ? 'border-sky-500 text-sky-600'
              : 'border-transparent text-slate-500 hover:border-slate-300 hover:text-slate-700'
          ]"
        >
          Categorías
        </button>
        <button
          @click="activeTab = 'subcategorias'"
          :class="[
            'whitespace-nowrap border-b-2 px-3 pt-2 pb-3 text-sm font-medium transition-colors',
            activeTab === 'subcategorias'
              ? 'border-sky-500 text-sky-600'
              : 'border-transparent text-slate-500 hover:border-slate-300 hover:text-slate-700'
          ]"
        >
          Subcategorías
        </button>
        <button
          @click="activeTab = 'items'"
          :class="[
            'whitespace-nowrap border-b-2 px-3 pt-2 pb-3 text-sm font-medium transition-colors',
            activeTab === 'items'
              ? 'border-sky-500 text-sky-600'
              : 'border-transparent text-slate-500 hover:border-slate-300 hover:text-slate-700'
          ]"
        >
          Items
        </button>
        <button
          @click="activeTab = 'por_categoria'"
          :class="[
            'whitespace-nowrap border-b-2 px-3 pt-2 pb-3 text-sm font-medium transition-colors',
            activeTab === 'por_categoria'
              ? 'border-sky-500 text-sky-600'
              : 'border-transparent text-slate-500 hover:border-slate-300 hover:text-slate-700'
          ]"
        >
          Por Categoría
        </button>
      </nav>
    </div>

    <!-- Secciones -->
    <div v-if="activeTab === 'secciones'" class="space-y-6">
      <div class="flex items-center justify-between">
        <h2 class="text-xl font-semibold text-slate-900">Secciones</h2>
        <button @click="showForm = 'secciones'" class="btn btn-primary flex items-center gap-2">
          <span>+</span> Agregar Sección
        </button>
      </div>

      <div class="card overflow-hidden">
        <div class="overflow-x-auto">
          <table class="min-w-full divide-y divide-slate-200">
            <thead class="bg-slate-50">
              <tr>
                <th class="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">ID</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">Nombre</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">Acciones</th>
              </tr>
            </thead>
            <tbody class="bg-white divide-y divide-slate-200">
              <tr v-for="sec in secciones" :key="sec.id" class="hover:bg-slate-50 transition-colors">
                <td class="px-6 py-4 whitespace-nowrap text-sm text-slate-900">{{ sec.id }}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-slate-900">{{ sec.nombre }}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm font-medium">
                  <div class="flex items-center gap-2">
                    <button @click="editarSeccion(sec)" class="text-sky-600 hover:text-sky-800 transition-colors">Editar</button>
                    <span class="text-slate-300">|</span>
                    <button @click="eliminarSeccion(sec.id)" class="text-rose-600 hover:text-rose-800 transition-colors">Eliminar</button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- Ubicaciones -->
    <div v-if="activeTab === 'ubicaciones'" class="space-y-6">
      <div class="flex items-center justify-between">
        <h2 class="text-xl font-semibold text-slate-900">Ubicaciones</h2>
        <button @click="showForm = 'ubicaciones'" class="btn btn-primary flex items-center gap-2">
          <span>+</span> Agregar Ubicación
        </button>
      </div>

      <div class="card overflow-hidden">
        <div class="overflow-x-auto">
          <table class="min-w-full divide-y divide-slate-200">
            <thead class="bg-slate-50">
              <tr>
                <th class="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">ID</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">Nombre</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">Acciones</th>
              </tr>
            </thead>
            <tbody class="bg-white divide-y divide-slate-200">
              <tr v-for="ubi in ubicaciones" :key="ubi.id" class="hover:bg-slate-50 transition-colors">
                <td class="px-6 py-4 whitespace-nowrap text-sm text-slate-900">{{ ubi.id }}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-slate-900">{{ ubi.nombre }}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm font-medium">
                  <div class="flex items-center gap-2">
                    <button @click="editarUbicacion(ubi)" class="text-sky-600 hover:text-sky-800 transition-colors">Editar</button>
                    <span class="text-slate-300">|</span>
                    <button @click="eliminarUbicacion(ubi.id)" class="text-rose-600 hover:text-rose-800 transition-colors">Eliminar</button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- Categorías Inventario -->
    <div v-if="activeTab === 'categorias'" class="space-y-6">
      <div class="flex items-center justify-between">
        <h2 class="text-xl font-semibold text-slate-900">Categorías Inventario</h2>
        <button @click="showForm = 'categorias'" class="btn btn-primary flex items-center gap-2">
          <span>+</span> Agregar Categoría
        </button>
      </div>

      <div class="card overflow-hidden">
        <div class="overflow-x-auto">
          <table class="min-w-full divide-y divide-slate-200">
            <thead class="bg-slate-50">
              <tr>
                <th class="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">ID</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">Nombre</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">Acciones</th>
              </tr>
            </thead>
            <tbody class="bg-white divide-y divide-slate-200">
              <tr v-for="cat in categoriasInventario" :key="cat.id" class="hover:bg-slate-50 transition-colors">
                <td class="px-6 py-4 whitespace-nowrap text-sm text-slate-900">{{ cat.id }}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-slate-900">{{ cat.nombre }}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm font-medium">
                  <div class="flex items-center gap-2">
                    <button @click="editarCategoriaInventario(cat)" class="text-sky-600 hover:text-sky-800 transition-colors">Editar</button>
                    <span class="text-slate-300">|</span>
                    <button @click="eliminarCategoriaInventario(cat.id)" class="text-rose-600 hover:text-rose-800 transition-colors">Eliminar</button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- Subcategorías -->
    <div v-if="activeTab === 'subcategorias'" class="space-y-6">
      <div class="flex items-center justify-between">
        <h2 class="text-xl font-semibold text-slate-900">Subcategorías Inventario</h2>
        <button @click="showForm = 'subcategorias'" class="btn btn-primary flex items-center gap-2">
          <span>+</span> Agregar Subcategoría
        </button>
      </div>

      <div class="card overflow-hidden">
        <div class="overflow-x-auto">
          <table class="min-w-full divide-y divide-slate-200">
            <thead class="bg-slate-50">
              <tr>
                <th class="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">ID</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">Nombre</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">Categoría</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">Acciones</th>
              </tr>
            </thead>
            <tbody class="bg-white divide-y divide-slate-200">
              <tr v-for="sub in subcategoriasInventario" :key="sub.id" class="hover:bg-slate-50 transition-colors">
                <td class="px-6 py-4 whitespace-nowrap text-sm text-slate-900">{{ sub.id }}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-slate-900">{{ sub.nombre }}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-slate-900">{{ sub.categoria }}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm font-medium">
                  <div class="flex items-center gap-2">
                    <button @click="editarSubcategoriaInventario(sub)" class="text-sky-600 hover:text-sky-800 transition-colors">Editar</button>
                    <span class="text-slate-300">|</span>
                    <button @click="eliminarSubcategoriaInventario(sub.id)" class="text-rose-600 hover:text-rose-800 transition-colors">Eliminar</button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- Inventario Items -->
    <div v-if="activeTab === 'items'" class="space-y-6">
      <div class="flex items-center justify-between">
        <h2 class="text-xl font-semibold text-slate-900">Inventario Items</h2>
        <button @click="showForm = 'items'" class="btn btn-primary flex items-center gap-2">
          <span>+</span> Agregar Item
        </button>
      </div>

      <div class="card overflow-hidden">
        <div class="overflow-x-auto">
          <table class="min-w-full divide-y divide-slate-200">
            <thead class="bg-slate-50">
              <tr>
                <th class="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">ID</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">Nombre</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">Cantidad</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">Acciones</th>
              </tr>
            </thead>
            <tbody class="bg-white divide-y divide-slate-200">
              <tr v-for="item in inventarioItems" :key="item.id" class="hover:bg-slate-50 transition-colors">
                <td class="px-6 py-4 whitespace-nowrap text-sm text-slate-900">{{ item.id }}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-slate-900">{{ item.nombre }}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-slate-900">{{ item.cantidad }}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm font-medium">
                  <div class="flex items-center gap-2">
                    <button @click="editarInventarioItem(item)" class="text-sky-600 hover:text-sky-800 transition-colors">Editar</button>
                    <span class="text-slate-300">|</span>
                    <button @click="eliminarInventarioItem(item.id)" class="text-rose-600 hover:text-rose-800 transition-colors">Eliminar</button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- Inventario por Categoría -->
    <div v-if="activeTab === 'por_categoria'" class="space-y-6">
      <div class="flex items-center justify-between">
        <h2 class="text-xl font-semibold text-slate-900">Inventario por Categoría</h2>
      </div>

      <div class="card overflow-hidden">
        <div class="overflow-x-auto">
          <table class="min-w-full divide-y divide-slate-200">
            <thead class="bg-slate-50">
              <tr>
                <th class="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">ID</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">Nombre</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">Categoría</th>
              </tr>
            </thead>
            <tbody class="bg-white divide-y divide-slate-200">
              <tr v-for="it in inventarioPorCategoria" :key="it.id" class="hover:bg-slate-50 transition-colors">
                <td class="px-6 py-4 whitespace-nowrap text-sm text-slate-900">{{ it.id }}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-slate-900">{{ it.nombre }}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-slate-900">{{ it.categoria }}</td>
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
            {{
              showForm === 'secciones' ? (editing ? 'Editar Sección' : 'Agregar Sección') :
              showForm === 'ubicaciones' ? (editing ? 'Editar Ubicación' : 'Agregar Ubicación') :
              showForm === 'categorias' ? (editing ? 'Editar Categoría' : 'Agregar Categoría') :
              showForm === 'subcategorias' ? (editing ? 'Editar Subcategoría' : 'Agregar Subcategoría') :
              (editing ? 'Editar Item' : 'Agregar Item')
            }}
          </h3>
        </div>
        <form @submit.prevent="submitForm" class="p-6 space-y-4">
          <!-- Secciones / Ubicaciones / Categorías -->
          <div v-if="['secciones','ubicaciones','categorias'].includes(showForm)">
            <label class="block text-sm font-medium text-slate-700 mb-1">Nombre</label>
            <input
              v-model="formData.nombre"
              placeholder="Nombre"
              required
              class="w-full px-3 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-500 focus:border-sky-500 transition-colors"
            >
          </div>

          <!-- Subcategorías -->
          <div v-if="showForm === 'subcategorias'" class="space-y-4">
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
              <label class="block text-sm font-medium text-slate-700 mb-1">Categoría</label>
              <select
                v-model="formData.categoria"
                class="w-full px-3 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-500 focus:border-sky-500 transition-colors"
              >
                <option value="">Seleccionar Categoría</option>
                <option v-for="cat in categoriasInventario" :key="cat.id" :value="cat.id">
                  {{ cat.nombre }}
                </option>
              </select>
            </div>
          </div>

          <!-- Items -->
          <div v-if="showForm === 'items'" class="space-y-4">
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
              <label class="block text-sm font-medium text-slate-700 mb-1">Cantidad</label>
              <input
                v-model="formData.cantidad"
                type="number"
                min="0"
                placeholder="0"
                required
                class="w-full px-3 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-500 focus:border-sky-500 transition-colors"
              >
            </div>
          </div>

          <div class="flex gap-3 pt-4">
            <button type="submit" class="btn btn-primary flex-1">
              {{ editing ? 'Actualizar' : 'Guardar' }}
            </button>
            <button type="button" @click="showForm = null" class="btn btn-ghost flex-1">
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
  name: 'Inventario',
  data() {
    return {
      activeTab: 'secciones',
      secciones: [],
      ubicaciones: [],
      categoriasInventario: [],
      subcategoriasInventario: [],
      inventarioItems: [],
      inventarioPorCategoria: [],
      showForm: null,
      formData: {
        nombre: '',
        cantidad: '',
        categoria: ''
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
        this.obtenerSecciones(),
        this.obtenerUbicaciones(),
        this.obtenerCategoriasInventario(),
        this.obtenerSubcategoriasInventario(),
        this.obtenerInventarioItems(),
        this.obtenerInventarioPorCategoria()
      ])
    },
    async obtenerSecciones() {
      try {
        const response = await api.get('secciones')
        this.secciones = response.data
      } catch (error) {
        console.error('Error obteniendo secciones:', error)
      }
    },
    async obtenerUbicaciones() {
      try {
        const response = await api.get('ubicaciones')
        this.ubicaciones = response.data
      } catch (error) {
        console.error('Error obteniendo ubicaciones:', error)
      }
    },
    async obtenerCategoriasInventario() {
      try {
        const response = await api.get('categorias_inventario')
        this.categoriasInventario = response.data
      } catch (error) {
        console.error('Error obteniendo categorías inventario:', error)
      }
    },
    async obtenerSubcategoriasInventario() {
      try {
        const response = await api.get('subcategorias_inventario')
        this.subcategoriasInventario = response.data
      } catch (error) {
        console.error('Error obteniendo subcategorías:', error)
      }
    },
    async obtenerInventarioItems() {
      try {
        const response = await api.get('inventario_items')
        this.inventarioItems = response.data
      } catch (error) {
        console.error('Error obteniendo items:', error)
      }
    },
    async obtenerInventarioPorCategoria() {
      try {
        const response = await api.get('inventario_por_categoria')
        this.inventarioPorCategoria = response.data
      } catch (error) {
        console.error('Error obteniendo por categoría:', error)
      }
    },
    editarSeccion(sec) {
      this.editing = sec
      this.formData = { ...sec }
      this.showForm = 'secciones'
    },
    editarUbicacion(ubi) {
      this.editing = ubi
      this.formData = { ...ubi }
      this.showForm = 'ubicaciones'
    },
    editarCategoriaInventario(cat) {
      this.editing = cat
      this.formData = { ...cat }
      this.showForm = 'categorias'
    },
    editarSubcategoriaInventario(sub) {
      this.editing = sub
      this.formData = { ...sub }
      this.showForm = 'subcategorias'
    },
    editarInventarioItem(item) {
      this.editing = item
      this.formData = { ...item }
      this.showForm = 'items'
    },
    async submitForm() {
      try {
        const endpoint = this.showForm === 'secciones' ? 'secciones' :
                         this.showForm === 'ubicaciones' ? 'ubicaciones' :
                         this.showForm === 'categorias' ? 'categorias_inventario' :
                         this.showForm === 'subcategorias' ? 'subcategorias_inventario' :
                         'inventario_items'
        if (this.editing) {
          await api.put(`actualizar_${endpoint.replace('_', '')}/${this.editing.id}`, this.formData)
        } else {
          await api.post(`crear_${endpoint.replace('_', '')}`, this.formData)
        }
        this.showForm = null
        this.formData = { nombre: '', cantidad: '', categoria: '' }
        this.editing = null
        this.loadData()
      } catch (error) {
        console.error('Error guardando:', error)
      }
    },
    async eliminarSeccion(id) {
      if (confirm('¿Eliminar sección?')) {
        try {
          await api.delete(`eliminar_seccion/${id}`)
          this.loadData()
        } catch (error) {
          console.error('Error eliminando:', error)
        }
      }
    },
    async eliminarUbicacion(id) {
      if (confirm('¿Eliminar ubicación?')) {
        try {
          await api.delete(`eliminar_ubicacion/${id}`)
          this.loadData()
        } catch (error) {
          console.error('Error eliminando:', error)
        }
      }
    },
    async eliminarCategoriaInventario(id) {
      if (confirm('¿Eliminar categoría?')) {
        try {
          await api.delete(`eliminar_categoria_inventario/${id}`)
          this.loadData()
        } catch (error) {
          console.error('Error eliminando:', error)
        }
      }
    },
    async eliminarSubcategoriaInventario(id) {
      if (confirm('¿Eliminar subcategoría?')) {
        try {
          await api.delete(`eliminar_subcategoria_inventario/${id}`)
          this.loadData()
        } catch (error) {
          console.error('Error eliminando:', error)
        }
      }
    },
    async eliminarInventarioItem(id) {
      if (confirm('¿Eliminar item?')) {
        try {
          await api.delete(`eliminar_inventario_item/${id}`)
          this.loadData()
        } catch (error) {
          console.error('Error eliminando:', error)
        }
      }
    }
  }
}
</script>
