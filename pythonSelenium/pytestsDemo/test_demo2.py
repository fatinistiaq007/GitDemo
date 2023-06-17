import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    msg = "Hello"
    assert msg == "Hi", "Test Failed because strings do not match."


def test_SecondCreditCardProgram():
    a = 4
    b = 6
    assert a + 2 == b, "Addition match"



