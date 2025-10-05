
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from contextlib import asynccontextmanager
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

@app.get("/")
async def root():
    return {"message": "Bienvenue sur l'API To-Do List"}

@app.post("/taches/", response_model=schemas.Tache)
async def create_tache_for_user(
    tache: schemas.TacheCreate, 
    db: AsyncSession = Depends(get_db) 
):
    return await crud.create_tache(db=db, tache=tache)

@app.get("/taches/", response_model=List[schemas.Tache])
async def read_taches(db: AsyncSession = Depends(get_db)):
    taches = await crud.get_taches(db=db)
    return taches

@app.put("/taches/{tache_id}", response_model=schemas.Tache)
async def update_existing_tache(
    tache_id: int, 
    tache: schemas.TacheCreate, 
    db: AsyncSession = Depends(get_db)
):
    db_tache = await crud.update_tache(db, tache_id=tache_id, tache_update=tache)
    if db_tache is None:
        raise HTTPException(status_code=404, detail="Tâche non trouvée")
    return db_tache

@app.delete("/taches/{tache_id}", status_code=204) # 204 = No Content, succès sans corps
async def delete_existing_tache(tache_id: int, db: AsyncSession = Depends(get_db)):
    success = await crud.delete_tache(db, tache_id=tache_id)
    if not success:
        raise HTTPException(status_code=404, detail="Tâche non trouvée")
    return 

@app.get("/taches/{tache_id}", response_model=schemas.Tache)
async def read_tache_by_id(tache_id: int, db: AsyncSession = Depends(get_db)):
    db_tache = await crud.get_tache_by_id(db, tache_id=tache_id)
    if db_tache is None:
        raise HTTPException(status_code=404, detail="Tâche non trouvée")
    return db_tache




