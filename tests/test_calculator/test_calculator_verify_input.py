from src.calculator import Calculator, InvalidArgumentError
import pytest


@pytest.mark.parametrize("param", ["Invalid", ["a", "b", "c"], [1, "a"]])
def test_verify_input_invalid_arguments(param):
    with pytest.raises(InvalidArgumentError):
        c = Calculator()
        c.verify_input(*param)


@pytest.mark.parametrize("structure", [[], (), {}, None, (1, 2), [1, 2]])
def test_verify_input_with_structures(structure):
    with pytest.raises(InvalidArgumentError):
        c = Calculator()
        c.verify_input(structure)
