from fastapi import APIRouter, HTTPException
from db.ingreso_db import IngresoInDB
from typing import Dict
from db.ingreso_db import update_ingreso, get_ingreso, database_ingresos, verificador
from models.ingreso_models import IngresoIn, IngresoOut

import datetime
from fastapi import FastAPI
from fastapi import HTTPException
api = FastAPI()
from fastapi.middleware.cors import CORSMiddleware

router = APIRouter()
@router.api.get("/",)
def inicio():
    return "Registro de Ingresos"

@router.api.get("/users/all/{Lista de Ingresos}", response_model=Dict[str, IngresoInDB])
async def get_ingresos():
    return database_ingresos

@router.api.post("/users/user/data/create/{Registrar Ingreso}")      
async def update_ingreso(Idingreso: str, ingreso_in_db: IngresoInDB):
    ingreso_in_db2 = verificador(Idingreso) 
    if ingreso_in_db2 == None:
        database_ingresos[Idingreso] = ingreso_in_db
        return ingreso_in_db
    return {"El ingreso ya existe"}
    
@router.api.put("/users/user/data/update/{Actualizar Ingreso}")      
async def update_ingreso(Idingreso: str, ingreso_in_db: IngresoInDB):
    
    try:
        database_ingresos[Idingreso] = ingreso_in_db
        return database_ingresos[Idingreso]
    
    except:
        raise HTTPException(status_code=404, detail="No existe el usuario")
    return ingreso_in_db

@router.api.delete("/users/user/delete/{Eliminar Ingreso}")
async def delete_ingreso(Idingreso: str):
    
    try:
        del database_ingresos[Idingreso]
        return database_ingresos, {"El ingreso de referencia " + Idingreso + " ha sido Eliminado"}
    
    except:
        raise HTTPException(status_code=404, detail="El ingreso de referencia " + Idingreso +  " no existe")

