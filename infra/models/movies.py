from infra.configs.base import Base

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class Movies(Base):  
    __tablename__ = 'movies'

    title = Column(String(255), primary_key=True)
    genre = Column(String(128), nullable=False)
    year = Column(Integer, nullable=False)

    # Relationship with actors table
    actors = relationship('Actors', backref='actors', lazy='subquery')

    def __repr__(self):
        return f'Movie(title="{self.title}", genre="{self.genre}", year={self.year})'
