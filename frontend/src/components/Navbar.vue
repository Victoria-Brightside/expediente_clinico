<template>
  <nav class="bg-[#124E66] text-white px-4 md:px-6 py-3 shadow-md">
    <div class="max-w-7xl mx-auto flex items-center justify-between">

      <!-- LEFT: Brand -->
      <div class="flex items-center space-x-3">
        <div class="text-2xl font-semibold tracking-wide select-none">
          OneFileMed
        </div>
      </div>

      <!-- MIDDLE / RIGHT: Desktop links + Login -->
      <div class="hidden md:flex items-center space-x-6">
        <router-link to="/" class="text-lg font-medium hover:text-teal-200 transition-colors">Inicio</router-link>
        <router-link to="/upload" class="text-lg font-medium hover:text-teal-200 transition-colors">Subir documento</router-link>
        <router-link to="/patients" class="text-lg font-medium hover:text-teal-200 transition-colors">Mis pacientes</router-link>

        <!-- Login button destacado -->
        <router-link
          to="/login"
          aria-label="Iniciar sesión"
          class="ml-2 inline-flex items-center gap-2 bg-white text-[#124E66] font-semibold px-4 py-2 rounded-lg shadow hover:shadow-lg transition-colors duration-200 hover:bg-gray-100"
        >
          <svg class="w-5 h-5" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
            <path d="M12 12c2.761 0 5-2.239 5-5s-2.239-5-5-5-5 2.239-5 5 2.239 5 5 5zM12 14c-4.418 0-8 1.79-8 4v2h16v-2c0-2.21-3.582-4-8-4z"/>
          </svg>
          Iniciar sesión
        </router-link>
      </div>

      <!-- MOBILE: hamburger -->
      <div class="md:hidden flex items-center">
        <button @click="open = !open" :aria-expanded="open" aria-label="Abrir menú"
                class="inline-flex items-center justify-center p-2 rounded-md text-white hover:bg-[rgba(255,255,255,0.08)] focus:outline-none focus:ring-2 focus:ring-white">
          <span v-if="!open" class="sr-only">Abrir menú</span>
          <span v-else class="sr-only">Cerrar menú</span>

          <!-- Iconos -->
          <svg v-if="!open" class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M4 6h16M4 12h16M4 18h16"></path>
          </svg>
          <svg v-else class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M6 18L18 6M6 6l12 12"></path>
          </svg>
        </button>
      </div>
    </div>

    <!-- MOBILE MENU -->
    <transition name="fade" enter-active-class="transition duration-150 ease-out" leave-active-class="transition duration-100 ease-in">
      <div v-if="open" class="md:hidden mt-2 px-4 pb-4 space-y-2">
        <router-link @click="open = false" to="/" class="block px-3 py-2 rounded-md text-base font-medium text-white hover:bg-[rgba(255,255,255,0.06)]">
          Inicio
        </router-link>
        <router-link @click="open = false" to="/upload" class="block px-3 py-2 rounded-md text-base font-medium text-white hover:bg-[rgba(255,255,255,0.06)]">
          Subir documento
        </router-link>
        <router-link @click="open = false" to="/patients" class="block px-3 py-2 rounded-md text-base font-medium text-white hover:bg-[rgba(255,255,255,0.06)]">
          Mis pacientes
        </router-link>

        <!-- Mobile login botón destacado -->
        <router-link
          @click="open = false"
          to="/login"
          class="mt-1 block w-full text-center bg-white text-[#124E66] font-semibold px-4 py-2 rounded-lg shadow hover:bg-gray-100"
        >
          <div class="inline-flex items-center justify-center gap-2">
            <svg class="w-5 h-5" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
              <path d="M12 12c2.761 0 5-2.239 5-5s-2.239-5-5-5-5 2.239-5 5 2.239 5 5 5zM12 14c-4.418 0-8 1.79-8 4v2h16v-2c0-2.21-3.582-4-8-4z"/>
            </svg>
            Iniciar sesión
          </div>
        </router-link>
      </div>
    </transition>
  </nav>
</template>

<script setup>
import { ref } from 'vue'
const open = ref(false)
</script>

<style scoped>
/* transición simple */
.fade-enter-from { opacity: 0; transform: translateY(-4px); }
.fade-enter-to   { opacity: 1; transform: translateY(0); }
.fade-leave-from { opacity: 1; transform: translateY(0); }
.fade-leave-to   { opacity: 0; transform: translateY(-4px); }
</style>
