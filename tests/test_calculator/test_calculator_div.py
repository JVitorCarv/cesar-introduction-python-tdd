from src.calculator import *
import pytest


@pytest.mark.parametrize("nums, exp_res", [([10, 5], 2), ([1, 2], 0.5), ([9, 3, 3], 1)])
def test_div_with_multiple_arguments(nums, exp_res):
    c = Calculator()
    res = c.div(*nums)
    assert res == exp_res


@pytest.mark.parametrize("nums", [0, [1, 2, 0]])
def test_div_with_0_in_argument(nums):
    c = Calculator()
    if type(nums) is list:
        res = c.div(*nums)
    else:
        res = c.div(nums)
    assert res == 0


@pytest.mark.parametrize("param", ["Invalid", ["a", "b", "c"], [1, "a"]])
def test_div_invalid_arguments(param):
    with pytest.raises(InvalidArgumentError):
        c = Calculator()
        c.div(*param)


@pytest.mark.parametrize("structure", [[], (), {}, None, (1, 2), [1, 2]])
def test_div_with_structures(structure):
    with pytest.raises(InvalidArgumentError):
        c = Calculator()
        c.div(structure)
