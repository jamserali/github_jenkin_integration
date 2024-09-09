import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def chrome_options():
    # Set up Chrome options
    chrome_option = Options()
    chrome_option.add_argument("--disable-notifications")
    chrome_option.add_argument("--disable-popup-blocking")
    chrome_option.add_argument("--disable-infobars")
    chrome_option.add_argument("--start-maximized")

    # You can also set preferences to disable pop-ups
    prefs = {
        "profile.default_content_setting_values.notifications": 2,  # 2 = Block
        "profile.default_content_setting_values.popups": 2,  # 2 = Block
    }
    chrome_option.add_experimental_option("prefs", prefs)
    return chrome_option


@pytest.fixture(scope='class')
def setup(request):
    # driver = webdriver.Chrome(executable_path=ChromeDriverManager()).install()
    driver = webdriver.Chrome(options=chrome_options())

    driver.get("https://www.yatra.com/")
    request.cls.driver = driver
    driver.maximize_window()
    # Ensure the page is fully loaded
    wait = WebDriverWait(driver, 20)
    wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")

    request.cls.wait = wait
    yield
    driver.close()
