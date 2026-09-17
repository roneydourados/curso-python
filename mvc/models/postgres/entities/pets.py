from sqlalchemy import Column, Integer, String
from src.models.postgres.settings.base import Base

class PetsTable(Base):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)

    def __repr__(self):
        return f"<PetsTable(id={self.id}, name={self.name}, type={self.type})>"
