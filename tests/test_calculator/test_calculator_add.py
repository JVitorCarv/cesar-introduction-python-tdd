from src.calculator import Calculator, InvalidArgumentError
import pytest


@pytest.mark.parametrize("nums, exp_res", [([1, 2, 3], 6), ([2, 6, 2, 5, 0], 15), ([1], 1)])
def test_add_multiple_arguments(nums, exp_res):
    c = Calculator()
    res = c.add(*nums)
    assert res == exp_res


def test_add_no_argument():
    c = Calculator()
    res = c.add()
    assert res == 0


@pytest.mark.parametrize("param", ["Invalid", ["a", "b", "c"], [1, "a"]])
def test_add_invalid_arguments(param):
    with pytest.raises(InvalidArgumentError):
        c = Calculator()
        c.add(*param)


@pytest.mark.parametrize("structure", [[], (), {}, None, (1, 2), [1, 2]])
def test_add_with_structures(structure):
    with pytest.raises(InvalidArgumentError):
        c = Calculator()
        c.add(structure)
