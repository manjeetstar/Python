import pytest

def test_test1():
    assert (2 + 3) == 5

def test_test2():
    assert [1, 2, 3] == [1, 2, 3]
    assert 1 in [1, 2, 3], "Item not present in the list"

def test_exception_message():
    with pytest.raises(ZeroDivisionError) as e1:
        10 / 0  # type: ignore

    assert (str(e1.value)) == "division by zero"
