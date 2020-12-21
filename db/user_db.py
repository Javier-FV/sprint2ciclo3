from typing import Dict
from pydantic import BaseModel
class UserInDB(BaseModel):
    username: str
    password: str
    nombre:str
    apellido:str
    correo:str
    ciudad:str
    edad:str
    estrato:str
    ocupacion:str
    estado_civil:str
    numero_hijos:str

database_users = Dict[str, UserInDB]
database_users = {
    "JavierFV": UserInDB(**{"username":"JavierFV",
                            "password":"root",
                            "nombre":"Javier",
                            "apellido":"Villamizar",
                            "correo":"javierfer_1998@hotmail.com",
                            "ciudad":"Bucaramanga",
                            "edad":"22",
                            "estrato":"3",
                            "ocupacion":"empleado",
                            "estado_civil":"soltero",
                            "numero_hijos":"0"}),
    "Alvarado5": UserInDB(**{"username":"Alvarado5",
                            "password":"hola",
                            "nombre":"Alvaro",
                            "apellido":"Alvarado",
                            "correo":"alvaalva@hotmail.com",
                            "ciudad":"Bogota",
                            "edad":"26",
                            "estrato":"4",
                            "ocupacion":"empleado",
                            "estado_civil":"casado",
                            "numero_hijos":"2"}),
}

def get_user(username: str):
    if username in database_users.keys():
        return database_users[username]
    else:
        return None

def verificador(username: str):
    if username in database_users.keys():
        return username
        print(username)
    else:
        return None
        print("None")
