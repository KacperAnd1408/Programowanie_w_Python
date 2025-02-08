from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com")
driver.maximize_window()

#number_of_articles = driver.find_element(By.CSS_SELECTOR, value='#articlecount a')
#number_of_articles.click()
#all_portals = driver.find_element(By.LINK_TEXT, value='Content portals')
#all_portals.click()
# search = driver.find_element(By.NAME, value="search")
# search.send_keys("Python", Keys.ENTER)

first_name = driver.find_element(By.NAME, value='fName')
last_name = driver.find_element(By.NAME, value='lName')
email = driver.find_element(By.NAME, value='email')

first_name.send_keys("Kacper")
last_name.send_keys("Andrzejewski")
email.send_keys("k.andrzejewski225@gmail.com", Keys.ENTER)
