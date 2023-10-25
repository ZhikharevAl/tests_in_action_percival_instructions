from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://localhost:8000/")

    # Проверяем, что страница содержит текст "FastAPI"
    assert "FastAPI" in page.content()
    print("Test your FastAPI endpoints")
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
