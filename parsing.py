from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


driver.get("https://univer.kaznu.kz/user/login?ReturnUrl=%2fnews%2fstudent%2f1%2f")


driver.implicitly_wait(10)

inputs = driver.find_elements(By.CLASS_NAME, "text")
inputs[0].send_keys("moldash.alikhan")
inputs[1].send_keys("Alihan7814@")


login_button = driver.find_element(By.XPATH, "//input[@value='Жүйеге кіру']")
login_button.click()


time.sleep(5)


# Закрываем браузер
driver.quit()
