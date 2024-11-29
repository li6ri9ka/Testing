import pytest

def returnLengthString(string):
    return len(string)

@pytest.fixture
def test_string():
    return ['asdasd',
            '',
            ' ',
            '\n\n']

def test_returnLengthString(test_string):
    for string in test_string:
        assert returnLengthString(test_string) == len(string)
