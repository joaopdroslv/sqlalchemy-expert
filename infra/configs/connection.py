from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound


class DBConnectionHandler:
    # Creating a context manager to manage our sessions
    def __init__(self):
        self.__connection_string = 'mysql+pymysql://root:admin123@localhost:3306/cinema'
        self.__engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine

    def get_engine(self):
        # Returns the engine if raw SQL statements are needed
        return self.__engine

    def __enter__(self):
        session_maker = sessionmaker(bind=self.__engine)
        self.session = session_maker()
        return self

    def __exit__(self, type, value, traceback):
        # We can handle our exception here, like:
        # if type is not None and issubclass(type, NoResultFound):
        #     return True  # Supress the exception
        # if type is not None:
        #     self.session.rollback()
        #     print('Something went wrong, rolling back!')

        self.session.close()

