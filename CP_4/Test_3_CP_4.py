import pytest

def classify_triangle(a, b, c):
    if a * b == b * c and a * c == c * b and b * c == c * a:
        return 'Равностороний'
    elif a * b == b * c and a*c != c*b:
        return 'Равнобедренный'
    else:
        return 'разностороний'


@pytest.mark.parametrize('a', [5,4,3])
@pytest.mark.parametrize('b', [3,2,5])
@pytest.mark.parametrize('c', [1,2,3])
def test_classify_triangle(a, b, c):
    assert classify_triangle(a, b, c) == classify_triangle(b, c, a)


print(classify_triangle(3,3,3))
