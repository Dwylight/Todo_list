from sqlalchemy.ext.asyncio import AsyncSession
from passlib.context import CryptContext
from datetime import date # Import ajouté
from sqlalchemy.future import select 
from sqlalchemy import update, delete

import models 
import schemas


#pour securiser le mot de passe (j'ai installé passlib)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

async def get_user_by_email(db: AsyncSession, email: str):
    #Récupère un utilisateur par email
    result = await db.execute(
        select(models.User).where(models.User.email == email)
    )
    return result.scalars().first()

async def create_user(db: AsyncSession, user: schemas.UserCreate):
    #pour créer un nouvel utilisateur avec un mot de passe haché
    safe_password = user.password[:72]

    hashed_password = get_password_hash(safe_password)
    
    db_user = models.User(
        email=user.email,
        hashed_password=hashed_password,
    )
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

# obtenir une tâche par son ID
async def get_taches_by_id(db: AsyncSession, tache_id: int):
    stmt = select(models.Tache).where(models.Tache.id == tache_id)
    result = await db.execute(stmt) #envoie la requête à la bdd
    return result.scalars().first() #selectionne uniquement les objets et non les lignes brutes

# obtenir toutes les tâches
async def get_taches(db: AsyncSession, skip: int = 0, limit: int = 100): #pagination optionnelle (skip/limit)
    stmt = select(models.Tache).offset(skip).limit(limit)    
    result = await db.execute(stmt)
    return list(result.scalars().all())

# créer une nouvelle tâche

async def create_tache(db: AsyncSession, tache: schemas.TacheCreate):
    db_tache = models.Tache(
        titre=tache.titre, 
        description=tache.description,
        achevee=tache.achevee,
        date_creation=date.today()
    )
    db.add(db_tache)  
    await db.commit()  
    await db.refresh(db_tache) #récupérer l'ID auto-généré par PostgreSQL en actualisant l'objet python
    return db_tache

#modifier une tâche existante
async def update_tache(db: AsyncSession, tache_id: int, tache_update: schemas.TacheCreate):
    db_tache = await get_tache_by_id(db, tache_id)
    if db_tache:
        update_data = tache_update.model_dump(exclude_unset=True) 
        for key, value in update_data.items():
            setattr(db_tache, key, value)
        # enregistrer les changements ds la bdd
        await db.commit() 
        await db.refresh(db_tache)
        return db_tache
    return None

# suppression d'une tâche
async def delete_tache(db: AsyncSession, tache_id: int):
    db_tache = await get_tache_by_id(db, tache_id)
    if db_tache:
        await db.delete(db_tache) 
        await db.commit()    
        return True 
    return False 

async def get_tache_by_id(db: AsyncSession, tache_id: int):
    result = await db.execute(
        select(models.Tache).where(models.Tache.id == tache_id)
    )
    return result.scalars().first()

