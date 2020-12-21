from pydantic import BaseModel
from datetime import datetime

class IngresoIn(BaseModel):
    Idingreso: str
class IngresoOut(BaseModel):
    Idingreso: str
    descripcion:str
    frecuencia:str
    valor:float
    estado:str
    categoria:str
    fecha_lanzamiento:datetime
    observaciones:str
 