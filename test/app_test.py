import pytest

from src.app import integer_sum, fizz_buzz


@pytest.fixture
def fix() -> str:
    return "Fizz"


def test_integer_sum() -> None:
    expected_result = 4
    result = integer_sum(2, 2)
    assert result == expected_result


def test_fizz_buzz() -> None:
    expected_result = [1, 2, "Fizz", 4, "Buzz"]
    result = fizz_buzz(6)
    assert result == expected_result
