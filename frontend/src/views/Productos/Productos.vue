<template>
  <div class="space-y-8">
    <!-- Header -->
    <section class="card">
      <div class="flex items-start justify-between gap-4">
        <div>
          <h1 class="text-2xl font-semibold tracking-tight text-slate-900">
            Gestión de Productos
          </h1>
          <p class="mt-2 text-slate-600">
            Administra productos, categorías, marcas y productos especiales desde un solo lugar.
          </p>
        </div>
      </div>
    </section>

    <!-- Tabs Navigation -->
    <div class="border-b border-slate-200 mt-4 mb-6 pt-3 pb-3">
      <nav class="flex flex-wrap gap-x-10 gap-y-2">
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
          @click="activeTab = 'marcas'"
          :class="[
            'whitespace-nowrap border-b-2 px-3 pt-2 pb-3 text-sm font-medium transition-colors',
            activeTab === 'marcas'
              ? 'border-sky-500 text-sky-600'
              : 'border-transparent text-slate-500 hover:border-slate-300 hover:text-slate-700'
          ]"
        >
          Marcas
        </button>
        <button
          @click="activeTab = 'especiales'"
          :class="[
            'whitespace-nowrap border-b-2 px-3 pt-2 pb-3 text-sm font-medium transition-colors',
            activeTab === 'especiales'
              ? 'border-sky-500 text-sky-600'
              : 'border-transparent text-slate-500 hover:border-slate-300 hover:text-slate-700'
          ]"
        >
          Productos Especiales
        </button>
        <button
          @click="activeTab = 'servicios'"
          :class="[
            'whitespace-nowrap border-b-2 px-3 pt-2 pb-3 text-sm font-medium transition-colors',
            activeTab === 'servicios'
              ? 'border-sky-500 text-sky-600'
              : 'border-transparent text-slate-500 hover:border-slate-300 hover:text-slate-700'
          ]"
        >
          Productos Servicio
        </button>
      </nav>
    </div>

    <!-- Productos -->
    <div v-if="activeTab === 'productos'" class="space-y-6">
      <!-- Header with Actions -->
      <div class="flex items-center justify-between">
        <h2 class="text-xl font-semibold text-slate-900">Productos</h2>
        <button 
          @click="showForm = 'productos'" 
          class="btn btn-primary flex items-center gap-2"
        >
          <span>+</span>
          Agregar Producto
        </button>
      </div>

      <!-- Products Table -->
      <div class="card overflow-hidden">
        <div class="overflow-x-auto">
          <table class="min-w-full divide-y divide-slate-200">
            <thead class="bg-slate-50">
              <tr>
                <th class="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">ID</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">Nombre</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">Precio</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">IVA</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">Categoría</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">Marca</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">Acciones</th>
              </tr>
            </thead>
            <tbody class="bg-white divide-y divide-slate-200">
              <tr v-for="producto in productos" :key="producto.id" class="hover:bg-slate-50 transition-colors">
                <td class="px-6 py-4 whitespace-nowrap text-sm text-slate-900">{{ producto.id }}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-slate-900">{{ producto.nombre }}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-slate-900">${{ producto.precio }}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-slate-900">{{ producto.iva }}%</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-slate-900">{{ producto.categoria }}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-slate-900">{{ producto.marca }}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm font-medium">
                  <div class="flex items-center gap-2">
                    <button 
                      @click="editarProducto(producto)" 
                      class="text-sky-600 hover:text-sky-800 transition-colors"
                    >
                      Editar
                    </button>
                    <span class="text-slate-300">|</span>
                    <button 
                      @click="eliminarProducto(producto.id)" 
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

    <!-- Categorías -->
    <div v-if="activeTab === 'categorias'" class="space-y-6">
      <!-- Header with Actions -->
      <div class="flex items-center justify-between">
        <h2 class="text-xl font-semibold text-slate-900">Categorías</h2>
        <button 
          @click="showForm = 'categorias'" 
          class="btn btn-primary flex items-center gap-2"
        >
          <span>+</span>
          Agregar Categoría
        </button>
      </div>

      <!-- Categories Table -->
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
              <tr v-for="categoria in categorias" :key="categoria.id" class="hover:bg-slate-50 transition-colors">
                <td class="px-6 py-4 whitespace-nowrap text-sm text-slate-900">{{ categoria.id }}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-slate-900">{{ categoria.nombre }}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm font-medium">
                  <div class="flex items-center gap-2">
                    <button 
                      @click="editarCategoria(categoria)" 
                      class="text-sky-600 hover:text-sky-800 transition-colors"
                    >
                      Editar
                    </button>
                    <span class="text-slate-300">|</span>
                    <button 
                      @click="eliminarCategoria(categoria.id)" 
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

    <!-- Marcas -->
    <div v-if="activeTab === 'marcas'" class="space-y-6">
      <!-- Header with Actions -->
      <div class="flex items-center justify-between">
        <h2 class="text-xl font-semibold text-slate-900">Marcas</h2>
        <button 
          @click="showForm = 'marcas'" 
          class="btn btn-primary flex items-center gap-2"
        >
          <span>+</span>
          Agregar Marca
        </button>
      </div>

      <!-- Brands Table -->
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
              <tr v-for="marca in marcas" :key="marca.id" class="hover:bg-slate-50 transition-colors">
                <td class="px-6 py-4 whitespace-nowrap text-sm text-slate-900">{{ marca.id }}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-slate-900">{{ marca.nombre }}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm font-medium">
                  <div class="flex items-center gap-2">
                    <button 
                      @click="editarMarca(marca)" 
                      class="text-sky-600 hover:text-sky-800 transition-colors"
                    >
                      Editar
                    </button>
                    <span class="text-slate-300">|</span>
                    <button 
                      @click="eliminarMarca(marca.id)" 
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

    <!-- Productos Especiales -->
    <div v-if="activeTab === 'especiales'" class="space-y-6">
      <!-- Header with Actions -->
      <div class="flex items-center justify-between">
        <h2 class="text-xl font-semibold text-slate-900">Productos Especiales</h2>
        <div class="flex items-center gap-3">
          <button 
            @click="calcularPrecioCorte" 
            class="btn btn-ghost flex items-center gap-2"
          >
            <span>📊</span>
            Calcular Precio Corte
          </button>
          <button 
            @click="showForm = 'especiales'" 
            class="btn btn-primary flex items-center gap-2"
          >
            <span>+</span>
            Agregar Producto Especial
          </button>
        </div>
      </div>

      <!-- Special Products Table -->
      <div class="card overflow-hidden">
        <div class="overflow-x-auto">
          <table class="min-w-full divide-y divide-slate-200">
            <thead class="bg-slate-50">
              <tr>
                <th class="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">ID</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">Nombre</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">Precio</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">Acciones</th>
              </tr>
            </thead>
            <tbody class="bg-white divide-y divide-slate-200">
              <tr v-for="especial in productosEspeciales" :key="especial.id" class="hover:bg-slate-50 transition-colors">
                <td class="px-6 py-4 whitespace-nowrap text-sm text-slate-900">{{ especial.id }}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-slate-900">{{ especial.nombre }}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-slate-900">${{ especial.precio }}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm font-medium">
                  <div class="flex items-center gap-2">
                    <button 
                      @click="editarProductoEspecial(especial)" 
                      class="text-sky-600 hover:text-sky-800 transition-colors"
                    >
                      Editar
                    </button>
                    <span class="text-slate-300">|</span>
                    <button 
                      @click="eliminarProductoEspecial(especial.id)" 
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

    <!-- Productos Servicio -->
    <div v-if="activeTab === 'servicios'" class="space-y-6">
      <!-- Header with Actions -->
      <div class="flex items-center justify-between">
        <h2 class="text-xl font-semibold text-slate-900">Productos Servicio</h2>
        <button 
          @click="showForm = 'servicios'" 
          class="btn btn-primary flex items-center gap-2"
        >
          <span>+</span>
          Agregar Producto Servicio
        </button>
      </div>

      <!-- Service Products Table -->
      <div class="card overflow-hidden">
        <div class="overflow-x-auto">
          <table class="min-w-full divide-y divide-slate-200">
            <thead class="bg-slate-50">
              <tr>
                <th class="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">ID</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">Nombre</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">Precio</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">Acciones</th>
              </tr>
            </thead>
            <tbody class="bg-white divide-y divide-slate-200">
              <tr v-for="servicio in productosServicio" :key="servicio.id" class="hover:bg-slate-50 transition-colors">
                <td class="px-6 py-4 whitespace-nowrap text-sm text-slate-900">{{ servicio.id }}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-slate-900">{{ servicio.nombre }}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-slate-900">${{ servicio.precio }}</td>
                <td class="px-6 py-4 whitespace-nowrap text-sm font-medium">
                  <div class="flex items-center gap-2">
                    <button 
                      @click="editarProductoServicio(servicio)" 
                      class="text-sky-600 hover:text-sky-800 transition-colors"
                    >
                      Editar
                    </button>
                    <span class="text-slate-300">|</span>
                    <button 
                      @click="eliminarProductoServicio(servicio.id)" 
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
            {{ showForm === 'productos' ? (editing ? 'Editar Producto' : 'Agregar Producto') : 
               showForm === 'categorias' ? (editing ? 'Editar Categoría' : 'Agregar Categoría') : 
               showForm === 'marcas' ? (editing ? 'Editar Marca' : 'Agregar Marca') : 
               showForm === 'especiales' ? (editing ? 'Editar Producto Especial' : 'Agregar Producto Especial') : 
               (editing ? 'Editar Producto Servicio' : 'Agregar Producto Servicio') }}
          </h3>
        </div>
        <form @submit.prevent="submitForm" class="p-6 space-y-4">
          <div>
            <label class="block text-sm font-medium text-slate-700 mb-1">Nombre</label>
            <input 
              v-model="formData.nombre" 
              placeholder="Ingresa el nombre" 
              required
              class="w-full px-3 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-500 focus:border-sky-500 transition-colors"
            >
          </div>
          
          <div v-if="showForm === 'productos'">
            <label class="block text-sm font-medium text-slate-700 mb-1">Precio</label>
            <input 
              v-model="formData.precio" 
              placeholder="0.00" 
              type="number" 
              step="0.01" 
              required
              class="w-full px-3 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-500 focus:border-sky-500 transition-colors"
            >
          </div>
          
          <div v-if="showForm === 'productos'">
            <label class="block text-sm font-medium text-slate-700 mb-1">IVA (%)</label>
            <input 
              v-model="formData.iva" 
              placeholder="0.00" 
              type="number" 
              step="0.01" 
              required
              class="w-full px-3 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-500 focus:border-sky-500 transition-colors"
            >
          </div>
          
          <div v-if="showForm === 'productos'">
            <label class="block text-sm font-medium text-slate-700 mb-1">Categoría</label>
            <select 
              v-model="formData.categoria"
              class="w-full px-3 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-500 focus:border-sky-500 transition-colors"
            >
              <option value="">Seleccionar Categoría</option>
              <option v-for="cat in categorias" :value="cat.id" :key="cat.id">{{ cat.nombre }}</option>
            </select>
          </div>
          
          <div v-if="showForm === 'productos'">
            <label class="block text-sm font-medium text-slate-700 mb-1">Marca</label>
            <select 
              v-model="formData.marca"
              class="w-full px-3 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-500 focus:border-sky-500 transition-colors"
            >
              <option value="">Seleccionar Marca</option>
              <option v-for="mar in marcas" :value="mar.id" :key="mar.id">{{ mar.nombre }}</option>
            </select>
          </div>
          
          <div v-if="showForm !== 'productos'">
            <label class="block text-sm font-medium text-slate-700 mb-1">Precio</label>
            <input 
              v-model="formData.precio" 
              placeholder="0.00" 
              type="number" 
              step="0.01" 
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
  name: 'Productos',
  data() {
    return {
      activeTab: 'productos',
      productos: [],
      categorias: [],
      marcas: [],
      productosEspeciales: [],
      productosServicio: [],
      showForm: null,
      formData: {
        nombre: '',
        precio: '',
        iva: '',
        categoria: '',
        marca: ''
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
        this.obtenerProductos(),
        this.obtenerCategorias(),
        this.obtenerMarcas(),
        this.obtenerProductosEspeciales(),
        this.obtenerProductosServicio()
      ])
    },
    async obtenerProductos() {
      try {
        const response = await api.get('productos')
        this.productos = response.data
      } catch (error) {
        console.error('Error obteniendo productos:', error)
      }
    },
    async obtenerCategorias() {
      try {
        const response = await api.get('categorias')
        this.categorias = response.data
      } catch (error) {
        console.error('Error obteniendo categorías:', error)
      }
    },
    async obtenerMarcas() {
      try {
        const response = await api.get('marcas')
        this.marcas = response.data
      } catch (error) {
        console.error('Error obteniendo marcas:', error)
      }
    },
    async obtenerProductosEspeciales() {
      try {
        const response = await api.get('productos_especiales')
        this.productosEspeciales = response.data
      } catch (error) {
        console.error('Error obteniendo productos especiales:', error)
      }
    },
    async obtenerProductosServicio() {
      try {
        const response = await api.get('productos_servicio')
        this.productosServicio = response.data
      } catch (error) {
        console.error('Error obteniendo productos servicio:', error)
      }
    },
    editarProducto(producto) {
      this.editing = producto
      this.formData = { ...producto }
      this.showForm = 'productos'
    },
    editarCategoria(categoria) {
      this.editing = categoria
      this.formData = { ...categoria }
      this.showForm = 'categorias'
    },
    editarMarca(marca) {
      this.editing = marca
      this.formData = { ...marca }
      this.showForm = 'marcas'
    },
    editarProductoEspecial(especial) {
      this.editing = especial
      this.formData = { ...especial }
      this.showForm = 'especiales'
    },
    editarProductoServicio(servicio) {
      this.editing = servicio
      this.formData = { ...servicio }
      this.showForm = 'servicios'
    },
    async submitForm() {
      try {
        if (this.editing) {
          if (this.showForm === 'productos') {
            await api.put(`actualizar_producto/${this.editing.id}`, this.formData)
          } else if (this.showForm === 'categorias') {
            await api.put(`actualizar_categoria/${this.editing.id}`, this.formData)
          } else if (this.showForm === 'marcas') {
            await api.put(`actualizar_marca/${this.editing.id}`, this.formData)
          } else if (this.showForm === 'especiales') {
            await api.put(`actualizar_producto_especial/${this.editing.id}`, this.formData)
          } else if (this.showForm === 'servicios') {
            await api.put(`actualizar_producto_servicio/${this.editing.id}`, this.formData)
          }
        } else {
          if (this.showForm === 'productos') {
            await api.post('crear_producto', this.formData)
          } else if (this.showForm === 'categorias') {
            await api.post('crear_categoria', this.formData)
          } else if (this.showForm === 'marcas') {
            await api.post('crear_marca', this.formData)
          } else if (this.showForm === 'especiales') {
            await api.post('crear_producto_especial', this.formData)
          } else if (this.showForm === 'servicios') {
            await api.post('crear_producto_servicio', this.formData)
          }
        }
        this.showForm = null
        this.formData = { nombre: '', precio: '', iva: '', categoria: '', marca: '' }
        this.editing = null
        this.loadData()
      } catch (error) {
        console.error('Error guardando:', error)
      }
    },
    async eliminarProducto(id) {
      if (confirm('¿Eliminar producto?')) {
        try {
          await api.delete(`eliminar_producto/${id}`)
          this.loadData()
        } catch (error) {
          console.error('Error eliminando:', error)
        }
      }
    },
    async eliminarCategoria(id) {
      if (confirm('¿Eliminar categoría?')) {
        try {
          await api.delete(`eliminar_categoria/${id}`)
          this.loadData()
        } catch (error) {
          console.error('Error eliminando:', error)
        }
      }
    },
    async eliminarMarca(id) {
      if (confirm('¿Eliminar marca?')) {
        try {
          await api.delete(`eliminar_marca/${id}`)
          this.loadData()
        } catch (error) {
          console.error('Error eliminando:', error)
        }
      }
    },
    async eliminarProductoEspecial(id) {
      if (confirm('¿Eliminar producto especial?')) {
        try {
          await api.delete(`eliminar_producto_especial/${id}`)
          this.loadData()
        } catch (error) {
          console.error('Error eliminando:', error)
        }
      }
    },
    async eliminarProductoServicio(id) {
      if (confirm('¿Eliminar producto servicio?')) {
        try {
          await api.delete(`eliminar_producto_servicio/${id}`)
          this.loadData()
        } catch (error) {
          console.error('Error eliminando:', error)
        }
      }
    },
    async calcularPrecioCorte() {
      try {
        const response = await api.get('calcular_precio_corte')
        alert('Precio calculado: ' + response.data.precio)
      } catch (error) {
        console.error('Error calculando precio:', error)
      }
    }
  }
}
</script>
