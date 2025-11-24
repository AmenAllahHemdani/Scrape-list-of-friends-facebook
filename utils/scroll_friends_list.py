from selenium.webdriver.common.by import By
import time

def scroll(driver, scroll_div):

    last_height = 0
    stagnant_loops = 0

    while True:
        driver.execute_script("arguments[0].scrollTop += 500", scroll_div)
        time.sleep(1)
        new_height = driver.execute_script("return arguments[0].scrollHeight", scroll_div)

        if new_height == last_height:
            stagnant_loops += 1
            if stagnant_loops >= 5:
                break
        else:
            stagnant_loops = 0
        last_height = new_height
    
    return driver