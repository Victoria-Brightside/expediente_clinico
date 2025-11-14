<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios'

const route = useRoute()
const router = useRouter()
const nota = ref(null)
const pacienteId = route.params.id
const noteId = route.params.noteId

// Traer nota completa
onMounted(async () => {
  try {
    const res = await axios.get(`http://127.0.0.1:8000/notas/${noteId}`)
    nota.value = res.data
  } catch (error) {
    console.error('Error al cargar la nota:', error)
  }
})
</script>

<template>
  <div class="p-6 max-w-4xl mx-auto">
    <router-link :to="{ name: 'PatientDetail', params: { id: pacienteId } }" 
                 class="text-blue-600 hover:underline">← Volver</router-link>

    <h1 class="text-2xl font-bold mb-4">
      Nota de {{ nota?.Nombres }} {{ nota?.Apellidos }}
    </h1>

    <div v-if="nota">
      <p><strong>Fecha:</strong> {{ nota.Fecha }} {{ nota.Hora }}</p>
      <p><strong>Diagnóstico:</strong> {{ nota.Diagnóstico }}</p>
      <p><strong>Padecimiento actual:</strong> {{ nota['Padecimiento actual'] }}</p>
      <p><strong>Antecedentes personales patológicos:</strong> {{ nota['Antecedentes personales patológicos'] }}</p>
      <p><strong>Tratamiento:</strong> {{ nota.Tratamiento }}</p>
      <p><strong>Médico tratante:</strong> {{ nota['Médico tratante'] }}</p>
      <p><strong>Especialidad:</strong> {{ nota.Especialidad }}</p>
      <!-- Agrega aquí los campos que quieras mostrar completos -->
    </div>

    <p v-else class="text-gray-500">Cargando nota...</p>
  </div>
</template>
