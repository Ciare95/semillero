<template>
  <div class="space-y-8">
    <!-- Tabs Navigation -->
    <div class="border-b border-slate-200 mt-4 mb-6 pt-3 pb-3">
      <nav class="flex flex-wrap gap-x-10 gap-y-2">
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
                <td class="px-6 py-4 whitespace-nowrap text-sm text-slate-900">
                  {{ formatFecha(venta.fecha_hora) }}
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-slate-900">{{ formatMoney(venta.total) }}</td>
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
              <tr v-if="ventas.length === 0">
                <td colspan="4" class="px-6 py-6 text-center text-slate-500">Sin ventas registradas</td>
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

      <!-- Sección de Productos -->
      <div class="card">
        <h3 class="text-lg font-semibold text-slate-900 mb-4">Productos</h3>
        
        <!-- Tabla de Productos -->
        <div class="mb-4">
          <div class="overflow-x-auto">
            <table class="min-w-full divide-y divide-slate-200">
              <thead class="bg-slate-50">
                <tr>
                  <th class="px-4 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">Producto</th>
                  <th class="px-4 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">Cantidad</th>
                  <th class="px-4 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">Precio</th>
                  <th class="px-4 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">Total</th>
                  <th class="px-4 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">Acciones</th>
                </tr>
              </thead>
              <tbody class="bg-white divide-y divide-slate-200">
                <tr v-for="(item, index) in productosVenta" :key="index" class="hover:bg-slate-50 transition-colors">
                  <td class="px-4 py-3 whitespace-nowrap text-sm text-slate-900">
                    {{ item.producto.nombre }}
                    <div class="text-xs text-slate-500">ID: {{ item.producto.id }}</div>
                  </td>
                  <td class="px-4 py-3 whitespace-nowrap">
                    <input
                      type="number"
                      min="1"
                      v-model.number="item.cantidad"
                      @change="actualizarTotalProducto(index)"
                      class="w-20 px-2 py-1 border border-slate-300 rounded focus:outline-none focus:ring-1 focus:ring-sky-500 focus:border-sky-500 transition-colors"
                    />
                  </td>
                  <td class="px-4 py-3 whitespace-nowrap text-sm text-slate-900">
                    {{ formatMoney(item.producto.precio_venta) }}
                  </td>
                  <td class="px-4 py-3 whitespace-nowrap text-sm text-slate-900 font-semibold">
                    {{ formatMoney(item.total) }}
                  </td>
                  <td class="px-4 py-3 whitespace-nowrap text-sm font-medium">
                    <button
                      @click="quitarProducto(index)"
                      class="text-rose-600 hover:text-rose-800 transition-colors"
                    >
                      Quitar
                    </button>
                  </td>
                </tr>
                <tr v-if="productosVenta.length === 0">
                  <td colspan="5" class="px-4 py-6 text-center text-slate-500">
                    No hay productos agregados
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <!-- Agregar Producto -->
        <div class="border-t border-slate-200 pt-4">
          <h4 class="text-md font-medium text-slate-700 mb-3">Agregar Producto</h4>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="relative">
              <label class="block text-sm font-medium text-slate-700 mb-1">Producto (ID o Nombre)</label>
              <input
                v-model="productQuery"
                @input="onProductInput"
                @keydown.enter.prevent="buscarProductoPorId"
                placeholder="Escribe ID y Enter, o escribe nombre para sugerencias"
                class="w-full px-3 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-500 focus:border-sky-500 transition-colors"
              />
              <!-- Sugerencias -->
              <div
                v-if="showSuggestions"
                class="absolute z-10 mt-1 w-full bg-white border border-slate-200 rounded-lg shadow-lg max-h-56 overflow-auto"
              >
                <button
                  v-for="p in filteredSuggestions"
                  :key="p.id"
                  type="button"
                  class="w-full text-left px-3 py-2 hover:bg-slate-50"
                  @click="seleccionarProducto(p)"
                >
                  <div class="flex justify-between">
                    <span class="text-sm text-slate-800">{{ p.nombre }}</span>
                    <span class="text-xs text-slate-500">ID: {{ p.id }}</span>
                  </div>
                  <div class="text-xs text-slate-500">
                    Precio: {{ formatMoney(p.precio_venta) }} · IVA: {{ Number(p.iva).toFixed(2) }}%
                  </div>
                </button>
                <div v-if="filteredSuggestions.length === 0" class="px-3 py-2 text-sm text-slate-500">
                  Sin resultados
                </div>
              </div>
              <!-- producto seleccionado -->
              <p v-if="selectedProduct" class="mt-2 text-xs text-slate-600">
                Seleccionado: <strong>{{ selectedProduct.nombre }}</strong>
                (Precio: {{ formatMoney(selectedProduct.precio_venta) }}, IVA: {{ Number(selectedProduct.iva).toFixed(2) }}%)
              </p>
            </div>
            <div>
              <label class="block text-sm font-medium text-slate-700 mb-1">Cantidad</label>
              <input
                type="number"
                min="1"
                v-model.number="cantidad"
                class="w-full px-3 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-500 focus:border-sky-500 transition-colors"
              />
            </div>
            <div class="md:col-span-2">
              <button
                type="button"
                @click="agregarProducto"
                class="btn btn-primary w-full"
                :disabled="!selectedProduct || !cantidad || cantidad <= 0"
              >
                Agregar Producto
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- Form Card -->
      <div class="card">
        <form @submit.prevent="crearVenta" class="space-y-5">
          <!-- 5 filas x 2 columnas -->
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">

            <!-- Fila 2: Cliente | Estado de la Venta -->
            <div>
              <label class="block text-sm font-medium text-slate-700 mb-1">Seleccionar Cliente</label>
              <select
                v-model="clienteId"
                class="w-full px-3 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-500 focus:border-sky-500 transition-colors"
              >
                <option value="">-- Sin cliente --</option>
                <option v-for="c in clientes" :key="c.id" :value="c.id">
                  {{ c.nombre || c.first_name || ('Cliente #' + c.id) }}
                </option>
              </select>
            </div>
            <div>
              <label class="block text-sm font-medium text-slate-700 mb-1">Estado de la Venta</label>
              <select
                v-model="estadoVenta"
                class="w-full px-3 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-500 focus:border-sky-500 transition-colors"
              >
                <option value="COMPLETADA">Completada</option>
                <option value="ANULADA">Anulada</option>
              </select>
              <p class="text-xs text-slate-500 mt-1">
                Nota: el backend crea la venta como COMPLETADA por defecto.
              </p>
            </div>

            <!-- Fila 3: Abono Inicial | (Método de Pago para compatibilidad backend) -->
            <div>
              <label class="block text-sm font-medium text-slate-700 mb-1">Abono Inicial</label>
              <input
                type="number"
                min="0"
                step="0.01"
                v-model.number="abonoInicial"
                class="w-full px-3 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-500 focus:border-sky-500 transition-colors"
              />
            </div>
            <div>
              <label class="block text-sm font-medium text-slate-700 mb-1">Método de Pago</label>
              <select
                v-model="metodoPago"
                class="w-full px-3 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-500 focus:border-sky-500 transition-colors"
              >
                <option value="EFECTIVO">Efectivo</option>
                <option value="TARJETA">Tarjeta</option>
                <option value="TRANSFERENCIA">Transferencia</option>
              </select>
            </div>

            <!-- Fila 4: (opcional/espacio) -->
            <div class="md:col-span-2">
              <label class="block text-sm font-medium text-slate-700 mb-1">Observaciones</label>
              <textarea
                v-model="observaciones"
                placeholder="Observaciones de la venta (opcional)"
                class="w-full px-3 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-500 focus:border-sky-500 transition-colors min-h-[72px]"
              ></textarea>
            </div>

            <!-- Fila 5: PRECIO TOTAL | Botón Transacción -->
            <div class="flex items-end">
              <div class="w-full">
                <label class="block text-sm font-medium text-slate-700 mb-1">PRECIO TOTAL</label>
                <div class="px-3 py-2 border border-slate-300 rounded-lg bg-slate-50 text-lg font-semibold">
                  {{ formatMoney(totalCalculado) }}
                </div>
              </div>
            </div>
            <div class="flex items-end">
              <button type="button" class="btn btn-ghost w-full" @click="onTransaccion">
                Transacción
              </button>
            </div>

            <!-- Fila 6: PRECIO TOTAL | Botón Guardar venta -->
            <div class="flex items-end">
              <div class="w-full">
                <label class="block text-sm font-medium text-slate-700 mb-1">PRECIO TOTAL</label>
                <div class="px-3 py-2 border border-slate-300 rounded-lg bg-slate-50 text-lg font-semibold">
                  {{ formatMoney(totalCalculado) }}
                </div>
              </div>
            </div>
            <div class="flex items-end">
              <button
                type="submit"
                class="btn btn-primary w-full"
                :disabled="loadingCreate"
              >
                {{ loadingCreate ? 'Guardando...' : 'Guardar venta' }}
              </button>
            </div>
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
      activeTab: 'crear',

      // Productos y clientes
      productos: [],
      clientes: [],

      // Formulario
      productQuery: '',
      selectedProduct: null,
      cantidad: 1,
      clienteId: '',
      estadoVenta: 'COMPLETADA',
      abonoInicial: 0,
      metodoPago: 'EFECTIVO',
      observaciones: '',

      // Productos en venta
      productosVenta: [],

      // UI
      loadingCreate: false,
    }
  },
  computed: {
    showSuggestions() {
      return this.productQuery && !this.selectedProduct
    },
    filteredSuggestions() {
      const q = this.productQuery.trim().toLowerCase()
      if (!q) return []
      const isNumeric = /^[0-9]+$/.test(q)
      const list = this.productos.filter(p => {
        if (isNumeric) {
          return String(p.id).includes(q) || (p.nombre || '').toLowerCase().includes(q)
        }
        return (p.nombre || '').toLowerCase().includes(q)
      })
      return list.slice(0, 10)
    },
    totalCalculado() {
      if (this.productosVenta.length === 0) return 0
      
      let totalGeneral = 0
      this.productosVenta.forEach(item => {
        const precio = Number(item.producto.precio_venta || 0)
        const ivaPercent = Number(item.producto.iva || 0)
        const subtotal = precio * item.cantidad
        const ivaValor = subtotal * (ivaPercent / 100)
        const total = subtotal + ivaValor
        totalGeneral += total
      })
      
      return Number(totalGeneral.toFixed(2))
    }
  },
  mounted() {
    this.listarVentas()
    this.cargarProductos()
    this.cargarClientes()
  },
  methods: {
    // Utilidades
    formatMoney(val) {
      const n = Number(val || 0)
      return n.toLocaleString('es-CO', { style: 'currency', currency: 'COP', minimumFractionDigits: 2 })
    },
    formatFecha(val) {
      try {
        const d = new Date(val)
        return d.toLocaleString('es-CO')
      } catch {
        return val
      }
    },

    // Carga inicial
    async cargarProductos() {
      try {
        const { data } = await api.get('productos')
        this.productos = Array.isArray(data) ? data : []
      } catch (error) {
        console.error('Error cargando productos:', error)
      }
    },
    async cargarClientes() {
      try {
        const { data } = await api.get('clientes')
        this.clientes = Array.isArray(data) ? data : []
      } catch (error) {
        console.error('Error cargando clientes:', error)
      }
    },

    // Listado/acciones ventas
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
    async anularVenta(id) {
      if (confirm('¿Anular venta?')) {
        try {
          await api.get(`anular_venta/${id}/`)
          this.listarVentas()
        } catch (error) {
          console.error('Error anulando venta:', error)
        }
      }
    },

    // Selección de producto
    onProductInput() {
      this.selectedProduct = null
    },
    seleccionarProducto(p) {
      this.selectedProduct = p
      this.productQuery = p.nombre || String(p.id)
    },
    async buscarProductoPorId() {
      const q = this.productQuery.trim()
      if (!/^[0-9]+$/.test(q)) return
      try {
        const { data } = await api.get(`productos/${q}/`)
        if (data && data.id) {
          this.seleccionarProducto(data)
        }
      } catch (error) {
        console.error('Producto no encontrado por ID:', error)
        alert('Producto no encontrado por ID')
      }
    },


    // Gestión de productos en venta
    agregarProducto() {
      if (!this.selectedProduct || !this.cantidad || this.cantidad <= 0) {
        alert('Debe seleccionar un producto y especificar una cantidad válida')
        return
      }

      // Verificar si el producto ya está en la lista
      const productoExistente = this.productosVenta.find(item => 
        item.producto.id === this.selectedProduct.id
      )

      if (productoExistente) {
        // Si ya existe, actualizar la cantidad
        productoExistente.cantidad += this.cantidad
        this.actualizarTotalProducto(this.productosVenta.indexOf(productoExistente))
      } else {
        // Si no existe, agregar nuevo producto
        const precio = Number(this.selectedProduct.precio_venta || 0)
        const ivaPercent = Number(this.selectedProduct.iva || 0)
        const subtotal = precio * this.cantidad
        const ivaValor = subtotal * (ivaPercent / 100)
        const total = subtotal + ivaValor

        this.productosVenta.push({
          producto: { ...this.selectedProduct },
          cantidad: this.cantidad,
          total: Number(total.toFixed(2))
        })
      }

      // Limpiar formulario de selección
      this.productQuery = ''
      this.selectedProduct = null
      this.cantidad = 1
    },

    actualizarTotalProducto(index) {
      const item = this.productosVenta[index]
      if (item && item.cantidad > 0) {
        const precio = Number(item.producto.precio_venta || 0)
        const ivaPercent = Number(item.producto.iva || 0)
        const subtotal = precio * item.cantidad
        const ivaValor = subtotal * (ivaPercent / 100)
        const total = subtotal + ivaValor
        item.total = Number(total.toFixed(2))
      }
    },

    quitarProducto(index) {
      this.productosVenta.splice(index, 1)
    },

    // Crear venta actualizada para múltiples productos
    async crearVenta() {
      if (this.productosVenta.length === 0) {
        alert('Debe agregar al menos un producto a la venta')
        return
      }

      const obsExtras = [
        this.observaciones && `Obs: ${this.observaciones}`,
        this.estadoVenta && `Estado (UI): ${this.estadoVenta}`,
        (this.abonoInicial || 0) > 0 && `Abono inicial: ${this.formatMoney(this.abonoInicial)}`
      ].filter(Boolean).join(' | ')

      const payload = {
        cliente: this.clienteId || null,
        metodo_pago: this.metodoPago,
        observaciones: obsExtras,
        items: this.productosVenta.map(item => ({
          producto: item.producto.id,
          cantidad: item.cantidad
        }))
      }

      this.loadingCreate = true
      try {
        await api.post('crear_venta/', payload)
        // Reset completo
        this.productQuery = ''
        this.selectedProduct = null
        this.cantidad = 1
        this.clienteId = ''
        this.estadoVenta = 'COMPLETADA'
        this.abonoInicial = 0
        this.metodoPago = 'EFECTIVO'
        this.observaciones = ''
        this.productosVenta = []
        this.activeTab = 'ventas'
        await this.listarVentas()
      } catch (error) {
        console.error('Error creando venta:', error)
        alert('No fue posible crear la venta. Revise la consola para más detalles.')
      } finally {
        this.loadingCreate = false
      }
    },

    // Placeholder transacción
    onTransaccion() {
      alert('Funcionalidad de Transacción pendiente de definición.')
    }
  }
}
</script>
