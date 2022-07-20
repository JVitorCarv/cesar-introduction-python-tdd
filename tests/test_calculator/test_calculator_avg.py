from src.calculator import Calculator, InvalidArgumentError
import pytest


@pytest.mark.parametrize("nums, exp_res", [([1, 2, 3], 2), ([2, 2], 2), ([7, 8, 7, 8], 7.5), (7, 7), (0, 0)])
def test_avg_with_multiple_arguments(nums, exp_res):
    c = Calculator()
    if type(nums) is list:
        res = c.avg(*nums)
    else:
        res = c.avg(nums)
    assert res == exp_res


def test_avg_with_no_argument():
    c = Calculator()
    res = c.avg()
    assert res == 0


@pytest.mark.parametrize("param", ["Invalid", ["a", "b", "c"], [1, "a"]])
def test_avg_invalid_arguments(param):
    with pytest.raises(InvalidArgumentError):
        c = Calculator()
        c.avg(*param)


@pytest.mark.parametrize("structure", [[], (), {}, None, (1, 2), [1, 2]])
def test_avg_with_structures(structure):
    with pytest.raises(InvalidArgumentError):
        c = Calculator()
        c.avg(structure)
