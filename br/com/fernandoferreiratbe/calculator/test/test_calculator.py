# _*_ encoding: utf-8 _*_

import pytest

from br.com.fernandoferreiratbe.calculator import calculator
from br.com.fernandoferreiratbe.calculator.exception.bad_request_error import BadRequestError


def test_sum_function_given_valid_numbers_should_sum_values_and_return_the_result_value():
    result = calculator.sum_values(2, 2)

    assert result == 4


def test_sum_function_given_invalid_number_should_raise_bad_request_exception():
    with pytest.raises(ValueError) as exception:
        calculator.sum_values("number", "another_number")


def test_divide_function_given_valid_values_should_divide_and_return_the_result_value():
    result = calculator.divide_values(10, 2)

    assert result == 5


def test_divide_function_given_invalid_value_for_divisor_should_raise_bad_request_error():
    with pytest.raises(BadRequestError) as exception:
        calculator.divide_values(10, 0)

