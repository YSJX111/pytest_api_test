import pytest

@pytest.fixture
def sample_list():
    """返回一个测试用的列表"""
    return [10, 20, 30, 40, 50]

def test_list_length(sample_list):
    assert len(sample_list) == 5

def test_list_sum(sample_list):
    assert sum(sample_list) == 150

def test_first_element(sample_list):
    assert sample_list[0] == 10