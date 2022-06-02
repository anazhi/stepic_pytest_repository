import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose lenguage en,ru,fr")



@pytest.fixture(scope="function")
def browser(request):
    options = webdriver.ChromeOptions()
    language = request.config.getoption("language")
    browser = None
    if language == "en":
        options.add_experimental_option('prefs', {'intl.accept_languages': 'en'})
        print("\nstart chrome browser for test on english..")
        browser = webdriver.Chrome(options = options)
    elif language == "ru":
        options.add_experimental_option('prefs', {'intl.accept_languages': 'ru'})
        print("\nstart chrome browser for test on russian..")
        browser = webdriver.Chrome(options = options)
    elif language == "fr":
        options.add_experimental_option('prefs', {'intl.accept_languages': 'fr'})
        print("\nstart chrome browser for test on french..")
        browser = webdriver.Chrome(options = options)
    else:
        raise pytest.UsageError("--language should be one of them: en,ru,fr")
    yield browser
    print("\nquit browser..")
    browser.quit()

