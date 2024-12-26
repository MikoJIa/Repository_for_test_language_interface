import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption("--browser_name", action='store', default='chrome',
                     help="Choose browser: Chrome or Firefox")

    parser.addoption("--language", action="store", default=None,
                    help="Choose language: '--language=ru' or '--language=en'")


@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test...")
        option = Options()
        option.add_experimental_option(
            'prefs', {'intl.accept_languages': user_language}
        )
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install(), option=option))
    elif browser_name == 'firefox':
        print("\nstart firefox browser for test...")
        option_firefox = FirefoxOptions()
        option_firefox.set_preference('intl.accept_languages', user_language)
        browser = webdriver.Firefox(options=option_firefox)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser")
    browser.quit()