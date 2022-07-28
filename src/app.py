from typing import List


def integer_sum(first_number: int, second_number: int) -> int:
    return first_number + second_number


def fizz_buzz(number: int) -> List:
    result = []
    start = 1
    for i in range(start, number):
        if i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        elif i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        else:
            result.append(i)
    return result
