<template>
  <div class="p-6 max-w-4xl mx-auto">
    <router-link to="/patients" class="text-blue-600 hover:underline">← Volver</router-link>
    <h1 class="text-2xl font-bold mb-4">{{ paciente?.Nombres }} {{ paciente?.Apellidos }}</h1>
    <p class="mb-4 text-gray-600">Diagnóstico: {{ paciente?.Diagnóstico }}</p>

    <h2 class="text-xl font-semibold mb-2">Notas médicas</h2>

    <ul v-if="notas.length" class="space-y-3">
      <li
        v-for="nota in notas"
        :key="nota._id.$oid"
        class="p-3 border rounded shadow-sm"
      >
        <p><strong>Fecha:</strong> {{ nota.Fecha }} {{ nota.Hora }}</p>
        <div v-for="(valor, key) in nota" :key="key" v-if="key !== '_id' && key !== 'Nombres' && key !== 'Apellidos' && key !== 'Fecha' && key !== 'Hora'">
          <strong>{{ key }}:</strong> {{ valor }}
        </div>
      </li>
    </ul>

    <p v-else class="text-gray-500">No hay notas registradas para este paciente.</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'

const route = useRoute()
const pacienteId = route.params.id

const paciente = ref(null)
const notas = ref([])

// Traer todas las notas y filtrar por paciente
onMounted(async () => {
  try {
    const res = await axios.get('http://127.0.0.1:8000/notas_medicas')
    const todasNotas = res.data

    // Filtrar por paciente usando el id
    notas.value = todasNotas.filter(nota => nota._id.$oid === pacienteId)

    if (notas.value.length > 0) {
      paciente.value = {
        Nombres: notas.value[0].Nombres,
        Apellidos: notas.value[0].Apellidos,
        Diagnóstico: notas.value[0].Diagnóstico
      }
    }
  } catch (error) {
    console.error('Error al cargar notas:', error)
  }
})
</script>
