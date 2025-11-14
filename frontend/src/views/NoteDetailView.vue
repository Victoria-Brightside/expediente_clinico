<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios'
import Swal from 'sweetalert2'
import 'sweetalert2/dist/sweetalert2.min.css'

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
    const datos = { ...nota.value }
    delete datos._id  // Esto es importante

    await axios.put(
      `http://127.0.0.1:8000/pacientes/${encodeURIComponent(pacienteId)}/notas/${noteId}`,
      datos
    )

    Swal.fire({
      title: 'Nota actualizada',
      text: 'Los cambios se guardaron correctamente.',
      icon: 'success',
      background: '#1f2937',
      color: '#f9fafb',
      iconColor: '#10b981',
      confirmButtonColor: '#3b82f6',
      confirmButtonText: 'Aceptar',
      customClass: {
        popup: 'rounded-xl shadow-xl',
        confirmButton: 'px-4 py-2 rounded-lg font-semibold hover:bg-blue-600'
      }
    })

    modoEdicion.value = false

  } catch (error) {
    Swal.fire({
      title: 'Error al guardar',
      text: 'Hubo un problema actualizando la nota.',
      icon: 'error',
      background: '#1f2937',
      color: '#f9fafb',
      iconColor: '#ef4444',
      confirmButtonColor: '#3b82f6',
      customClass: {
        popup: 'rounded-xl shadow-xl',
        confirmButton: 'px-4 py-2 rounded-lg font-semibold hover:bg-blue-600'
      }
    })
  }
}
</script>

<template>
  <div class="p-6 max-w-4xl mx-auto">
    <router-link
      :to="{ name: 'PatientDetail', params: { id: pacienteId } }"
      class="text-blue-600 hover:underline"
    >
      ← Volver a notas
    </router-link>

    <h1 class="text-2xl font-bold mb-4">
      Nota de {{ nota.Nombres }} {{ nota.Apellidos }}
    </h1>

    <div class="mb-4">
 <button
  @click="modoEdicion ? guardarNota() : toggleEdicion()"
  class="px-5 py-2 rounded-xl font-semibold
         bg-[#124E66] hover:bg-[#1C6E88]
         text-white shadow-md transition-all"
>
  {{ modoEdicion ? 'Guardar cambios' : 'Editar nota' }}
</button>

    </div>

    <form
  v-if="nota._id"
  class="grid grid-cols-[200px_1fr] gap-x-6 gap-y-4 max-w-3xl mx-auto"
>
  <label class="font-semibold text-right pr-2 text-[#124E66] pt-2">Fecha:</label>
  <input
    type="date"
    v-model="nota.Fecha"
    :disabled="!modoEdicion"
    class="w-full px-3 py-2 rounded-lg bg-[#1b2f3a] text-gray-100 border
           border-teal-700 focus:outline-none focus:border-teal-500
           disabled:bg-gray-800 disabled:text-gray-400 disabled:border-gray-600
           transition-all duration-200 shadow-sm"
  />

  <label class="font-semibold text-right pr-2 text-[#124E66] pt-2">Hora:</label>
  <input
    type="time"
    v-model="nota.Hora"
    :disabled="!modoEdicion"
    class="w-full px-3 py-2 rounded-lg bg-[#1b2f3a] text-gray-100 border
           border-teal-700 focus:outline-none focus:border-teal-500
           disabled:bg-gray-800 disabled:text-gray-400 disabled:border-gray-600
           transition-all duration-200 shadow-sm"
  />

  <label class="font-semibold text-right pr-2 text-[#124E66] pt-2">Diagnóstico:</label>
  <input
    type="text"
    v-model="nota.Diagnóstico"
    :disabled="!modoEdicion"
    class="w-full px-3 py-2 rounded-lg bg-[#1b2f3a] text-gray-100 border
           border-teal-700 focus:outline-none focus:border-teal-500
           disabled:bg-gray-800 disabled:text-gray-400 disabled:border-gray-600"
  />

  <!-- Textareas -->

  <label class="font-semibold text-right pr-2 text-[#124E66] pt-2">Padecimiento actual:</label>
  <textarea
    v-model="nota['Padecimiento actual']"
    :disabled="!modoEdicion"
    class="w-full px-3 py-2 rounded-lg bg-[#1b2f3a] text-gray-100 border
           border-teal-700 focus:outline-none focus:border-teal-500
           disabled:bg-gray-800 disabled:text-gray-400 disabled:border-gray-600
           min-h-[3rem] resize-y"
  ></textarea>

  <label class="font-semibold text-right pr-2 text-[#124E66] pt-2">Antecedentes personales patológicos:</label>
  <textarea
    v-model="nota['Antecedentes personales patológicos']"
    :disabled="!modoEdicion"
    class="w-full px-3 py-2 rounded-lg bg-[#1b2f3a] text-gray-100 border
           border-teal-700 focus:outline-none focus:border-teal-500
           disabled:bg-gray-800 disabled:text-gray-400 disabled:border-gray-600
           min-h-[3rem] resize-y"
  ></textarea>

  <label class="font-semibold text-right pr-2 text-[#124E66] pt-2">Antecedentes personales no patológicos:</label>
  <textarea
    v-model="nota['Antecedentes personales no patológicos']"
    :disabled="!modoEdicion"
    class="w-full px-3 py-2 rounded-lg bg-[#1b2f3a] text-gray-100 border
           border-teal-700 focus:outline-none focus:border-teal-500
           disabled:bg-gray-800 disabled:text-gray-400 disabled:border-gray-600
           min-h-[3rem] resize-y"
  ></textarea>

  <label class="font-semibold text-right pr-2 text-[#124E66] pt-2">Antecedentes heredofamiliares:</label>
  <textarea
    v-model="nota['Antecedentes heredofamiliares']"
    :disabled="!modoEdicion"
    class="w-full px-3 py-2 rounded-lg bg-[#1b2f3a] text-gray-100 border
           border-teal-700 focus:outline-none focus:border-teal-500
           disabled:bg-gray-800 disabled:text-gray-400 disabled:border-gray-600
           min-h-[3rem] resize-y"
  ></textarea>

  <label class="font-semibold text-right pr-2 text-[#124E66] pt-2">Exploración física:</label>
  <textarea
    v-model="nota['Exploración física']"
    :disabled="!modoEdicion"
    class="w-full px-3 py-2 rounded-lg bg-[#1b2f3a] text-gray-100 border
           border-teal-700 focus:outline-none focus:border-teal-500
           disabled:bg-gray-800 disabled:text-gray-400 disabled:border-gray-600
           min-h-[3rem] resize-y"
  ></textarea>

  <label class="font-semibold text-right pr-2 text-[#124E66] pt-2">Resultados de laboratorio:</label>
  <textarea
    v-model="nota['Resultados de laboratorio']"
    :disabled="!modoEdicion"
    class="w-full px-3 py-2 rounded-lg bg-[#1b2f3a] text-gray-100 border
           border-teal-700 focus:outline-none focus:border-teal-500
           disabled:bg-gray-800 disabled:text-gray-400 disabled:border-gray-600
           min-h-[3rem] resize-y"
  ></textarea>

  <label class="font-semibold text-right pr-2 text-[#124E66] pt-2">Estudios de imagenología:</label>
  <textarea
    v-model="nota['Estudios de imagenología']"
    :disabled="!modoEdicion"
    class="w-full px-3 py-2 rounded-lg bg-[#1b2f3a] text-gray-100 border
           border-teal-700 focus:outline-none focus:border-teal-500
           disabled:bg-gray-800 disabled:text-gray-400 disabled:border-gray-600
           min-h-[3rem] resize-y"
  ></textarea>

  <label class="font-semibold text-right pr-2 text-[#124E66] pt-2">Pronóstico:</label>
  <input
    type="text"
    v-model="nota.Pronóstico"
    :disabled="!modoEdicion"
    class="w-full px-3 py-2 rounded-lg bg-[#1b2f3a] text-gray-100 border
           border-teal-700 focus:outline-none focus:border-teal-500
           disabled:bg-gray-800 disabled:text-gray-400 disabled:border-gray-600"
  />

  <label class="font-semibold text-right pr-2 text-[#124E66] pt-2">Tratamiento:</label>
  <textarea
    v-model="nota.Tratamiento"
    :disabled="!modoEdicion"
    class="w-full px-3 py-2 rounded-lg bg-[#1b2f3a] text-gray-100 border
           border-teal-700 focus:outline-none focus:border-teal-500
           disabled:bg-gray-800 disabled:text-gray-400 disabled:border-gray-600
           min-h-[3rem] resize-y"
  ></textarea>

  <label class="font-semibold text-right pr-2 text-[#124E66] pt-2">Médico tratante:</label>
  <input
    type="text"
    v-model="nota['Médico tratante']"
    :disabled="!modoEdicion"
    class="w-full px-3 py-2 rounded-lg bg-[#1b2f3a] text-gray-100 border
           border-teal-700 focus:outline-none focus:border-teal-500
           disabled:bg-gray-800 disabled:text-gray-400 disabled:border-gray-600"
  />

  <label class="font-semibold text-right pr-2 text-[#124E66] pt-2">Especialidad:</label>
  <input
    type="text"
    v-model="nota.Especialidad"
    :disabled="!modoEdicion"
    class="w-full px-3 py-2 rounded-lg bg-[#1b2f3a] text-gray-100 border
           border-teal-700 focus:outline-none focus:border-teal-500
           disabled:bg-gray-800 disabled:text-gray-400 disabled:border-gray-600"
  />
</form>


    <p v-else class="text-gray-500">No se encontró la nota.</p>
  </div>
</template>


