import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")
    parser.addoption('--user_language', action='store', default='en',
                     help="Choose language: en, fr, etc.")

@pytest.fixture(scope="session")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("user_language")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        options = FirefoxOptions()  # Создаем объект FirefoxOptions
        options.set_preference("intl.accept_languages", user_language)  # Устанавливаем язык
        browser = webdriver.Firefox(options=options)  # Передаем options вместо firefox_profile
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser
    print("\nquit browser..")
    browser.quit()