<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios'

const route = useRoute()
const router = useRouter()

const pacienteId = route.params.id
const noteId = route.params.noteId

const nota = ref({})
const modoEdicion = ref(false)

// Traer la nota específica al montar el componente
onMounted(async () => {
  try {
    const res = await axios.get(
      `http://127.0.0.1:8000/pacientes/${encodeURIComponent(pacienteId)}/notas`
    )
    const notas = res.data
    nota.value = notas.find(n => n._id === noteId) || {}
  } catch (error) {
    console.error('Error al cargar la nota:', error)
  }
})

// Alternar modo edición
const toggleEdicion = () => {
  modoEdicion.value = !modoEdicion.value
}

// Guardar cambios
const guardarNota = async () => {
  try {
    await axios.put(
      `http://127.0.0.1:8000/pacientes/${encodeURIComponent(pacienteId)}/notas/${noteId}`,
      nota.value
    )
    alert('Nota actualizada correctamente')
    modoEdicion.value = false
  } catch (error) {
    console.error('Error al guardar la nota:', error)
    alert('No se pudo guardar la nota')
  }
}
</script>

<template>
  <div class="p-6 max-w-4xl mx-auto">
    <router-link :to="{ name: 'PatientDetail', params: { id: pacienteId } }"
                 class="text-blue-600 hover:underline">
      ← Volver a notas
    </router-link>

    <h1 class="text-2xl font-bold mb-4">
      Nota de {{ nota.Nombres }} {{ nota.Apellidos }}
    </h1>

    <div class="mb-4">
      <button @click="modoEdicion ? guardarNota() : toggleEdicion()"
              class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700">
        {{ modoEdicion ? 'Guardar cambios' : 'Editar nota' }}
      </button>
    </div>

    <form v-if="nota._id" class="nota-form">
      <label>Fecha:</label>
      <input type="date" v-model="nota.Fecha" :disabled="!modoEdicion" />

      <label>Hora:</label>
      <input type="time" v-model="nota.Hora" :disabled="!modoEdicion" />

      <label>Diagnóstico:</label>
      <input type="text" v-model="nota.Diagnóstico" :disabled="!modoEdicion" />

      <label>Padecimiento actual:</label>
      <textarea v-model="nota['Padecimiento actual']" :disabled="!modoEdicion"></textarea>

      <label>Antecedentes personales patológicos:</label>
      <textarea v-model="nota['Antecedentes personales patológicos']" :disabled="!modoEdicion"></textarea>

      <label>Antecedentes personales no patológicos:</label>
      <textarea v-model="nota['Antecedentes personales no patológicos']" :disabled="!modoEdicion"></textarea>

      <label>Antecedentes heredofamiliares:</label>
      <textarea v-model="nota['Antecedentes heredofamiliares']" :disabled="!modoEdicion"></textarea>

      <label>Exploración física:</label>
      <textarea v-model="nota['Exploración física']" :disabled="!modoEdicion"></textarea>

      <label>Resultados de laboratorio:</label>
      <textarea v-model="nota['Resultados de laboratorio']" :disabled="!modoEdicion"></textarea>

      <label>Estudios de imagenología:</label>
      <textarea v-model="nota['Estudios de imagenología']" :disabled="!modoEdicion"></textarea>

      <label>Pronóstico:</label>
      <input type="text" v-model="nota.Pronóstico" :disabled="!modoEdicion" />

      <label>Tratamiento:</label>
      <textarea v-model="nota.Tratamiento" :disabled="!modoEdicion"></textarea>

      <label>Médico tratante:</label>
      <input type="text" v-model="nota['Médico tratante']" :disabled="!modoEdicion" />

      <label>Especialidad:</label>
      <input type="text" v-model="nota.Especialidad" :disabled="!modoEdicion" />
    </form>

    <p v-else class="text-gray-500">No se encontró la nota.</p>
  </div>
</template>

<style scoped>
/* Formulario de edición de nota */
.nota-form {
  display: grid;
  grid-template-columns: 200px 1fr; /* Label fijo, input flexible */
  gap: 1rem 2rem;
  align-items: start;
  max-width: 800px;
  margin: 0 auto;
}

.nota-form label {
  font-weight: 600;
  text-align: right;
  padding-top: 0.5rem;
}

.nota-form input,
.nota-form textarea {
  border: 1px solid #646cff;
  border-radius: 6px;
  padding: 0.5rem;
  width: 100%;
  background-color: #1a1a1a;
  color: #fff;
  font-family: inherit;
}

.nota-form textarea {
  resize: vertical;
  min-height: 3rem;
}

/* Campos deshabilitados */
.nota-form input:disabled,
.nota-form textarea:disabled {
  background-color: #2a2a2a;
  color: #aaa;
  border-color: #444;
}
</style>
