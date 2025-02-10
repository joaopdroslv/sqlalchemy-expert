from infra.repository.actors_repository import ActorsRepository
from infra.repository.movies_repository import MoviesRepository


actors_repo = ActorsRepository()

# records = actors_repo.select_with_movie_data()
# for record in records:
#     actor_name, movie_title, movie_genre = record
#     print(f'The actor/actress {actor_name} acted in the {movie_title} a(an) {movie_genre} genre movie.')


movies_repo = MoviesRepository()

movies = movies_repo.select()
print(movies[0].actors)

print(movies_repo.force_error())
