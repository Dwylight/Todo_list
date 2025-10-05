from pydantic import BaseModel
from typing import Optional
from datetime import date

class TacheBase(BaseModel):
    titre: str
    description: str

    achevee: Optional[bool] = False

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "titre": "Terminer le projet FastAPI",
                    "description": "Implémenter les routes GET et POST et tester la connexion BDD.",
                    "achevee": False
                }
            ]
        }
    }

class TacheCreate(TacheBase):
    pass

class Tache(TacheBase):
    id: int
    date_creation: date
    
class Config:
        from_attributes = True 