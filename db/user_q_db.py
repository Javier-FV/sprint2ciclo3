from typing import Dict
from pydantic import BaseModel
from models.userq import Userq

    

database_users_q = Dict[str, Userq]
database_users_q = {
    "JavierFV": Userq(**{"username":"JavierFV",
                            "question1":1,
                            "question2":2,
                            "question3":3,
                            "question4":4,
                            "question5":5,
                            "question6":6,
                            "question7":7,
                            "question8":8,
                            "question9":9,
                            "question10":10,
                            "question11":11,
                            "question12":12
                                                 }),
    "Alvarado5": Userq(**{"username":"Alvarado5",
                            "question1":1,
                            "question2":2,
                            "question3":3,
                            "question4":4,
                            "question5":5,
                            "question6":6,
                            "question7":7,
                            "question8":8,
                            "question9":9,
                            "question10":10,
                            "question11":11,
                            "question12":12
                            }),
}

def get_user_q(username: str):
    if username in database_users_q.keys():
        return database_users_q[username]
    else:
        return None

def set_user_q(userq_in_db:Userq):
    database_users_q[userq_in_db.username]=userq_in_db
    return userq_in_db



