from datetime import datetime, timedelta
from typing import Any
from jose import JWTError, jwt 
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from starlette import status
import schemas 
import crud
from database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
import os

from dotenv import load_dotenv
load_dotenv()



# Configuration du JWT

SECRET_KEY = os.getenv("SECRET_KEY") # Clé secrète pour signer le jeton
ALGORITHM = "HS256" # Algorithme de hachage pour la signature
ACCESS_TOKEN_EXPIRE_MINUTES = 30 # Durée de validité du jeton 


#  Le Schéma de Sécurité OAuth2
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Fonctions de Création et Vérification du Jeton

def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        
    to_encode.update({"exp": expire}) 
    to_encode.update({"sub": data["email"]}) 
    
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM) # Signature du jeton
    return encoded_jwt

# 4. Fonction de Décodage et Récupération de l'Utilisateur

async def get_current_user(token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_db)):
    
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Impossible de valider les identifiants",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        # Décodage du jeton
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        
        # Récupération de l'identifiant (email)
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
            
        token_data = schemas.TokenData(email=email)
        
    except JWTError:
        raise credentials_exception
        
    # Vérification de l'utilisateur en BDD
    user = await crud.get_user_by_email(db, email=token_data.email)
    
    if user is None:
        raise credentials_exception
        
    return user