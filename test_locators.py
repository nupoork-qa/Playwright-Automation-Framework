from playwright.sync_api import Page

def test_playwrightBasics(playwright):
    browser = playwright.chromium.launch(headless = False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://support.saucelabs.com/s/login/?language=en_US")
def test_playwrightShortcut(page:Page):
    page.goto("https://support.saucelabs.com/s/login/?language=en_US")

def test_coreLocators(page:Page):
    page.goto("https://support.saucelabs.com/s/login/?language=en_US")
    page.get_by_label("Username").fill("nupoor")
    page.get_by_label("Password").fill("abc")
    
        