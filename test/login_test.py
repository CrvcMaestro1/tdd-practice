import pytest
from src.login.login import Login

class TestLogin:

    def test_user_and_passw_could_not_be_empty(self) -> None:
        login = Login()
        username: str = ""
        password: str = ""

        with pytest.raises(ValueError, match='User and pass must not be empty'):
            login.login(username, password)