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

      <!-- Filtros de Fecha -->
      <div class="card">
        <h3 class="text-lg font-semibold text-slate-900 mb-4">Filtrar por Fecha</h3>
        <div class="grid grid-cols-1 md:grid-cols-4 gap-4">
          <!-- Filtro por Día -->
          <div>
            <label class="block text-sm font-medium text-slate-700 mb-1">Día</label>
            <div class="relative" @click="$refs.dateInput.focus()">
              <input
                ref="dateInput"
                type="date"
                v-model="filtroDia"
                @change="aplicarFiltroDia"
                class="w-full px-3 py-2 pr-10 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-500 focus:border-sky-500 transition-colors cursor-pointer bg-white"
                :title="filtroDia ? `Fecha seleccionada: ${formatearFechaParaMostrar(filtroDia)}` : 'Seleccionar fecha'"
                onkeydown="return false"
                onpaste="return false"
                oncut="return false"
              />
              <svg class="absolute right-3 top-1/2 transform -translate-y-1/2 w-5 h-5 text-slate-400 pointer-events-none" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"></path>
              </svg>
            </div>
            <p v-if="filtroDia" class="text-xs text-slate-500 mt-1">
              {{ formatearFechaParaMostrar(filtroDia) }}
            </p>
          </div>
          
          <!-- Filtro por Mes -->
          <div>
            <label class="block text-sm font-medium text-slate-700 mb-1">Mes</label>
            <select
              v-model="filtroMes"
              @change="aplicarFiltroMes"
              class="w-full px-3 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-500 focus:border-sky-500 transition-colors"
            >
              <option value="">Seleccionar mes</option>
              <option v-for="mes in meses" :key="mes.value" :value="`${new Date().getFullYear()}-${mes.value}`">
                {{ mes.label }} {{ new Date().getFullYear() }}
              </option>
            </select>
            <p v-if="filtroMes" class="text-xs text-slate-500 mt-1">
              {{ formatearMesParaMostrar(filtroMes) }}
            </p>
          </div>
          
          <!-- Filtro por Año -->
          <div>
            <label class="block text-sm font-medium text-slate-700 mb-1">Año</label>
            <select
              v-model="filtroAnio"
              @change="aplicarFiltroAnio"
              class="w-full px-3 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-500 focus:border-sky-500 transition-colors"
            >
              <option value="">Seleccionar año</option>
              <option v-for="anio in añosDisponibles" :key="anio" :value="anio">{{ anio }}</option>
            </select>
          </div>
          
          <!-- Botones de Acción -->
          <div class="flex items-end gap-2">
            <button
              @click="limpiarFiltros"
              class="btn btn-ghost flex-1"
            >
              Limpiar
            </button>
            <button
              @click="filtrarHoy"
              class="btn btn-primary"
            >
              Hoy
            </button>
          </div>
        </div>
        
        <!-- Estado del filtro actual -->
        <div v-if="filtroActual" class="mt-3 p-3 bg-slate-50 rounded-lg">
          <p class="text-sm text-slate-600">
            <strong>Filtro actual:</strong> {{ filtroActual }}
          </p>
        </div>
      </div>

      <!-- Resumen de Ventas Filtradas -->
      <div class="card bg-sky-50 border-sky-200">
        <div class="flex items-center justify-between">
          <div>
            <h3 class="text-lg font-semibold text-slate-900">Resumen de Ventas</h3>
            <p class="text-sm text-slate-600 mt-1">
              {{ filtroActual || 'Todas las ventas' }}
            </p>
          </div>
          <div class="text-right">
            <p class="text-sm text-slate-600">Total de ventas</p>
            <p class="text-2xl font-bold text-sky-700">{{ formatMoney(totalVentasFiltradas) }}</p>
            <p class="text-xs text-slate-500 mt-1">{{ ventas.length }} venta{{ ventas.length !== 1 ? 's' : '' }}</p>
          </div>
        </div>
      </div>

      <!-- Sales Table -->
      <div class="card overflow-hidden">
        <div class="overflow-x-auto">
          <table class="min-w-full divide-y divide-slate-200">
            <thead class="bg-slate-50">
              <tr>
                <th class="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">ID</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">Fecha</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">Vendedor</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">Cliente</th>
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
                <td class="px-6 py-4 whitespace-nowrap text-sm text-slate-900">
                  {{ obtenerNombreUsuario(venta.vendedor) }}
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-slate-900">
                  {{ obtenerNombreCliente(venta.cliente) }}
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
                <td colspan="6" class="px-6 py-6 text-center text-slate-500">Sin ventas registradas</td>
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
                  <th class="px-4 py-3 text-left text-xs font-medium text-slate-500 uppercase tracking-wider">Precio por Unidad</th>
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
                <option value="PENDIENTE">Pendiente</option>
                <option value="COMPLETADA">Completada</option>
                <option value="ANULADA">Anulada</option>
              </select>
            </div>

            <!-- Fila 3: Abono Inicial | (Método de Pago para compatibilidad backend) -->
            <div>
              <label class="block text-sm font-medium text-slate-700 mb-1">Abono Inicial</label>
              <input
                type="number"
                min="0"
                step="0.01"
                v-model.number="abonoInicial"
                :disabled="abonoInicialDeshabilitado"
                :class="[
                  'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 transition-colors',
                  abonoInicialDeshabilitado
                    ? 'border-slate-200 bg-slate-100 text-slate-500 cursor-not-allowed'
                    : 'border-slate-300 bg-white focus:ring-sky-500 focus:border-sky-500'
                ]"
              />
              <p v-if="abonoInicialDeshabilitado" class="text-xs text-slate-500 mt-1">
                Solo disponible para ventas pendientes
              </p>
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

            <!-- Fila 5: PRECIO TOTAL (ocupa todo el ancho) -->
            <div class="md:col-span-2">
              <label class="block text-sm font-medium text-slate-700 mb-1">PRECIO TOTAL</label>
              <div class="px-3 py-2 border-2 border-green-500 rounded-lg bg-slate-50 text-lg font-semibold text-center">
                {{ formatMoney(totalCalculado) }}
              </div>
            </div>

            <!-- Fila 6: Botones Transacción y Guardar Venta -->
            <div class="flex items-end">
              <button 
                type="button" 
                class="btn w-full"
                @click="onTransaccion"
                style="background-color: #b8860b; color: white; border-color: #b8860b;"
              >
                Transacción
              </button>
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

    <!-- Modal de Transacción -->
    <div v-if="showModalTransaccion" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div class="bg-white rounded-lg shadow-xl w-full max-w-md mx-4">
        <!-- Header -->
        <div class="px-6 py-4 border-b border-slate-200">
          <h3 class="text-lg font-semibold text-slate-900">Transacción</h3>
        </div>
        
        <!-- Content -->
        <div class="px-6 py-4 space-y-4">
          <!-- Total a Pagar -->
          <div>
            <label class="block text-sm font-medium text-slate-700 mb-1">Total a pagar</label>
            <div class="px-3 py-2 border-2 border-green-500 rounded-lg bg-slate-50 text-lg font-semibold text-center">
              {{ formatMoney(totalCalculado) }}
            </div>
          </div>
          
          <!-- Importe Recibido -->
          <div>
            <label class="block text-sm font-medium text-slate-700 mb-1">Importe recibido</label>
            <input
              type="number"
              min="0"
              step="0.01"
              v-model.number="importeRecibido"
              @input="calcularCambio"
              placeholder="0.00"
              class="w-full px-3 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-500 focus:border-sky-500 transition-colors text-lg font-semibold text-center"
            />
          </div>
          
          <!-- Cambio a Entregar -->
          <div>
            <label class="block text-sm font-medium text-slate-700 mb-1">Cambio a entregar</label>
            <div 
              :class="[
                'px-3 py-2 border-2 rounded-lg text-lg font-semibold text-center transition-colors',
                cambioCalculado >= 0 
                  ? 'border-green-500 bg-green-50 text-green-700' 
                  : 'border-red-500 bg-red-50 text-red-700'
              ]"
            >
              {{ formatMoney(cambioCalculado) }}
            </div>
            <p v-if="cambioCalculado < 0" class="text-xs text-red-600 mt-1">
              El importe recibido es insuficiente
            </p>
          </div>
        </div>
        
        <!-- Footer -->
        <div class="px-6 py-4 border-t border-slate-200 flex justify-end gap-3">
          <button
            @click="cerrarModalTransaccion"
            class="btn btn-ghost"
          >
            Cancelar
          </button>
          <button
            @click="confirmarTransaccion"
            class="btn btn-primary"
            :disabled="cambioCalculado < 0"
          >
            Confirmar
          </button>
        </div>
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

      // Productos, clientes y usuarios
      productos: [],
      clientes: [],
      usuarios: [],

      // Formulario
      productQuery: '',
      selectedProduct: null,
      cantidad: 1,
      clienteId: '',
      estadoVenta: 'PENDIENTE',
      abonoInicial: 0,
      metodoPago: 'EFECTIVO',
      observaciones: '',

      // Productos en venta
      productosVenta: [],

      // Filtros de fecha
      filtroDia: '',
      filtroMes: '',
      filtroAnio: '',
      filtroActual: '',

      // Meses para el select
      meses: [
        { value: '01', label: 'Enero' },
        { value: '02', label: 'Febrero' },
        { value: '03', label: 'Marzo' },
        { value: '04', label: 'Abril' },
        { value: '05', label: 'Mayo' },
        { value: '06', label: 'Junio' },
        { value: '07', label: 'Julio' },
        { value: '08', label: 'Agosto' },
        { value: '09', label: 'Septiembre' },
        { value: '10', label: 'Octubre' },
        { value: '11', label: 'Noviembre' },
        { value: '12', label: 'Diciembre' }
      ],

      // UI
      loadingCreate: false,

      // Modal de Transacción
      showModalTransaccion: false,
      importeRecibido: 0,
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
        const subtotal = precio * item.cantidad
        totalGeneral += subtotal
      })
      
      return Number(totalGeneral.toFixed(2))
    },
    añosDisponibles() {
      const añoActual = new Date().getFullYear()
      const años = []
      for (let i = añoActual; i >= 2020; i--) {
        años.push(i)
      }
      return años
    },
    // Determina si el campo abono inicial debe estar deshabilitado
    abonoInicialDeshabilitado() {
      return this.estadoVenta !== 'PENDIENTE'
    },
    // Calcula el total de las ventas filtradas
    totalVentasFiltradas() {
      if (this.ventas.length === 0) return 0
      
      let total = 0
      this.ventas.forEach(venta => {
        total += Number(venta.total || 0)
      })
      
      return Number(total.toFixed(2))
    },
    // Calcula el cambio a entregar
    cambioCalculado() {
      const total = this.totalCalculado
      const recibido = Number(this.importeRecibido || 0)
      return Number((recibido - total).toFixed(2))
    }
  },
  mounted() {
    // Por defecto mostrar ventas del día actual
    this.filtrarHoy()
    this.cargarProductos()
    this.cargarClientes()
    this.cargarUsuarios()
  },
  watch: {
    // Watcher para el estado de venta
    estadoVenta(newEstado) {
      if (newEstado === 'COMPLETADA') {
        // Si la venta está completada, resetear el abono inicial a 0
        this.abonoInicial = 0
      }
    }
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
    formatearFechaParaMostrar(fecha) {
      try {
        const d = new Date(fecha)
        return d.toLocaleDateString('es-CO', { 
          year: 'numeric', 
          month: 'long', 
          day: 'numeric' 
        })
      } catch {
        return fecha
      }
    },
    formatearMesParaMostrar(mes) {
      try {
        const [anio, mesNum] = mes.split('-')
        const fecha = new Date(parseInt(anio), parseInt(mesNum) - 1, 1)
        return fecha.toLocaleDateString('es-CO', { 
          year: 'numeric', 
          month: 'long'
        })
      } catch {
        return mes
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

    async cargarUsuarios() {
      try {
        const { data } = await api.get('usuarios')
        this.usuarios = Array.isArray(data) ? data : []
      } catch (error) {
        console.error('Error cargando usuarios:', error)
      }
    },

    // Listado/acciones ventas
    async listarVentas(filtros = {}) {
      try {
        const params = new URLSearchParams()
        
        // Agregar filtros a los parámetros de consulta
        if (filtros.fecha_desde) {
          params.append('fecha_desde', filtros.fecha_desde)
        }
        if (filtros.fecha_hasta) {
          params.append('fecha_hasta', filtros.fecha_hasta)
        }
        
        const queryString = params.toString()
        const url = queryString ? `listar_ventas/?${queryString}` : 'listar_ventas/'
        
        const response = await api.get(url)
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
        const subtotal = precio * this.cantidad

        this.productosVenta.push({
          producto: { ...this.selectedProduct },
          cantidad: this.cantidad,
          total: Number(subtotal.toFixed(2))
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
        const subtotal = precio * item.cantidad
        item.total = Number(subtotal.toFixed(2))
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
        // Se mantiene en la pestaña de Crear Venta
        await this.listarVentas()
      } catch (error) {
        console.error('Error creando venta:', error)
        alert('No fue posible crear la venta. Revise la consola para más detalles.')
      } finally {
        this.loadingCreate = false
      }
    },

    // Métodos de transacción
    onTransaccion() {
      if (this.productosVenta.length === 0) {
        alert('Debe agregar al menos un producto a la venta para calcular la transacción')
        return
      }
      this.showModalTransaccion = true
      this.importeRecibido = 0
      // Enfocar automáticamente el campo de importe recibido
      this.$nextTick(() => {
        const modal = this.$el.querySelector('.fixed.inset-0')
        if (modal) {
          const input = modal.querySelector('input[type="number"]')
          if (input) {
            input.focus()
            input.select()
          }
        }
      })
    },

    calcularCambio() {
      // El cálculo se realiza automáticamente en la computed property cambioCalculado
      // Este método se mantiene para el @input en el template
    },

    cerrarModalTransaccion() {
      this.showModalTransaccion = false
      this.importeRecibido = 0
    },

    async confirmarTransaccion() {
      if (this.cambioCalculado < 0) {
        alert('El importe recibido es insuficiente para cubrir el total de la venta')
        return
      }

      // Cerrar modal y proceder con la venta
      this.cerrarModalTransaccion()
      
      // Configurar la venta como completada con pago en efectivo
      this.estadoVenta = 'COMPLETADA'
      this.metodoPago = 'EFECTIVO'
      
      // Guardar la venta automáticamente
      await this.crearVenta()
    },

    // Métodos de filtros de fecha independientes
    aplicarFiltroDia() {
      if (this.filtroDia) {
        // Limpiar otros filtros
        this.filtroMes = ''
        this.filtroAnio = ''
        
        // Aplicar filtro por día
        this.listarVentas({
          fecha_desde: this.filtroDia,
          fecha_hasta: this.filtroDia
        })
        this.filtroActual = `Día: ${this.filtroDia}`
      } else {
        this.listarVentas()
        this.filtroActual = 'Todas las ventas'
      }
    },

    aplicarFiltroMes() {
      if (this.filtroMes) {
        // Limpiar otros filtros
        this.filtroDia = ''
        this.filtroAnio = ''
        
        // Calcular rango del mes
        const [anio, mes] = this.filtroMes.split('-')
        const primerDia = `${anio}-${mes}-01`
        const ultimoDia = new Date(parseInt(anio), parseInt(mes), 0).toISOString().split('T')[0]
        
        // Aplicar filtro por mes
        this.listarVentas({
          fecha_desde: primerDia,
          fecha_hasta: ultimoDia
        })
        this.filtroActual = `Mes: ${mes}/${anio}`
      } else {
        this.listarVentas()
        this.filtroActual = 'Todas las ventas'
      }
    },

    aplicarFiltroAnio() {
      if (this.filtroAnio) {
        // Limpiar otros filtros
        this.filtroDia = ''
        this.filtroMes = ''
        
        // Aplicar filtro por año
        this.listarVentas({
          fecha_desde: `${this.filtroAnio}-01-01`,
          fecha_hasta: `${this.filtroAnio}-12-31`
        })
        this.filtroActual = `Año: ${this.filtroAnio}`
      } else {
        this.listarVentas()
        this.filtroActual = 'Todas las ventas'
      }
    },

    limpiarFiltros() {
      this.filtroDia = ''
      this.filtroMes = ''
      this.filtroAnio = ''
      this.listarVentas()
      this.filtroActual = 'Todas las ventas'
    },

    filtrarHoy() {
      // Obtener fecha actual en formato YYYY-MM-DD
      const hoy = new Date().toISOString().split('T')[0]
      
      // Limpiar otros filtros
      this.filtroDia = hoy
      this.filtroMes = ''
      this.filtroAnio = ''
      
      // Aplicar filtro del día actual
      this.listarVentas({
        fecha_desde: hoy,
        fecha_hasta: hoy
      })
      this.filtroActual = `Hoy: ${hoy}`
    },

    // Métodos para obtener nombres de usuario y cliente
    obtenerNombreUsuario(usuario) {
      if (!usuario) return 'Sin vendedor'
      
      // El usuario puede ser un objeto o un ID
      if (typeof usuario === 'object') {
        // Intentar obtener el nombre completo
        if (usuario.first_name && usuario.last_name) {
          return `${usuario.first_name} ${usuario.last_name}`
        }
        if (usuario.first_name) {
          return usuario.first_name
        }
        if (usuario.username) {
          return usuario.username
        }
        if (usuario.email) {
          return usuario.email
        }
        return 'Usuario desconocido'
      }
      
      // Si es un ID, buscar en la lista de usuarios cargados
      const usuarioEncontrado = this.usuarios.find(u => u.id === usuario)
      if (usuarioEncontrado) {
        if (usuarioEncontrado.first_name && usuarioEncontrado.last_name) {
          return `${usuarioEncontrado.first_name} ${usuarioEncontrado.last_name}`
        }
        if (usuarioEncontrado.first_name) {
          return usuarioEncontrado.first_name
        }
        if (usuarioEncontrado.username) {
          return usuarioEncontrado.username
        }
        if (usuarioEncontrado.email) {
          return usuarioEncontrado.email
        }
        return `Usuario #${usuarioEncontrado.id}`
      }
      
      return `Usuario #${usuario}`
    },

    obtenerNombreCliente(cliente) {
      if (!cliente) return 'Sin cliente'
      
      // El cliente puede ser un objeto o un ID
      if (typeof cliente === 'object') {
        // Intentar obtener el nombre completo
        if (cliente.nombre) {
          return cliente.nombre
        }
        if (cliente.first_name && cliente.last_name) {
          return `${cliente.first_name} ${cliente.last_name}`
        }
        if (cliente.first_name) {
          return cliente.first_name
        }
        if (cliente.email) {
          return cliente.email
        }
        return `Cliente #${cliente.id}`
      }
      
      // Si es un ID, buscar en la lista de clientes cargados
      const clienteEncontrado = this.clientes.find(c => c.id === cliente)
      if (clienteEncontrado) {
        return clienteEncontrado.nombre || clienteEncontrado.first_name || `Cliente #${clienteEncontrado.id}`
      }
      
      return `Cliente #${cliente}`
    }
  }
}
</script>
