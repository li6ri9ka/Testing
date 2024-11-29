import pytest


def calculate_area(length, width):
    S = length * width
    return S

@pytest.mark.parametrize("lenght", [1,2,3,4,5])
@pytest.mark.parametrize("width", [5,4,3,2,1])
def test_area(lenght,width):
    result = lenght * width
    assert result == calculate_area(lenght,width)
