# page.goto() = “open this URL in the current tab."
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

# To write any beginner-level Playwright test, you mainly need:

# page.goto("url") → open a page

# page.click("selector") → click something

# page.fill("selector", "text") → type into an input

# Playwright also waits automatically until the element is ready — which is why you rarely write sleeps.