from pydantic import BaseModel
from typing import Optional
from datetime import date, time

class Nota(BaseModel):
    fecha: Optional[str]
    hora: Optional[str]
    nombres: str
    apellidos: str
    edad: Optional[int]
    sexo: Optional[str]
    padecimiento_actual: Optional[str]
    antecedentes_personales_pat: Optional[str]
    antecedentes_personales_no_pat: Optional[str]
    antecedentes_heredofamiliares: Optional[str]
    exploracion_fisica: Optional[str]
    resultados_laboratorio: Optional[str]
    estudios_imagenologia: Optional[str]
    diagnostico: Optional[str]
    pronostico: Optional[str]
    tratamiento: Optional[str]
    medico_tratante: Optional[str]
    especialidad: Optional[str]
