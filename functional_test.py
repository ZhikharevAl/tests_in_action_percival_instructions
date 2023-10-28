
from playwright.sync_api import Page, expect


def test_has_title(page: Page):
    page.goto("http://localhost:8000/")

    content = page.inner_text("body > pre")

    assert "FastAPI" in content
