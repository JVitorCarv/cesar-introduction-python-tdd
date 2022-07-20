from src.calculator import *
import pytest


@pytest.mark.parametrize("nums, exp_res", [([2, 2, 3], 12), ([2, 6, 2, 5], 120), ([1], 1)])
def test_mult_with_multiple_arguments(nums, exp_res):
    c = Calculator()
    res = c.mult(*nums)
    assert res == exp_res


def test_mult_no_argument():
    c = Calculator()
    res = c.mult()
    assert res == 1


@pytest.mark.parametrize("nums", [[2, 0, 3], [0, 0, 0]])
def test_mult_with_zero_in_arguments(nums):
    with pytest.raises(MultError):
        c = Calculator()
        if type(nums) == int:
            c.mult(nums)
        else:
            c.mult(*nums)


def test_mult_with_single_0():
    with pytest.raises(MultError):
        c = Calculator()
        c.mult(0)


@pytest.mark.parametrize("param", ["Invalid", ["a", "b", "c"], [1, "a"]])
def test_mult_invalid_arguments(param):
    with pytest.raises(InvalidArgumentError):
        c = Calculator()
        c.mult(*param)


@pytest.mark.parametrize("structure", [[], (), {}, None, (1, 2), [1, 2]])
def test_mult_with_structures(structure):
    with pytest.raises(InvalidArgumentError):
        c = Calculator()
        c.mult(structure)
