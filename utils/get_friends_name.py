from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def get_friends_name(driver):
    friends = set()
    friends_container = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div")

    friends_divs = friends_container.find_elements(By.XPATH, "./div")
    for friend in friends_divs:
        try:
            name_element = WebDriverWait(friend, 1).until(
                EC.presence_of_element_located((By.XPATH, ".//a/div[1]/div[2]/div[1]/div/div/div[1]/span/span/span"))
            )
            friends.add(name_element.text.strip())
        except:
            continue

    return friends