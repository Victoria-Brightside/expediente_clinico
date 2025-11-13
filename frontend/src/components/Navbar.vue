<template>
  <nav class="navbar">
    <ul>
      <li><router-link to="/">Inicio</router-link></li>
      <li><router-link to="/upload">Subir documento</router-link></li>
      <li><router-link to="/patients">Mis pacientes</router-link></li>

      <li><router-link to="/edit/1">Editar documento</router-link></li>
    </ul>
  </nav>
</template>

<script>
export default {
  name: "Navbar",
};
</script>

<style scoped>
.navbar {
  background-color: #3498db;
  padding: 10px 20px;
}

.navbar ul {
  list-style: none;
  display: flex;
  gap: 15px;
  margin: 0;
  padding: 0;
}

.navbar a {
  color: white;
  text-decoration: none;
  font-weight: bold;
}

.navbar a:hover {
  text-decoration: underline;
}
</style>
