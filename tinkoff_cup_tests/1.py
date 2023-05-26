from selenium import webdriver
from dotenv import load_dotenv
import os

load_dotenv()


def test_200():
    options_G = webdriver.ChromeOptions()
    port = os.getenv('PORT3')
    url = os.getenv('URL')
    driver = webdriver.Remote(
        command_executor=f'http://localhost:{port}',
        options=options_G
    )

    driver.get(url)

    driver.quit()