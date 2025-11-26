# from playwright.sync_api import page

# def test_google_search(page):
#     page.goto("https://google.com")
#     page.get_by_role("textbox").fill("playwright test")
#     assert "Google" in page.title()

from playwright.sync_api import sync_playwright

def test_google_search():
    with sync_playwright() as p:  
        #sync_playwright() → starts the Playwright engine for Python
        # with ... as p: → ensures that Playwright will automatically clean up (close processes) when the block ends.
        # p → is just a variable that gives you access to all browser types (chromium, firefox, webkit).
        
        browser = p.chromium.launch(headless=False)  # Open Chrome  
        #headless=False → makes the browser visible
        page = browser.new_page()
        page.goto("https://google.com")
        page.get_by_role("textbox").fill("playwright test")
        assert "Google" in page.title()
        browser.close()  #browser.close() → cleanly closes the browser
