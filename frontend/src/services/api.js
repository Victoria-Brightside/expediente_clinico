import axios from 'axios'

const api = axios.create({
  baseURL: 'http://127.0.0.1:8000',
})

// Traer todas las notas
export const getNotas = async () => {
  const res = await api.get('/notas')
  return res.data
}

// Traer pacientes únicos a partir de notas
export const getPacientes = async () => {
  const notas = await getNotas()
  const pacientesMap = {}

  notas.forEach(nota => {
    const key = (nota.nombres || nota.Nombres || '') + '-' + (nota.apellidos || nota.Apellidos || '')
    if (!pacientesMap[key]) {
      pacientesMap[key] = {
        id: nota._id?.$oid || nota._id,
        nombres: nota.Nombres || nota.nombres || '',
        apellidos: nota.Apellidos || nota.apellidos || '',
        diagnostico: nota.Diagnóstico || nota.diagnostico || '',
        fecha: nota.Fecha || nota.fecha || '',
        notas: []
      }
    }
    pacientesMap[key].notas.push(nota)
  })

  return Object.values(pacientesMap)
}

// Traer nota por ID
export const getNotaById = async (id) => {
  const res = await api.get(`/notas/${id}`)
  return res.data
}

// Crear nueva nota
export const crearNota = async (nota) => {
  const res = await api.post('/notas', nota)
  return res.data
}

// Actualizar nota
export const actualizarNota = async (id, nota) => {
  const res = await api.put(`/notas/${id}`, nota)
  return res.data
}
