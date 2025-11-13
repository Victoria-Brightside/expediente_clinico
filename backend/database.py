from pymongo import MongoClient

# Conexión a MongoDB local
client = MongoClient("mongodb://127.0.0.1:27017/")
db = client["expediente_medico"]       # ← aquí la base correcta
notas_collection = db["notas_medicas"] # ← aquí la colección correcta
