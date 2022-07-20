from src.calculator import *
import pytest


@pytest.mark.parametrize("nums, exp_res", [([1, 2, 3], 6), ([2, 6, 2, 5], 15)])
def test_sum_multiple_arguments(nums, exp_res):
    c = Calculator()
    res = c.add(*nums)
    assert res == exp_res


def test_sum_no_argument():
    c = Calculator()
    res = c.add()
    assert res == 0


@pytest.mark.parametrize("param", ["Invalid", ["a", "b", "c"]])
def test_sum_invalid_argument(param):
    with pytest.raises(InvalidArgumentError):
        c = Calculator()
        res = c.add(*param)

@pytest.mark.parametrize("structure", [[], (), {}, None, (1, 2), [1, 2]])
def test_with_structures(structure):
    with pytest.raises(InvalidArgumentError):
        c = Calculator()
        res = c.add(structure)
