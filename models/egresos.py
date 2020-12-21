from pydantic import BaseModel
from datetime import datetime

class Egresos(BaseModel):
    Idegresos:int
    username:str
    descripcion:str
    frecuencia:str
    importe:float
    fecha_de_vencimiento:str
    estado:str
    categoria:str
    fecha_lanzamiento:str
    fecha_pago:str
    observaciones:str