
def test_playwrightBasic(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://playwright.dev/")   
    
#page.goto() = “open this URL in the current tab."
# Think of page as:
# A tab inside a browser that you can control through code

# A basic Python Playwright test looks like:

# def test_example(page):
#     page.goto("https://example.com")
#     page.click("text=Login")

# Let’s break it gently:

# def test_example(page):
# → Playwright gives you the page object automatically using a fixture.

# page.goto(...)
# → Open the website.

# page.click(...)
# → Interact with something.

