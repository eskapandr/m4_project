from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions

# для корректного отображения кириллицы в параметризаторах
def pytest_make_parametrize_id(config, val): return repr(val)


# добавляем параметр запуска тестов в командной строке(чем запускать, хромом или фаерфоксом) По умолчанию хром
def pytest_addoption(parser):
    # parser.addoption('--browser_name', action='store', default=None, help="Choose browser: chrome or firefox")
    # Можно задать значение параметра по умолчанию,
    # чтобы в командной строке не обязательно было указывать параметр --browser_name, например, так:
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser language, e.g. --language=сhrome")
    parser.addoption('--language', action='store', default="en",
                     help="Choose browser language, e.g. --language=ru")


# Запуск браузера(для каждой функции)
@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("--browser_name")
    language = request.config.getoption("--language")

    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option(
            "prefs", {"intl.accept_languages": language}
        )
        browser = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        options = FirefoxOptions()
        options.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(options=options)

    else:
        raise pytest.UsageError("Browser should be chrome or firefox")

    yield browser
    browser.quit()