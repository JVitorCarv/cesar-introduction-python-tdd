from src.incrementer import *
import pytest


@pytest.mark.parametrize("num, exp_res", [(2, 3), (6, 7), (9, 10)])
def test_with_int(num, exp_res):
    i = Incrementer()
    res = i.inc(num)
    assert exp_res == res


@pytest.mark.parametrize("value", [1.2, 4.2, (-1.2), (-3)])
def test_with_non_natural_numbers(value):
    i = Incrementer()
    with pytest.raises(IncError):
        i.inc(value)


@pytest.mark.parametrize("word", ["Word", "Hello"])
def test_with_strings(word):
    i = Incrementer()
    with pytest.raises(IncError):
        i.inc(word)


@pytest.mark.parametrize("values, exp_res", [([1, 2, 3], [2, 3, 4])])
def test_with_lists(values, exp_res):
    i = Incrementer()
    i.inc(values)
    assert values == exp_res


@pytest.mark.parametrize("values", [([1, -1, "String", 2.3])])
def test_with_wrong_lists(values):
    i = Incrementer()
    with pytest.raises(IncError):
        i.inc(values)
