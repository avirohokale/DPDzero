import pytest
from selenium import webdriver


@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("https://simple-todo-app-gamma.vercel.app/")
    driver.maximize_window()

    return driver





