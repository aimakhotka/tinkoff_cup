import argparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# создание парсера аргументов
parser = argparse.ArgumentParser(description='Run PWA test with specified URL')
parser.add_argument('url', type=str, help='URL to test')
args = parser.parse_args()

# настройки Chrome для эмуляции PWA
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--enable-features=NetworkServiceInProcess")

# создание экземпляра драйвера
driver = webdriver.Chrome(options=chrome_options)

# переход на страницу
driver.get(args.url)

# выключение интернета
driver.set_network_conditions(offline=True)

# проверка отображения страницы "Интернет не доступен"
try:
    error_message_locator = (By.XPATH, "//div[contains(text(), 'Интернет не доступен')]")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(error_message_locator))
except:
    print("Test FAILED: error message not found")
    driver.quit()
    exit()

# включение интернета и обновление страницы
driver.set_network_conditions(offline=False)
driver.refresh()

# проверка отображения страницы после включения интернета
try:
    logo_locator = (By.XPATH, "//img[@alt='Тинькофф Банк']")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(logo_locator))
except:
    print("Test FAILED: page not loaded after turning on the internet")
    driver.quit()
    exit()

# закрытие браузера
driver.quit()

print("Test OK")