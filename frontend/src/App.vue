<script setup>
</script>

<template>
  <div id="app" class="min-h-screen bg-slate-50 text-slate-800 flex">
    <!-- Sidebar (desktop) -->
    <nav class="hidden md:flex md:flex-col md:w-64 md:shrink-0 border-r border-slate-200 bg-white/80 backdrop-blur">
      <div class="px-6 py-5 border-b border-slate-200">
        <h1 class="text-lg font-semibold tracking-tight text-slate-900">Semilleros</h1>
        <p class="text-xs text-slate-500">Panel</p>
      </div>
      <ul class="flex-1 p-4 space-y-1">
        <li><router-link to="/" class="block rounded-md px-3 py-2 text-sm text-slate-700 hover:bg-slate-100">Inicio</router-link></li>
        <li><router-link to="/productos" class="block rounded-md px-3 py-2 text-sm text-slate-700 hover:bg-slate-100">Productos</router-link></li>
        <li><router-link to="/usuarios" class="block rounded-md px-3 py-2 text-sm text-slate-700 hover:bg-slate-100">Usuarios</router-link></li>
        <li><router-link to="/ventas" class="block rounded-md px-3 py-2 text-sm text-slate-700 hover:bg-slate-100">Ventas</router-link></li>
        <li><router-link to="/compras" class="block rounded-md px-3 py-2 text-sm text-slate-700 hover:bg-slate-100">Compras</router-link></li>
        <li><router-link to="/inventario" class="block rounded-md px-3 py-2 text-sm text-slate-700 hover:bg-slate-100">Inventario</router-link></li>
        <li><router-link to="/reportes" class="block rounded-md px-3 py-2 text-sm text-slate-700 hover:bg-slate-100">Reportes</router-link></li>
      </ul>
      <div class="p-4 mt-auto text-xs text-slate-400">© Semilleros</div>
    </nav>

    <!-- Main content -->
    <div class="flex-1 flex flex-col">
      <!-- Top bar with compact nav (mobile) -->
      <header class="md:hidden sticky top-0 z-10 bg-white/80 backdrop-blur border-b border-slate-200">
        <div class="container-safe py-3">
          <div class="text-base font-semibold text-slate-900">Semilleros</div>
          <div class="mt-2 -mx-1 overflow-x-auto">
            <div class="flex gap-1 px-1 pb-1">
              <router-link to="/" class="whitespace-nowrap rounded-md px-3 py-1.5 text-xs text-slate-700 hover:bg-slate-100">Inicio</router-link>
              <router-link to="/productos" class="whitespace-nowrap rounded-md px-3 py-1.5 text-xs text-slate-700 hover:bg-slate-100">Productos</router-link>
              <router-link to="/usuarios" class="whitespace-nowrap rounded-md px-3 py-1.5 text-xs text-slate-700 hover:bg-slate-100">Usuarios</router-link>
              <router-link to="/ventas" class="whitespace-nowrap rounded-md px-3 py-1.5 text-xs text-slate-700 hover:bg-slate-100">Ventas</router-link>
              <router-link to="/compras" class="whitespace-nowrap rounded-md px-3 py-1.5 text-xs text-slate-700 hover:bg-slate-100">Compras</router-link>
              <router-link to="/inventario" class="whitespace-nowrap rounded-md px-3 py-1.5 text-xs text-slate-700 hover:bg-slate-100">Inventario</router-link>
              <router-link to="/reportes" class="whitespace-nowrap rounded-md px-3 py-1.5 text-xs text-slate-700 hover:bg-slate-100">Reportes</router-link>
            </div>
          </div>
        </div>
      </header>

      <main class="container-safe py-6">
        <router-view />
      </main>
    </div>
  </div>
</template>

<style>
/* Tailwind maneja el diseño. No CSS adicional aquí. */
</style>
