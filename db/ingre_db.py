from typing import Dict
from pydantic import BaseModel
class IngresoInDB(BaseModel):
    Idingreso: str
    descripcion:str
    frecuencia:str
    valor:int
    estado:str
    categoria:str
    fecha_lanzamiento:str
    observaciones:str

database_ingresos = Dict[str, IngresoInDB]
database_ingresos = {
    "Ingreso01": IngresoInDB(**{"Idingreso":"Ingreso01",
                           "descripcion":"nomina" ,
                           "frecuencia":"mensual"  ,
                           "valor":990.0  ,
                           "estado":"realizado" ,
                           "categoria":"Ingresos Fijos",
                           "fecha_lanzamiento":"2020-12-14 10:00:00.000000" ,
                           "observaciones":"Ingresos generados por trabajo en compañía"}),
    "Ingreso02": IngresoInDB(**{"Idingreso":"Ingreso02",
                          "descripcion":"horas extras" ,
                          "frecuencia":"semanal"  ,
                          "valor":340.0   ,
                          "estado":"realizado" ,
                          "categoria":"Ingresos variables",
                          "fecha_lanzamiento":"2020-12-14 10:00:00.000000" ,
                          "observaciones":"Ingresos generados por trabajo semanal nocturno"}),
}

def get_ingreso(Idingreso: str):
    if Idingreso in database_ingresos.keys():
        return database_ingresos[Idingreso]
    else:
        return None

def verificador(Idingreso: str):
    if Idingreso in database_ingresos.keys():
        return Idingreso
        print(username)
    else:
        return None
        print("None")

def update_ingreso(ingreso_in_db: IngresoInDB,descripcion_in_db: IngresoInDB,
                frecuencia_in_db : IngresoInDB,valor_in_db: IngresoInDB,
                estado_in_db : IngresoInDB,categoria_in_db : IngresoInDB,
                fecha_lanzamiento_in_db : IngresoInDB,observaciones_in_db: IngresoInDB,
                ):
    database_ingresos[ingreso_in_db.Idingreso] = ingreso_in_db
    database_ingresos[descripcion_in_db.descripcion] = descripcion_in_db
    database_ingresos[frecuencia_in_db.frecuencia] = frecuencia_in_db
    database_ingresos[valor_in_db.valor] = valor_in_db
    database_ingresos[estado_in_db.estado] = estado_in_db
    database_ingresos[categoria_in_db.categoria] = categoria_in_db
    database_ingresos[fecha_lanzamiento_in_db.fecha_lanzamiento] = fecha_lanzamiento_in_db
    database_ingresos[observaciones_in_db.observaciones] = observaciones_in_db
    return ingreso_in_db