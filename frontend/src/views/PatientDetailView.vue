<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios'

const route = useRoute()
const router = useRouter()
const notas = ref([])
const paciente = ref({})
const pacienteId = route.params.id

onMounted(async () => {
  try {
    const res = await axios.get(`http://127.0.0.1:8000/pacientes/${encodeURIComponent(pacienteId)}/notas`)
    notas.value = res.data

    if (notas.value.length > 0) {
      paciente.value = {
        Nombres: notas.value[0].Nombres,
        Apellidos: notas.value[0].Apellidos
      }
    }
  } catch (error) {
    console.error('Error al cargar notas del paciente:', error)
  }
})

const verNota = (notaId) => {
  router.push({ name: 'NoteDetail', params: { id: pacienteId, noteId: notaId } })
}
</script>

<template>
  <div class="p-6 max-w-4xl mx-auto">
    <router-link to="/patients" class="text-blue-600 hover:underline">← Volver</router-link>

    <h1 class="text-2xl font-bold mb-4">
      Notas de {{ paciente.Nombres }} {{ paciente.Apellidos }}
    </h1>

    <ul v-if="notas.length" class="space-y-2">
      <li
        v-for="nota in notas"
        :key="nota._id"
        class="border rounded-lg p-3 shadow-sm cursor-pointer transition-all duration-200 hover:bg-blue-200 hover:shadow-lg flex items-center space-x-2"
        @click="verNota(nota._id)"
      >
        <span>📅 {{ nota.Fecha }}</span>
        <span>—</span>
        <span>{{ nota.Diagnóstico }}</span>
      </li>
    </ul>

    <p v-else class="text-gray-500">No hay notas registradas para este paciente.</p>
  </div>
</template>
