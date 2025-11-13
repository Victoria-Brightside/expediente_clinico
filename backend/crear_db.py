from pymongo import MongoClient

# Conexión a MongoDB local
client = MongoClient("mongodb://localhost:27017/")

# Nombre de la base de datos
db = client["expediente_medico"]

# Colección donde guardaremos las notas
notas_collection = db["notas_medicas"]

# Documento de ejemplo basado en tus etiquetas
nota_ejemplo = {
    "Fecha": "2025-11-13",
    "Hora": "12:30",
    "Nombres": "Juan",
    "Apellidos": "Pérez",
    "Edad": 35,
    "Sexo": "Masculino",
    "Padecimiento actual": "Dolor de rodilla",
    "Antecedentes personales patológicos": "Hipertensión",
    "Antecedentes personales no patológicos": "No fuma",
    "Antecedentes heredofamiliares": "Diabetes",
    "Exploración física": "Rodilla derecha inflamada",
    "Resultados de laboratorio": "Normal",
    "Estudios de imagenología": "Radiografía normal",
    "Diagnóstico": "Esguince leve",
    "Pronóstico": "Recuperación completa",
    "Tratamiento": "Reposo y antiinflamatorios",
    "Médico tratante": "Dr. Victoria Bernal",
    "Especialidad": "Ortopedia"
}

# Insertar el documento de ejemplo
resultado = notas_collection.insert_one(nota_ejemplo)
print(f"Documento insertado con ID: {resultado.inserted_id}")
