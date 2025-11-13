# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import notas_collection  # tu conexión a MongoDB

app = FastAPI(title="Backend Expediente Médico")

# ---- Configuración de CORS ----
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # permite cualquier origen (puedes restringirlo a tu frontend)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---- Endpoints ----

# Obtener todos los pacientes únicos
@app.get("/pacientes")
def listar_pacientes():
    pacientes_dict = {}
    for nota in notas_collection.find():
        key = (nota.get("Nombres"), nota.get("Apellidos"))
        if key not in pacientes_dict:
            pacientes_dict[key] = {
                "id": str(nota["_id"]),  # id único para cada paciente (tomamos el de la primera nota)
                "Nombres": nota.get("Nombres"),
                "Apellidos": nota.get("Apellidos"),
                "Diagnóstico": nota.get("Diagnóstico"),
                "Fecha": nota.get("Fecha")
            }
    return list(pacientes_dict.values())

# Obtener todas las notas médicas
@app.get("/notas_medicas")
def listar_notas():
    notas = []
    for nota in notas_collection.find():
        notas.append({
            "_id": {"$oid": str(nota["_id"])},
            "Fecha": nota.get("Fecha"),
            "Hora": nota.get("Hora"),
            "Nombres": nota.get("Nombres"),
            "Apellidos": nota.get("Apellidos"),
            "Diagnóstico": nota.get("Diagnóstico"),
            "Edad": nota.get("Edad"),
            "Sexo": nota.get("Sexo"),
            "Padecimiento actual": nota.get("Padecimiento actual"),
            "Antecedentes personales patológicos": nota.get("Antecedentes personales patológicos"),
            "Antecedentes personales no patológicos": nota.get("Antecedentes personales no patológicos"),
            "Antecedentes heredofamiliares": nota.get("Antecedentes heredofamiliares"),
            "Exploración física": nota.get("Exploración física"),
            "Resultados de laboratorio": nota.get("Resultados de laboratorio"),
            "Estudios de imagenología": nota.get("Estudios de imagenología"),
            "Pronóstico": nota.get("Pronóstico"),
            "Tratamiento": nota.get("Tratamiento"),
            "Médico tratante": nota.get("Médico tratante"),
            "Especialidad": nota.get("Especialidad"),
        })
    return notas
