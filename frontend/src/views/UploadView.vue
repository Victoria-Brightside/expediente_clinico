<template>
  <div>
    <h1>Subir documentos médicos</h1>
    <FileUploader />
  </div>
</template>

<script>
import FileUploader from '../components/FileUploader.vue';

export default {
  name: 'UploadView',
  components: { FileUploader },
};
</script>
