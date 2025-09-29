import pytest
from app.operation import Operation


def test_addition_positive():
    a = 10.0
    b = 5.0
    expected_result = 15.0
    result = Operation.addition(a, b)
    assert result == expected_result


def test_addition_negative_numbers():
    a = -10.0
    b = -5.0
    expected_result = -15.0
    result = Operation.addition(a, b)
    assert result == expected_result


def test_addition_positive_negative():
    a = 10.0
    b = -5.0
    expected_result = 5.0
    result = Operation.addition(a, b)
    assert result == expected_result


def test_addition_with_zero():
    a = 10.0
    b = 0.0
    expected_result = 10.0
    result = Operation.addition(a, b)
    assert result == expected_result


def test_subtraction_positive():
    a = 10.0
    b = 5.0
    expected_result = 5.0
    result = Operation.subtraction(a, b)
    assert result == expected_result


def test_subtraction_negative_numbers():
    a = -10.0
    b = -5.0
    expected_result = -5.0
    result = Operation.subtraction(a, b)
    assert result == expected_result


def test_subtraction_positive_negative():
    a = 10.0
    b = -5.0
    expected_result = 15.0
    result = Operation.subtraction(a, b)
    assert result == expected_result


def test_subtraction_with_zero():
    a = 10.0
    b = 0.0
    expected_result = 10.0
    result = Operation.subtraction(a, b)
    assert result == expected_result


def test_multiplication_positive():
    a = 10.0
    b = 5.0
    expected_result = 50.0
    result = Operation.multiplication(a, b)
    assert result == expected_result


def test_multiplication_negative_numbers():
    a = -10.0
    b = -5.0
    expected_result = 50.0
    result = Operation.multiplication(a, b)
    assert result == expected_result


def test_multiplication_positive_negative():
    a = 10.0
    b = -5.0
    expected_result = -50.0
    result = Operation.multiplication(a, b)
    assert result == expected_result


def test_multiplication_with_zero():
    a = 10.0
    b = 0.0
    expected_result = 0.0
    result = Operation.multiplication(a, b)
    assert result == expected_result


def test_division_positive():
    a = 10.0
    b = 5.0
    expected_result = 2.0
    result = Operation.division(a, b)
    assert result == expected_result


def test_division_negative_numbers():
    a = -10.0
    b = -5.0
    expected_result = 2.0
    result = Operation.division(a, b)
    assert result == expected_result


def test_division_positive_negative():
    a = 10.0
    b = -5.0
    expected_result = -2.0
    result = Operation.division(a, b)
    assert result == expected_result


def test_division_with_zero_divisor():
    a = 10.0
    b = 0.0
    with pytest.raises(ValueError) as exc_info:
        Operation.division(a, b)
    assert str(exc_info.value) == "Division by zero is not allowed"


def test_division_with_zero_numerator():
    a = 0.0
    b = 5.0
    expected_result = 0.0
    result = Operation.division(a, b)
    assert result == expected_result


@pytest.mark.parametrize("calc_method, a, b, expected_exception", [
    (Operation.addition, '10', 5.0, TypeError),
    (Operation.subtraction, 10.0, '5', TypeError),
    (Operation.multiplication, '10', '5', TypeError),
    (Operation.division, 10.0, '5', TypeError),
])
def test_operations_invalid_input_types(calc_method, a, b, expected_exception):
    with pytest.raises(expected_exception):
        calc_method(a, b)


def test_power_positive():
    a = 2.0
    b = 2.0
    expected_result = 4.0
    result = Operation.power(a, b)
    assert result == expected_result