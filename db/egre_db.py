from typing import Dict

from pydantic.main import BaseModel
from models.egresos import Egresos

class EgresoInDb(BaseModel):
    username: str
    descripcion: str
    frecuencia: str
    importe: str
    fecha_de_vencimiento: str
    estado: str
    categoria: str
    fecha_lanzamiento: str
    fecha_pago: str
    observaciones: str
    username: str

database_egresos = Dict[str,Egresos]

database_egresos = {
    1: Egresos(**{
        "Idegresos": 1  ,
        "descripcion":"Arriendo" ,
        "frecuencia":"mensual"  ,
        "importe":330.0   ,
        "fecha_de_vencimiento":"2020-12-01 23:59:59.000000" ,
        "estado":"realizado" ,
        "categoria":"Pagos Recurrentes",
        "fecha_lanzamiento":"2020-11-01 08:59:00.000000" ,
        "fecha_pago":"2020-12-01 00:00:00.000000",
        "observaciones":"Bueno" ,
        "username":"Jhon"
    }),
    2: Egresos(**{
        "Idegresos": 2,
        "descripcion": "Pago Electricidad",
        "frecuencia": "mensual",
        "importe": 75.0,
        "fecha_de_vencimiento": "2020-12-15 23:59:59.000000",
        "estado": "realizado",
        "categoria": "Pagos Recurrentes",
        "fecha_lanzamiento": "2020-11-01 09:00:00.000000",
        "fecha_pago": "2020-12-10 00:00:00.000000",
        "observaciones": "Bueno",
        "username": "camilo24"
    }),
    3: Egresos(**{
        "Idegresos": 3,
        "descripcion": "Pago Acueducto",
        "frecuencia": "mensual",
        "importe": 45.0,
        "fecha_de_vencimiento": "2020-12-10 23:59:59.000000",
        "estado": "realizado",
        "categoria": "Pagos Recurrentes",
        "fecha_lanzamiento": "2020-11-01 09:01:00.000000",
        "fecha_pago": "2020-12-10 00:00:00.000000",
        "observaciones": "Bueno",
        "username": "Jhon"
    }),
    4: Egresos(**{
        "Idegresos": 4,
        "descripcion": "Pago Acueducto",
        "frecuencia": "mensual",
        "importe": 45.0,
        "fecha_de_vencimiento": "2020-12-10 23:59:59.000000",
        "estado": "realizado",
        "categoria": "Pagos Recurrentes",
        "fecha_lanzamiento": "2020-11-01 09:01:00.000000",
        "fecha_pago": "2020-12-10 00:00:00.000000",
        "observaciones": "Bueno",
        "username": "Walther"
    }),
    5: Egresos(**{
        "Idegresos": 5,
        "descripcion": "Pago Acueducto",
        "frecuencia": "mensual",
        "importe": 70.0,
        "fecha_de_vencimiento": "2020-12-13 23:59:59.000000",
        "estado": "realizado",
        "categoria": "Pagos Recurrentes",
        "fecha_lanzamiento": "2020-11-01 09:01:00.000000",
        "fecha_pago": "2020-12-10 00:00:00.000000",
        "observaciones": "Bueno",
        "username": "camilo24"
    })
}


def get_egreso(Idegresos: int):
    if Idegresos in database_egresos.keys():
        return database_egresos[Idegresos]
    else:
        return None

def set_egreso(egreso_in_db: Egresos):
    database_egresos[egreso_in_db.Idegresos] = egreso_in_db
    return egreso_in_db

async def get_user_egresos(username: str):
    return username