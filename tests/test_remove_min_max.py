from src.remove_min_max import *
import pytest


@pytest.mark.parametrize("num_list, exp_res", [([1, 2, 3], [2]), ([2.2, 2.1, 3.3], [2.2]),
                                               ([3, 2, 1], [2]), ([1, 1, 1], [1])])
def test_with_list_size_above_3(num_list, exp_res):
    res = remove_min_max(num_list)
    assert res == exp_res


@pytest.mark.parametrize("num_list, exp_res", [([1, 1], [])])
def test_with_list_size_equals_2(num_list, exp_res):
    res = remove_min_max(num_list)
    assert res == exp_res


@pytest.mark.parametrize("num_list, exp_res", [([1], [])])
def test_with_list_size_equals_1(num_list, exp_res):
    res = remove_min_max(num_list)
    assert res == exp_res


@pytest.mark.parametrize("num_list, exp_res", [([], [])])
def test_with_empty_list(num_list, exp_res):
    res = remove_min_max(num_list)
    assert res == exp_res


@pytest.mark.parametrize("not_list", [("String"), (1), (1.1), ((1, 1))])
def test_with_not_list(not_list):
    with pytest.raises(NotListError):
        res = remove_min_max(not_list)


@pytest.mark.parametrize("mixed_list", [([1, "a", "str"]), ["str"]])
def test_with_mixed_list(mixed_list):
    with pytest.raises(NotANumber):
        res = remove_min_max(mixed_list)


