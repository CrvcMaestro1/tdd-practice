import pytest
from _pytest.fixtures import fixture

from src.login.login import Login
from unittest.mock import Mock


@pytest.fixture
def database() -> Mock:
    return Mock()


class TestLogin:
    @fixture(autouse=True)
    def setup(self, database):
        self.__database = database

    def test_user_and_passw_could_not_be_empty(self) -> None:
        login = Login(self.__database)
        username: str = ""
        password: str = ""

        with pytest.raises(ValueError, match='User and pass must not be empty'):
            login.login(username, password)

    def test_should_not_login_with_incorrect_credentials(self) -> None:
        login = Login(self.__database)
        username: str = "Wladimir"
        password: str = "JuniorDev"
        self.__database.get_password.return_value = "abcd1234"

        with pytest.raises(ValueError, match='User and pass incorrect'):
            login.login(username, password)
        self.__database.get_password.assert_called_once_with(username)

    def test_should_login_with_correct_credentials(self) -> None:
        login = Login(self.__database)
        username: str = "Wladimir"
        password: str = "JuniorDev"
        self.__database.get_password.return_value = "JuniorDev"

        login.login(username, password)
        self.__database.get_password.assert_called_once_with(username)
