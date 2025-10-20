from sqlalchemy import Column, Integer, String, Boolean, Date
from sqlalchemy.orm import relationship #pour créer les liens entre les modèles
from database import Base 

class Tache(Base): # indique à sqlalchemy que Tache est une table de ma bdd
    __tablename__ = "taches"

    id = Column(Integer, primary_key=True, index=True)
    
    titre = Column(String(50), unique=True, index=True) 
    
    description = Column(String(255))
    
    date_creation = Column(Date) 
    
    achevee = Column(Boolean, default=False)
    
    def __repr__(self): #définit comment l'objet sera affiché dans la console (optionnel mais utile)
        return f"<Tache(id={self.id}, titre='{self.titre}', achevee={self.achevee})>"
    

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    
    email = Column(String(100), unique=True, index=True, nullable=False)
    
    hashed_password = Column(String, nullable=False)
    
    is_active = Column(Boolean, default=True) 

    def __repr__(self):
        return f"<User(email='{self.email}', is_active={self.is_active})>"