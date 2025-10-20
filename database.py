import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv() #test

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_async_engine(
    DATABASE_URL, 
    echo=True # pour afficher les requêtes SQL dans la console 
)

AsyncSessionLocal = sessionmaker(
    autocommit=False, #je pourrai valider moi même les changements
    autoflush=False,
    bind=engine, #liaison avec mon moteur de base de donnée
    class_=AsyncSession,
    expire_on_commit=False #pour garder les objets accessibles après le commit
)

Base = declarative_base()

async def get_db(): #fastapi l'appelle pour chaque requêtes, elle fournit une session
    async with AsyncSessionLocal() as db:
        yield db

