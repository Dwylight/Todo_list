from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class TacheBase(BaseModel):
    titre: str = Field(min_length=1, max_length=50)
    description: str= Field(min_length=1, max_length=255)
    achevee: Optional[bool] = False

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "titre": "Aller au marché",
                    "description": "Acheter mes fournitures scolaires pour la rentrée",
                    "achevee": False
                }
            ]
        }
    } #ajout 'un exemple

class TacheCreate(TacheBase):
    pass

class Tache(TacheBase):
    id: int
    date_creation: date
    
class Config:
        from_attributes = True 

class UserCreate(BaseModel):
    email: str
    password: str = Field(min_length=8) #forcer la longueur minimale du mot de passe
class User(BaseModel):
    id: int
    email: str
    is_active: bool
    class Config:
        from_attributes = True

# Schéma pour la requête de Jeton 
# Utilisé par FastAPI pour la route 
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

# Schéma pour les données à l'intérieur du Jeton (Token Data)
class TokenData(BaseModel):
    email: str | None = None