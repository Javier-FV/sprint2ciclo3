from fastapi import APIRouter, HTTPException

from db.egre_db import EgresoInDb, database_egresos, get_egreso, set_egreso
from models.egresos import Egresos

router = APIRouter()

@router.post("/egresos")
def save_egresos(egresos: Egresos):
    try:
        egresos.Idegresos = max(database_egresos.keys()) + 1
        set_egreso(egresos)
        return get_egresos(egresos.username)
    except Exception:
        raise HTTPException(status_code=404, detail="No se pudo insertar")

@router.put('/egresos/{id}')
def update_egreso(id: str, egresos: Egresos):
    database_egresos[id] = egresos
    return get_egreso(egresos.username)

@router.get('/egresos/{username}')
def get_egresos(username: str): 
    egresos = {}
    for i in database_egresos:
        if database_egresos[i].username == username:
            egresos[i] = database_egresos[i]
    return egresos

@router.delete('/egresos/{Idegresos}')
def delete_egreso(Idegresos: str):
    try:
        del database_egresos[int(Idegresos)]
        return {"Egreso " + Idegresos + " Eliminado"}
    except:
        raise HTTPException(status_code=404, detail="Egreso no encontrado")

@router.get('/egresos/{id}')
def get_un_egreso(Idegresos: int):
    return get_egreso(database_egresos[Idegresos])