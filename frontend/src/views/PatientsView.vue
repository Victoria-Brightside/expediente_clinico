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
        class="border rounded-lg p-4 shadow-sm hover:shadow-md transition"
      >
        <p>
          <strong>Nombre:</strong>
          <router-link
            :to="{ name: 'PatientDetail', params: { id: paciente.PacienteId } }"
            class="text-blue-600 hover:underline"
          >
            {{ paciente.Nombres }} {{ paciente.Apellidos }}
          </router-link>
        </p>
        <p><strong>Diagnóstico:</strong> {{ paciente.Diagnóstico || 'N/A' }}</p>
        <p><strong>Fecha de consulta:</strong> {{ paciente.Fecha || 'N/A' }}</p>
      </li>
    </ul>

    <p v-else class="text-gray-500 text-center mt-4">
      No se encontraron pacientes con ese criterio.
    </p>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import axios from 'axios'

const pacientes = ref([])
const busqueda = ref('')

onMounted(async () => {
  try {
    const res = await axios.get('http://127.0.0.1:8000/pacientes')
    pacientes.value = res.data
  } catch (error) {
    console.error('Error al cargar pacientes:', error)
  }
})

// Filtrado por cualquier campo
const pacientesFiltrados = computed(() => {
  const texto = busqueda.value.toLowerCase().trim()
  if (!texto) return pacientes.value
  return pacientes.value.filter(paciente =>
    Object.values(paciente).some(valor =>
      valor && valor.toString().toLowerCase().includes(texto)
    )
  )
})
</script>
