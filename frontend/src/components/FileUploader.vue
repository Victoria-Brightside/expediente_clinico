<template>
  <div>
    <input type="file" multiple @change="handleFiles" />
    <button @click="uploadFiles">Subir archivos</button>
    <Loader v-if="loading" />
  </div>
</template>

<script>
import axios from 'axios';
import Loader from './Loader.vue';

export default {
  components: { Loader },
  data() {
    return {
      files: [],
      loading: false,
    };
  },
  methods: {
    handleFiles(event) {
      this.files = Array.from(event.target.files);
    },
    async uploadFiles() {
      if (!this.files.length) return;

      const formData = new FormData();
      this.files.forEach(file => formData.append('files', file));

      this.loading = true;
      try {
        const res = await axios.post('http://localhost:8000/upload', formData);
        console.log(res.data); // JSON procesado por backend
        alert('Archivos procesados correctamente');
      } catch (err) {
        console.error(err);
        alert('Error al procesar archivos');
      } finally {
        this.loading = false;
      }
    },
  },
};
</script>
