from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")

# price_dollar = driver.find_element(By.CLASS_NAME, value='a-price-whole')
# price_cents = driver.find_element(By.CLASS_NAME, value='a-price-fraction')
#
# print(f'The price is {price_dollar.text}.{price_cents.text}')

# input_ph = driver.find_element(By.NAME, value='q')
# #print(input_ph.tag_name)
# #lub
# #print(input_ph.get_attribute("placeholder"))
#
# button = driver.find_element(By.ID, value='submit')
# # print(button.size)
#
# doc_link = driver.find_element(By.CSS_SELECTOR, value='.documentation-widget a')
# print(doc_link.text)

# bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

web_dates = driver.find_elements(By.CSS_SELECTOR, value='.menu li time')
dates = []
for web_date in web_dates:
    dates.append(web_date.get_attribute('datetime'))

five_dates = dates[5:]

web_events = driver.find_elements(By.CSS_SELECTOR, value='.shrubbery .menu li a')
events = []
for web_event in web_events:
    events.append(web_event.text)

five_events = events[5:10]
#print(five_events)

dat_event_dic = {}
for i in range(len(five_events)):
    dat_event_dic[f'{five_dates[i].split('T')[0]}'] = f'{five_events[i]}'
    

print(dat_event_dic)
















driver.close()
