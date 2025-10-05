from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
import models
import schemas
async def get_taches(db: AsyncSession, skip: int = 0, limit: int = 100):
    stmt = select(models.Tache).offset(skip).limit(limit)
    result = await db.execute(stmt)
    taches = result.scalars().all() 
    return list(taches)

async def create_tache(db: AsyncSession, tache: schemas.TacheCreate):
    db_tache = models.Tache(
        titre=tache.titre, 
        description=tache.description,
    )
        
    db.add(db_tache)  
    await db.commit()  
    await db.refresh(db_tache) 
    
    return db_tache

async def update_tache(db: AsyncSession, tache_id: int, tache_update: schemas.TacheCreate):
    db_tache = await get_tache_by_id(db, tache_id)
    
    if db_tache:
        update_data = tache_update.model_dump(exclude_unset=True) 
        for key, value in update_data.items():
            setattr(db_tache, key, value)
            
        await db.commit() 
        await db.refresh(db_tache)
        
    return db_tache

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