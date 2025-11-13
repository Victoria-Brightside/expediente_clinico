<template>
  <div>
    <h2>Vista previa:</h2>
    <div v-for="(section, index) in data" :key="index">
      <h3>{{ section.title }}</h3>
      <p>{{ section.content }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Preview',
  props: ['data']
};
</script>
