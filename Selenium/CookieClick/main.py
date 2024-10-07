from selenium import webdriver
from selenium.webdriver.common.by import By
import time
    
URL : str = "https://orteil.dashnet.org/experiments/cookie/"
TIME_INTERVAL: int = 10
GAME_DURATION: int = 60 * 1
    
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach", value=True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)
    
cookie = driver.find_element(By.ID, value="cookie")
    
  
def check_store() -> None:
        store_items: list = driver.find_elements(By.CSS_SELECTOR, value="#store div")
        for item in store_items[::-1]: 
            if item.get_attribute("class") != "grayed":
                item.click()
                break
    
    
start_time = time.time()
game_start_time = time.time()
    
while True:
        cookie.click()
        current_time = time.time()
    
        if current_time - start_time >= TIME_INTERVAL: 
            start_time = current_time
            check_store()
    
        if current_time - game_start_time >= GAME_DURATION: 
            print(f"cookies/second:  {driver.find_element(By.ID, value="cps").text}")
            driver.quit()
            break
    
        time.sleep(0.1) 