import requests
import pytest
#获取所有帖子
def test_get_all_posts():
    # 发送 GET 请求到 需要调用数据的网址/posts 接口
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    # 断言1：状态码是 200（表示成功）
    assert response.status_code == 200

    # 断言2：返回的数据是一个列表,isinstance 是 Python 内置函数，意思是 “是否是某个类型”。
    data = response.json()
    assert isinstance(data, list)

    # 断言3：列表长度是 100
    assert len(data) == 100

#获取单个帖子
def test_get_single_post():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)

    assert response.status_code == 200

    # 把返回的 JSON 转成字典
    data = response.json()

    # 断言：返回的帖子 id 应该是 1
    assert data["id"] == 1
    assert "title" in data
    assert "body" in data

#创建新帖子
def test_create_post():
    # 要发送的数据
    new_post = {
        "title": "我的测试帖子",
        "body": "这是通过自动化测试创建的内容",
        "userId": 1
    }

    # 发送 POST 请求
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.post(url, json=new_post)

    # 断言1：状态码是 201（Created，表示创建成功）
    assert response.status_code == 201

    # 断言2：返回的数据包含我们发送的标题
    data = response.json()
    assert data["title"] == "我的测试帖子"
    assert data["body"] == "这是通过自动化测试创建的内容"
    assert data["userId"] == 1

    # 断言3：服务器返回了一个新的 id（通常是 101）
    assert "id" in data

#更新帖子
def test_update_post():
    # 要更新的数据
    updated_post = {
        "id": 1,
        "title": "更新后的标题",
        "body": "这是更新后的内容",
        "userId": 1
    }

    # 发送 PUT 请求（完整更新）
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.put(url, json=updated_post)

    # 断言：状态码是 200
    assert response.status_code == 200

    # 断言：返回的数据包含了更新后的内容
    data = response.json()
    assert data["title"] == "更新后的标题"
    assert data["body"] == "这是更新后的内容"

#删除帖子
def test_delete_post():
    # 发送 DELETE 请求
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.delete(url)

    # 断言：状态码是 200（有些API返回204，这里返回200）
    assert response.status_code == 200

    # DELETE 请求通常返回空内容，能成功删除就算通过
    # 如果返回了内容，可以打印看看
    if response.text:
        print("删除返回:", response.json())