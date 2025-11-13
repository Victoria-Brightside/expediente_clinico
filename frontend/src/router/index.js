import { createRouter, createWebHistory } from 'vue-router'

// Importamos las vistas con rutas exactas
import UploadView from '../views/UploadView.vue'
import EditView from '../views/EditView.vue'
import HomeView from '../views/HomeView.vue'
import PatientsView from '../views/PatientsView.vue'
import PatientDetailView from '../views/PatientDetailView.vue' // 👈 Nueva vista

const routes = [
  { path: '/', component: HomeView },
  { path: '/upload', component: UploadView },
  { path: '/patients', component: PatientsView },
  // 👇 Nueva ruta dinámica para detalle de paciente
  { 
    path: '/patients/:id', 
    name: 'PatientDetail', 
    component: PatientDetailView, 
    props: true 
  },
  { path: '/edit', component: EditView },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
