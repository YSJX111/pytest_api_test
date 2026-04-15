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