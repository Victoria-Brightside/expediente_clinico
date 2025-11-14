from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import notas_collection
from urllib.parse import unquote

app = FastAPI()

# Configuración CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # o tu frontend http://localhost:5173
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoint para listar pacientes únicos
@app.get("/pacientes")
def listar_pacientes():
    pacientes_dict = {}
    for nota in notas_collection.find():
        paciente_id = nota.get("PacienteId")  # usa el campo real de MongoDB
        if paciente_id not in pacientes_dict:
            pacientes_dict[paciente_id] = {
                "PacienteId": paciente_id,
                "Nombres": nota.get("Nombres"),
                "Apellidos": nota.get("Apellidos"),
                "Diagnóstico": nota.get("Diagnóstico"),
                "Fecha": nota.get("Fecha")
            }
    return list(pacientes_dict.values())


# Endpoint para traer todas las notas de un paciente
@app.get("/pacientes/{paciente_id}/notas")
def listar_notas_paciente(paciente_id: str):
    paciente_id = unquote(paciente_id)  # decodifica caracteres URL (%C3%A9 → é)
    notas = list(notas_collection.find({"PacienteId": paciente_id}))
    for nota in notas:
        nota["_id"] = str(nota["_id"])
    return notas

