from sqlalchemy import Column, Integer, String, ForeignKey
from src.models.postgres.settings.base import Base


class PeopleTable(Base):
    __tablename__ = "people"

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    pet_id = Column(Integer, ForeignKey("pets.id"))

    def __repr__(self):
        return f"<PeopleTable(id={self.id}, first_name={self.first_name}, last_name={self.last_name}, age={self.age}, pet_id={self.pet_id})>"
