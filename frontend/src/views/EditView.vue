<template>
  <div>
    <h1>Editar nota médica</h1>

    <!-- Mostrar secciones editables -->
    <EditableParagraph
      v-for="(section, index) in note"
      :key="index"
      :label="section.title"
      v-model="section.content"
    />

    <!-- Botón para guardar cambios -->
    <button @click="saveNote">Guardar</button>

    <!-- Vista previa de la nota -->
    <Preview :data="note" />
  </div>
</template>

<script>
import EditableParagraph from '../components/EditableParagraph.vue';
import Preview from '../components/Preview.vue';
import axios from 'axios';

export default {
  name: 'EditView',
  components: { EditableParagraph, Preview },
  data() {
    return {
      note: [], // Aquí se almacenan las secciones de la nota médica
    };
  },
  created() {
    this.fetchNote();
  },
  methods: {
    // Traer los datos de la nota desde el backend
    async fetchNote() {
      try {
        const id = this.$route.params.id || 1; // por defecto 1 si no hay id
        const res = await axios.get(`http://localhost:8000/note/${id}`);
        this.note = res.data;
      } catch (err) {
        console.error('Error al cargar la nota:', err);
        alert('No se pudo cargar la nota médica.');
      }
    },

    // Guardar cambios en el backend
    async saveNote() {
      try {
        const id = this.$route.params.id || 1;
        await axios.post(`http://localhost:8000/note/${id}`, this.note);
        alert('Nota guardada correctamente');
      } catch (err) {
        console.error('Error al guardar la nota:', err);
        alert('No se pudo guardar la nota médica.');
      }
    },
  },
};
</script>

<style scoped>
h1 {
  color: #2c3e50;
  margin-bottom: 20px;
}

button {
  margin-top: 20px;
  padding: 10px 15px;
  background-color: #3498db;
  color: white;
  border: none;
  cursor: pointer;
}

button:hover {
  background-color: #2980b9;
}
</style>
