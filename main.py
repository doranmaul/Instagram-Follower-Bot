from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions
import os, time

FB_EMAIL = os.environ["FB_EMAIL"]
FB_PASS = os.environ["FB_PASS"]
SIMILAR_ACCOUNT_URL = "https://www.instagram.com/therock"  # Insert page desired here

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options)
driver.get("https://www.instagram.com")


def find_followers():
    time.sleep(5)
    modal = driver.find_element(By.CSS_SELECTOR, '._aano')
    for i in range(10):
        #In this case we're executing some Javascript, that's what the execute_script() method does.
        #The method can accept the script as well as a HTML element.
        #The modal in this case, becomes the arguments[0] in the script.
        #Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
        time.sleep(2)


def follow():
    all_buttons = driver.find_elements(By.XPATH, "//button[contains(.,'Follow')]")
    for btn in all_buttons:
        try:
            driver.execute_script("arguments[0].click();", btn)
            time.sleep(1)
        except selenium.common.exceptions.ElementClickInterceptedException:
            cancel_button = driver.find_element(By.XPATH, '//button[@class="_a9-- _ap36 _a9_1" and text()="Cancel"]')
            cancel_button.click()


time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[5]/button').click()
time.sleep(2)
fb_email = (driver.find_element(By.XPATH, '//input[@type="text" and @class="inputtext _55r1 inputtext _1kbt inputtext _1kbt" and @name="email"]'))
fb_email.send_keys(FB_EMAIL)
driver.find_element(By.XPATH, '//input[@type="password" and @class="inputtext _55r1 inputtext _1kbt inputtext _1kbt" and @name="pass"]').send_keys(FB_PASS)
fb_email.send_keys(Keys.ENTER)
time.sleep(8)
driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()
time.sleep(2)
driver.get(SIMILAR_ACCOUNT_URL)

time.sleep(5)
driver.find_element(By.XPATH, '//a[@class="x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz _alvs _a6hd"]').click()

for i in range(15):
    follow()
    find_followers()


# The app is kind of glitchy atm, but it still follows everyone as intended












# Old code below

# except selenium.common.exceptions.NoSuchElementException:
#     driver.find_element(By.XPATH,"//div[contains(@class, 'x6s0dn4') and contains(@class, 'x78zum5') and .//svg[contains(@aria-label, 'Close')]]").click()
#     if follow_range < 7:
#         driver.execute_script("arguments[0].click();", btn)
#         follow_range += 1
#     else:
#         fBody = driver.find_element(By.CSS_SELECTOR, value="._aano")
#         driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
#         follow_range = 0
# except selenium.common.exceptions.ElementClickInterceptedException:
#     driver.find_element(By.XPATH, '//button[@class="_a9-- _ap36 _a9_1" and text()="Cancel"]').click()
#     if follow_range < 7:
#         driver.execute_script("arguments[0].click();", btn)
#         follow_range += 1
#     else:
#         fBody = driver.find_element(By.CSS_SELECTOR, value="._aano")
#         driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
#         follow_range = 0

