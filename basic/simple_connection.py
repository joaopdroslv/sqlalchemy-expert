from sqlalchemy import create_engine, text


engine = create_engine('mysql+pymysql://root:admin123@localhost:3306/cinema')

# Opening a connection and executing a QUERY
# conn = engine.connect()  # Opens a connection
# movies = conn.execute(text('SELECT * FROM movies;'))

# This gives us the same result
with engine.connect() as conn:  # Using the engine.connect as a conext manager
    movies = conn.execute(text('SELECT * FROM movies;'))
    for movie in movies:
        # print(movie)
        print(f'{movie.title}, a(an) {movie.genre} movie from {movie.year}')
