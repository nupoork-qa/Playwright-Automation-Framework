# Playwright Automation Framework (Python) 🐍

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Playwright](https://img.shields.io/badge/Playwright-Latest-green)
![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)

## 📖 What is Playwright?

**Playwright** is an open-source test automation library initially developed by Microsoft. It is designed to enable reliable end-to-end testing for modern web apps.

While popular with Node.js, Playwright offers robust support for **Python**. It operates under the **Apache 2.0 License** and allows you to automate Chromium, Firefox, and WebKit with a single API.

## 🚀 Features of Playwright Automation

Playwright is packed with features to make Python testing faster and more reliable:

* **🌐 Cross-Browser Testing:** Supports Chromium, Firefox, and WebKit (Safari) with a single API.
* **⚡ Auto-Waiting:** The framework waits automatically for elements to be ready (clickable, visible) before performing actions, eliminating flaky `time.sleep()` calls.
* **🐍 Python Native:** integrates seamlessly with **Pytest** for fixtures and assertions.
* **🎭 Headless & Headed Modes:** Run tests in the background (headless) for CI/CD, or visible (headed) for debugging.
* **📱 Mobile & Device Emulation:** Seamlessly emulate real-world devices, screen sizes, and geolocation.
* **📡 Network Interception:** Intercept network activity to mock API responses and control server conditions.
* **🛠 Built-in Test Generator:** Record your user interactions to auto-generate Python code (`playwright codegen`).
* **📸 Visual & Screenshot Testing:** Capture full-page screenshots, element snapshots, and video recordings.
  
## 🌟 Advantages of Playwright

Playwright contributors are highly active, releasing new features monthly. 

* Easy Setup & Configuration:** Installation is fast and straightforward using standard Python package managers.
* Multi-Browser Support:** Supports the generic **Chromium** family (Chrome, Edge), **WebKit** (Safari), and **Firefox** with a single API.
* Versatile Testing Types:** Supports Functional, End-to-End (E2E), and API Testing. It can also integrate with third-party plugins (like `axe-core`) for **Accessibility Testing**.
* Parallel Execution:** Supports simultaneous test execution through **Browser Contexts**, allowing you to run tests across multiple browsers at once to scale up testing speed.
* Multi-Tab & Window Support:** effortlessly handles scenarios that require launching new windows/tabs and returning to the parent window.
* Robust Reporting:** Comes with built-in reporters (List, Dot, Line, JSON, JUnit, and HTML). It also supports third-party integrations like **Allure Report**.
* Powerful Debugging:** Developer-friendly tools include the Playwright Inspector, VSCode Debugger, Browser Developer Tools, and Trace Viewers.
* CI/CD Integration:** easy integration with CI pipelines (Jenkins, GitHub Actions, Azure DevOps) and provides Docker images for containerized testing.

## ⚠️ Limitations

To maintain transparency regarding the tool selection:
* **Legacy Support:** There is **no support for IE11**.
* **Mobile Scope:** Playwright handles mobile *web* emulation excellently, but does **not support Native Mobile Apps**.
* **Community:** While documentation is excellent, the community is newer compared to Selenium, though it is growing rapidly.


## ⚙️ Prerequisites

1.  **Python 3.8+**
2.  **Visual Studio Code** (Recommended, with the Python Extension installed)

## 🛠️ Installation

To set up the project locally, install the Playwright Pytest plugin and the necessary browser binaries:

```bash
# 1. Install Playwright and Pytest
pip install pytest-playwright

# 2. Install the required browsers (Chromium, Firefox, WebKit)
playwright install
