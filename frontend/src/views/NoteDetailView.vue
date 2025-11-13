<template>
  <div class="p-6 max-w-3xl mx-auto">
    <router-link :to="`/pacients/${id}`" class="text-blue-600 hover:underline">← Volver</router-link>

    <h1 class="text-2xl font-bold mb-4">🩺 {{ nota.titulo }}</h1>
    <p class="text-gray-600 mb-2">Fecha: {{ formatFecha(nota.fecha) }}</p>

    <textarea
      v-model="nota.contenido"
      rows="12"
      class="w-full border rounded p-2 mb-4"
    ></textarea>

    <div class="flex gap-3">
      <button @click="guardarNota" class="bg-blue-600 text-white px-4 py-2 rounded">💾 Guardar</button>
      <button @click="imprimirNota" class="bg-gray-600 text-white px-4 py-2 rounded">🖨️ Vista previa</button>
    </div>

    <p v-if="mensaje" class="text-green-600 mt-3">{{ mensaje }}</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'

const route = useRoute()
const id = route.params.id
const noteId = route.params.noteId

const nota = ref({})
const mensaje = ref('')
const API_URL = 'http://localhost:8000'

onMounted(async () => {
  const res = await axios.get(`${API_URL}/patients/${id}/notes/${noteId}`)
  nota.value = res.data
})

const guardarNota = async () => {
  await axios.put(`${API_URL}/patients/${id}/notes/${noteId}`, nota.value)
  mensaje.value = '✅ Nota guardada correctamente.'
  setTimeout(() => mensaje.value = '', 2000)
}

const imprimirNota = () => {
  const ventana = window.open('', '_blank')
  ventana.document.write(`<pre>${nota.value.contenido}</pre>`)
  ventana.print()
}

const formatFecha = f => new Date(f).toLocaleDateString()
</script>
