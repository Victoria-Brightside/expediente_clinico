<template>
  <div class="p-6 max-w-4xl mx-auto">
    <h1 class="text-2xl font-bold mb-4">Lista de Pacientes</h1>

    <input
      v-model="busqueda"
      type="text"
      placeholder="Buscar por cualquier campo..."
      class="w-full p-2 border border-gray-300 rounded mb-4"
    />

    <ul v-if="pacientesFiltrados.length" class="space-y-2">
      <li
        v-for="paciente in pacientesFiltrados"
        :key="paciente.PacienteId"
        class="border rounded-lg p-3 shadow-sm cursor-pointer transition-all duration-200 hover:bg-blue-200 hover:shadow-md flex items-center gap-6"
        @click="irADetalle(paciente.PacienteId)"
      >
        <!-- Icono de usuario -->
        <span class="text-xl">👤</span>

        <!-- Nombre -->
        <span class="flex-1 min-w-[180px] font-medium px-2">{{ paciente.Nombres }} {{ paciente.Apellidos }}</span>

        <!-- Diagnóstico -->
        <span class="flex-1 min-w-[180px] px-2">{{ paciente.Diagnóstico || 'N/A' }}</span>

        <!-- Fecha -->
        <span class="flex-1 min-w-[140px] text-right px-2">{{ paciente.Fecha || 'N/A' }}</span>
      </li>
    </ul>

    <p v-else class="text-gray-500 text-center mt-4">
      No se encontraron pacientes con ese criterio.
    </p>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const pacientes = ref([])
const busqueda = ref('')
const router = useRouter()

onMounted(async () => {
  try {
    const res = await axios.get('http://127.0.0.1:8000/pacientes')
    pacientes.value = res.data
  } catch (error) {
    console.error('Error al cargar pacientes:', error)
  }
})

const pacientesFiltrados = computed(() => {
  const texto = busqueda.value.toLowerCase().trim()
  if (!texto) return pacientes.value
  return pacientes.value.filter(paciente =>
    Object.values(paciente).some(valor =>
      valor && valor.toString().toLowerCase().includes(texto)
    )
  )
})

const irADetalle = (id) => {
  router.push({ name: 'PatientDetail', params: { id } })
}
</script>
