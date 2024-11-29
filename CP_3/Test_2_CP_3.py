import pytest


def save_string_in_file(file_path, string):
    with open(file_path, 'w') as f:
        f.write(string)


@pytest.fixture
def temp_file(tmp_path):
    file_path = tmp_path / "test_file.txt"
    return file_path


def test_save_string():
    save_string_in_file('/Users/li6ri9ka/PycharmProjects/CheckPoint_3/src/file.txt', 'qwerty')

    with open('file.txt', 'r') as f:
        assert f.read() == 'qwerty'

    save_string_in_file('/Users/li6ri9ka/PycharmProjects/CheckPoint_3/src/file.txt', 'ytrewq')
    with open('file.txt', 'r') as f:
        assert f.read() == 'ytrewq'

