
from playwright.sync_api import Page


def test_has_content(page: Page):
    page.goto("http://localhost:8000/")

    content = page.inner_text("body > pre")

    assert "FastAPI" in content, f"{content} should contain 'FastAPI'"
