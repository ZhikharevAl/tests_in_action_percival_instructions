from playwright.sync_api import Page, sync_playwright
import pytest


class TestNewVisitor:
    @pytest.fixture(scope="class")
    def browser_page(self):
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            yield page
            page.close()
            browser.close()

    def test_has_content(self, browser_page):
        page = browser_page
        page.goto("http://localhost:8000/")

        content = page.inner_text("body > pre")

        assert "To-Do" in content, f"{content} should contain 'To-Do'"
