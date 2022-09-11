# _*_ encoding: utf-8 _*_

from pytest_learning.bad_request_error import BadRequestError


def sum_values(first: int, second: int) -> int:
    __check_whether_is_a_valid_number(first)
    __check_whether_is_a_valid_number(second)

    return first + second


def subtract_values(first: int, second: int) -> int:
    __check_whether_is_a_valid_number(first)
    __check_whether_is_a_valid_number(second)

    return first - second


def divide_values(dividend: int, divider: int) -> float:
    if divider == 0:
        """ BadRequestError is used only for illustrate a custom exception. 
            In real life you should use ZeroDivisionError 
        """
        raise BadRequestError("Could not divide a value by 0")

    return dividend / divider


def multiply_values(first: int, second: int) -> int:
    __check_whether_is_a_valid_number(first)
    __check_whether_is_a_valid_number(second)

    return first * second


def __check_whether_is_a_valid_number(value):
    if type(value) not in [int, float]:
        raise ValueError("Value is not a valid number")


if __name__ == '__main__':
    try:
        divide_values(10, 0)
    except BadRequestError as exception:
        print(f"Exception caught is -> {exception}")
