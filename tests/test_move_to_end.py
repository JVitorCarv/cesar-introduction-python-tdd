from src.move_to_end import move_to_end, NotListError
import pytest


@pytest.mark.parametrize("test_list, exp_res", [([1, 2, 3], [2, 3, 1]), ([4, 5], [5, 4]),
                                                (["Ab", "Bc"], ["Bc", "Ab"]),
                                                (["Ab", "Bc", "Cd"], ["Bc", "Cd", "Ab"]),
                                                ([1, "Abc", 2.2], ["Abc", 2.2, 1])])
def test_with_list_size_above_1(test_list, exp_res):
    move_to_end(test_list)
    assert test_list == exp_res


@pytest.mark.parametrize("test_list, exp_res", [([1], [1]), (["Hello"], ["Hello"])])
def test_with_list_size_equals_1(test_list, exp_res):
    move_to_end(test_list)
    assert test_list == exp_res


@pytest.mark.parametrize("test_list, exp_res", [([], [])])
def test_with_empty_list(test_list, exp_res):
    move_to_end(test_list)
    assert test_list == exp_res


@pytest.mark.parametrize("test_list", [1, "Abc", 2.2])
def test_with_non_list(test_list):
    with pytest.raises(NotListError):
        move_to_end(test_list)
