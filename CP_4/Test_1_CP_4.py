import pytest
@pytest.mark.parametrize('number', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
def test_is_even(number):
    result = number % 2 == 0
    assert result == is_even(number)

def is_even(number):
    if number % 2 == 0:
        return True
