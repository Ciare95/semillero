<template>
  <div class="space-y-8">
    <!-- Hero / Welcome -->
    <section class="card mb-8">
      <div class="flex items-start justify-between gap-4">
        <div>
          <h1 class="text-2xl font-semibold tracking-tight text-slate-900">
            Bienvenido a Semilleros
          </h1>
          <p class="mt-2 text-slate-600">
            Gestiona tu aplicación desde el panel. Usa el menú lateral o las acciones rápidas.
          </p>
        </div>
      </div>
      <div class="mt-4 flex flex-wrap gap-2">
        <router-link to="/productos" class="btn btn-primary">
          Ir a Productos
        </router-link>
        <router-link to="/reportes" class="btn btn-ghost">
          Ver Reportes
        </router-link>
      </div>
    </section>

    <!-- Quick actions -->
    <section>
      <h2 class="sr-only">Accesos rápidos</h2>
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
        <router-link
          to="/productos"
          class="group block rounded-xl border border-slate-200 bg-white p-4 shadow-sm hover:shadow-md transition"
        >
          <div class="flex items-center justify-between">
            <div class="flex items-center gap-3">
              <div class="h-9 w-9 rounded-lg bg-sky-50 text-sky-700 grid place-content-center">
                📦
              </div>
              <div>
                <div class="font-medium text-slate-900">Productos</div>
                <div class="text-sm text-slate-500">Gestiona catálogo y precios</div>
              </div>
            </div>
            <div class="text-slate-300 group-hover:text-slate-400">→</div>
          </div>
        </router-link>

        <router-link
          to="/usuarios"
          class="group block rounded-xl border border-slate-200 bg-white p-4 shadow-sm hover:shadow-md transition"
        >
          <div class="flex items-center justify-between">
            <div class="flex items-center gap-3">
              <div class="h-9 w-9 rounded-lg bg-emerald-50 text-emerald-700 grid place-content-center">
                👤
              </div>
              <div>
                <div class="font-medium text-slate-900">Usuarios</div>
                <div class="text-sm text-slate-500">Control de accesos</div>
              </div>
            </div>
            <div class="text-slate-300 group-hover:text-slate-400">→</div>
          </div>
        </router-link>

        <router-link
          to="/ventas"
          class="group block rounded-xl border border-slate-200 bg-white p-4 shadow-sm hover:shadow-md transition"
        >
          <div class="flex items-center justify-between">
            <div class="flex items-center gap-3">
              <div class="h-9 w-9 rounded-lg bg-indigo-50 text-indigo-700 grid place-content-center">
                🧾
              </div>
              <div>
                <div class="font-medium text-slate-900">Ventas</div>
                <div class="text-sm text-slate-500">Registra transacciones</div>
              </div>
            </div>
            <div class="text-slate-300 group-hover:text-slate-400">→</div>
          </div>
        </router-link>

        <router-link
          to="/compras"
          class="group block rounded-xl border border-slate-200 bg-white p-4 shadow-sm hover:shadow-md transition"
        >
          <div class="flex items-center justify-between">
            <div class="flex items-center gap-3">
              <div class="h-9 w-9 rounded-lg bg-amber-50 text-amber-700 grid place-content-center">
                🛒
              </div>
              <div>
                <div class="font-medium text-slate-900">Compras</div>
                <div class="text-sm text-slate-500">Abastecimiento y costos</div>
              </div>
            </div>
            <div class="text-slate-300 group-hover:text-slate-400">→</div>
          </div>
        </router-link>

        <router-link
          to="/inventario"
          class="group block rounded-xl border border-slate-200 bg-white p-4 shadow-sm hover:shadow-md transition"
        >
          <div class="flex items-center justify-between">
            <div class="flex items-center gap-3">
              <div class="h-9 w-9 rounded-lg bg-fuchsia-50 text-fuchsia-700 grid place-content-center">
                🏬
              </div>
              <div>
                <div class="font-medium text-slate-900">Inventario</div>
                <div class="text-sm text-slate-500">Existencias y movimientos</div>
              </div>
            </div>
            <div class="text-slate-300 group-hover:text-slate-400">→</div>
          </div>
        </router-link>

        <router-link
          to="/reportes"
          class="group block rounded-xl border border-slate-200 bg-white p-4 shadow-sm hover:shadow-md transition"
        >
          <div class="flex items-center justify-between">
            <div class="flex items-center gap-3">
              <div class="h-9 w-9 rounded-lg bg-rose-50 text-rose-700 grid place-content-center">
                📊
              </div>
              <div>
                <div class="font-medium text-slate-900">Reportes</div>
                <div class="text-sm text-slate-500">Indicadores y métricas</div>
              </div>
            </div>
            <div class="text-slate-300 group-hover:text-slate-400">→</div>
          </div>
        </router-link>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'Home',
}
</script>

<style scoped>
</style>
