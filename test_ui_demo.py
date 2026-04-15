import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()


def test_example_search(page):
    # 访问 example.com（一个安全的测试网站）
    page.goto("https://www.example.com")

    # 打印页面标题
    print("页面标题是：", page.title())

    # 断言页面标题包含 "Example"
    assert "Example" in page.title()

    # 暂停2秒，让你看到结果
    page.wait_for_timeout(2000)


def test_example_links(page):
    """测试：点击链接（处理新标签页）"""
    # 访问百度
    page.goto("https://www.baidu.com")
    page.wait_for_timeout(2000)

    # 监听新标签页的出现
    with page.context.expect_page() as new_page_info:
        page.click("text=新闻")

    # 切换到新标签页
    new_page = new_page_info.value
    new_page.wait_for_timeout(2000)

    # 断言新页面的标题包含"新闻"
    assert "新闻" in new_page.title()
    print("新页面标题是：", new_page.title())


def test_example_screenshot(page):
    """测试：截图功能"""
    page.goto("https://www.example.com")

    # 截取整个页面并保存
    page.screenshot(path="example.png")
    print("截图已保存为 example.png")

    # 断言截图文件已创建（简单验证）
    import os
    assert os.path.exists("example.png")