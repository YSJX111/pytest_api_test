# 接口自动化测试项目

## 项目简介
这是一个基于 Python + pytest + requests 的接口自动化测试项目，用于测试 JSONPlaceholder 假数据 API。

## 测试覆盖
- GET 请求：获取所有帖子、获取单个帖子
- POST 请求：创建新帖子
- PUT 请求：更新帖子
- DELETE 请求：删除帖子

## 技术栈
- Python 3.8
- pytest 测试框架
- requests 库

## 如何运行
1. 安装依赖：`pip install pytest requests`
2. 运行测试：`pytest test_api_basic.py -v`

## 测试结果
所有测试均通过（5/5）