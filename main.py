
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from contextlib import asynccontextmanager
import auth
import crud
import models
import schemas
import database
engine = database.engine
Base = database.Base
get_db = database.get_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Démarrage de l'application...")
    async with database.engine.begin() as conn:
        await conn.run_sync(database.Base.metadata.create_all)
    yield 
    print("Arrêt de l'application...")

app = FastAPI(title="To-Do List", lifespan=lifespan)

#Création d'un utilisateur (Inscription)
@app.post("/users/", response_model=schemas.User)

async def create_new_user(user: schemas.UserCreate, db: AsyncSession = Depends(get_db)):
    db_user = await crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="L'email est déjà enregistré")
    return await crud.create_user(db=db, user=user)


@app.post("/token", response_model=schemas.Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), # FastAPI fournit un formulaire pour login/password
    db: AsyncSession = Depends(get_db)
):
    # Tenter de récupérer l'utilisateur par son nom d'utilisateur (email)
    user = await crud.get_user_by_email(db, email=form_data.username)
    
    # Vérifier l'utilisateur et le mot de passe
    if not user or not crud.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Nom d'utilisateur ou mot de passe incorrect",
            headers={"WWW-Authenticate": "Bearer"},
        )
        
    # Créer le Jeton JWT
    access_token = auth.create_access_token(
        data={"email": user.email}
    )
    
    return {"access_token": access_token, "token_type": "bearer"}



@app.get("/") 
async def root():
    return {"message": "Bienvenue sur l'API To-Do List"}

#créer une tâche
@app.post("/taches/", response_model=schemas.Tache)

async def create_tache_for_user(
    tache: schemas.TacheCreate, #pour valider avec pydantic
    db: AsyncSession = Depends(get_db),
    current_user: schemas.User = Depends(auth.get_current_user) # AJOUT DE LA PROTECTION
):
    return await crud.create_tache(db=db, tache=tache)

#lire toutes les tâches
@app.get("/taches/", response_model=List[schemas.Tache])

async def read_taches(
    db: AsyncSession = Depends(get_db),
    current_user: schemas.User = Depends(auth.get_current_user) # AJOUT DE LA PROTECTION
):
    taches = await crud.get_taches(db=db)
    return taches

#lire une tâche par id
@app.get("/taches/{tache_id}", response_model=schemas.Tache)

async def read_tache_by_id(tache_id: int, db: AsyncSession = Depends(get_db), current_user: schemas.User = Depends(auth.get_current_user)):
    db_tache = await crud.get_tache_by_id(db, tache_id=tache_id)
    if db_tache is None:
        raise HTTPException(status_code=404, detail="Tâche non trouvée")
    return db_tache

#Mettre à jour une tâche
@app.put("/taches/{tache_id}", response_model=schemas.Tache)

async def update_existing_tache(
    tache_id: int,
    tache: schemas.TacheCreate, 
    db: AsyncSession = Depends(get_db),
    current_user: schemas.User = Depends(auth.get_current_user)
):
    db_tache = await crud.update_tache(db, tache_id=tache_id, tache_update=tache)
    if db_tache is None:
        raise HTTPException(status_code=404, detail="Tâche non trouvée")
    return db_tache

#Supprimer une tâche
@app.delete("/taches/{tache_id}", status_code=204) 
async def delete_existing_tache(
    tache_id: int, 
    db: AsyncSession = Depends(get_db),
    current_user: schemas.User = Depends(auth.get_current_user) # Protection
):
    success = await crud.delete_tache(db, tache_id=tache_id)
    if not success:
        raise HTTPException(status_code=404, detail="Tâche non trouvée")
    return


