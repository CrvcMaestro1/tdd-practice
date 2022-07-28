from typing import List


def integer_sum(first_number: int, second_number: int) -> int:
    return first_number + second_number


class FizzBuzz:

    def run(self, number: int) -> List:
        result = []
        start = 1
        for num in range(start, number):
            if self.is_fizz(num):
                result.append("Fizz")
            elif self.is_buzz(num):
                result.append("Buzz")
            elif self.is_fizz_buzz(num):
                result.append("FizzBuzz")
            else:
                result.append(num)
        return result

    @staticmethod
    def is_fizz(number: int) -> bool:
        return number % 3 == 0

    @staticmethod
    def is_buzz(number: int) -> bool:
        return number % 5 == 0

    def is_fizz_buzz(self, number: int) -> bool:
        return self.is_fizz(number) and self.is_buzz(number)
