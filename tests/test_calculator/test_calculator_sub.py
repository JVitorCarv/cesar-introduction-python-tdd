from src.calculator import Calculator, InvalidArgumentError
import pytest


@pytest.mark.parametrize("nums, exp_res", [([1, 2, 3], -4), ([2, 6, 2, 5], -11), ([1], 1), ([0], 0)])
def test_sub_with_multiple_arguments(nums, exp_res):
    c = Calculator()
    res = c.sub(*nums)
    assert res == exp_res


def test_sub_no_argument():
    c = Calculator()
    res = c.sub()
    assert res == 0


@pytest.mark.parametrize("param", ["Invalid", ["a", "b", "c"], [1, "a"]])
def test_verify_sub_invalid_arguments(param):
    with pytest.raises(InvalidArgumentError):
        c = Calculator()
        c.sub(*param)


@pytest.mark.parametrize("structure", [[], (), {}, None, (1, 2), [1, 2]])
def test_verify_sub_with_structures(structure):
    with pytest.raises(InvalidArgumentError):
        c = Calculator()
        c.sub(structure)
