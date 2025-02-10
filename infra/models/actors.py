from infra.configs.base import Base

from sqlalchemy import Column, String, Integer, ForeignKey


class Actors(Base):
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)

    # Relationship with movies table
    movie_title = Column(String(255), ForeignKey('movies.title'), nullable=False)

    def __repr__(self):
        return f'Actor(id={self.id}, name="{self.name}", movie_title="{self.movie_title}")'
