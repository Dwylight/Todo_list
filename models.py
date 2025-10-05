from sqlalchemy import Column, Integer, String, Boolean, Date
from database import Base 

class Tache(Base):
    __tablename__ = "taches"

    id = Column(Integer, primary_key=True, index=True)
    
    titre = Column(String(50), unique=True, index=True) 
    
    description = Column(String(255))
    
    date_creation = Column(Date) 
    
    achevee = Column(Boolean, default=False)
    
    def __repr__(self):
        return f"<Tache(titre='{self.titre}', achevee={self.achevee})>"
    