from selenium import webdriver

#call time to prevent auto close browser
import time
from selenium import webdriver

# import Action chains to click on submenu
from selenium.webdriver.common.action_chains import ActionChains

#load .env file
import os
from dotenv import load_dotenv

load_dotenv()


driver = webdriver.Chrome()

def login(url,username,password):
   driver.get(url)
   driver.find_element("id", "username").send_keys(username)
   driver.find_element("id", "password").send_keys(password)
   driver.find_element("xpath",'//*[@id="userLogin"]/div[4]/div/button').click()
   mainMenu = driver.find_element("xpath",'//*[@id="navbarDropdown"]')
   action = ActionChains(driver)
   action.move_to_element(mainMenu)
   subMenu = driver.find_element("xpath",'//*[@id="navbarSupportedContent"]/ul/li[2]/div/a[1]')
   action.move_to_element(subMenu)
   action.click().perform()
   time.sleep(5000) # Let the user actually see something!
   driver.quit()


login(os.getenv('url'), os.getenv('user_name'), os.getenv('password'))