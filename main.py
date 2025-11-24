from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import os


from utils.save_data import save_data
from utils.get_friends_name import get_friends_name
from utils.scroll_friends_list import scroll


temp_profile = f"/tmp/chrome_profile_{os.getpid()}"
options = webdriver.ChromeOptions()
options.add_argument(f"--user-data-dir={temp_profile}")
options.add_argument("--no-first-run")
options.add_argument("--disable-notifications")
options.add_argument("--disable-infobars")
options.add_argument("--disable-web-security")
options.add_argument("--disable-gpu") 
options.add_argument("--window-size=1400,900")


try:
    driver = webdriver.Chrome(options=options)
    
    driver.get("https://www.facebook.com/login")
    print("Facebook login page loaded!")
    
    print("\nMANUAL LOGIN COUNTDOWN: 30 SECONDS")
    
    for i in range(30, 0, -1):
        print(f"   {i} seconds remaining...", end='\r')
        time.sleep(1)

    print("\nLOGIN WINDOW CLOSED - Starting auto-scroll!")
    
    driver.get("https://www.facebook.com/friends/list")
    print("Loading friends page...")
    time.sleep(2)
    
    print("Scrolling to load ALL friends")

    scroll_div = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[2]")

    driver = scroll(driver, scroll_div)

    driver.execute_script("arguments[0].scrollTop = 0", scroll_div)
    time.sleep(2)

    friends = get_friends_name(driver)

    print("Total friends collected:", len(friends))

        
    save_data(friends)


except Exception as e:
    print("error : ", e)
