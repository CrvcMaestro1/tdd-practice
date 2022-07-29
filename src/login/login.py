from src.model.database_interface import DatabaseInterface


class Login:

    def __init__(self, database: DatabaseInterface):
        self.__database = database

    def login(self, username: str, password: str):
        if username == "" or password == "":
            raise ValueError("User and pass must not be empty")

        password_database = self.__database.get_password(username)
        if password_database != password:
            raise ValueError("User and pass incorrect")

