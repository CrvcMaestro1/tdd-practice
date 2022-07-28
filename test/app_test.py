import pytest

from src.app import integer_sum, FizzBuzz


@pytest.fixture
def fix() -> str:
    return "Fizz"


def test_integer_sum() -> None:
    expected_result = 4
    result = integer_sum(2, 2)
    assert result == expected_result


class TestFizzBuzz:

    def test_fizz_buzz(self) -> None:
        expected_result = [1, 2, "Fizz", 4, "Buzz"]
        fiz_buzz = FizzBuzz()
        result = fiz_buzz.run(6)
        assert result == expected_result
