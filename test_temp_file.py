import pytest
import tempfile
import os


@pytest.fixture
def temp_file():
    """创建一个临时文件，里面写入一些内容，测试结束后自动删除"""
    # 创建临时文件（“在系统临时文件夹里创建一个临时文件，以‘写入’模式打开，并且不要自动删除它。把这个文件的对象赋值给变量 f。”）
    f = tempfile.NamedTemporaryFile(mode='w', delete=False)
    f.write("Hello, pytest!")
    f.close()
    print(f"临时文件路径是：{f.name}")

    # 把文件路径交给测试函数
    yield f.name

    # 测试结束后，删除文件
    os.unlink(f.name)


def test_read_temp_file(temp_file):
    """测试：读取临时文件的内容"""
    with open(temp_file, 'r') as f:
        content = f.read()
    assert content == "Hello, pytest!"


def test_file_exists(temp_file):
    """测试：文件确实存在"""
    assert os.path.exists(temp_file) is True