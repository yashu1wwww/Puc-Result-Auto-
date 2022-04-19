from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://karresults.nic.in/indexpuc_2021.asp")


input=driver.find_element_by_xpath('//*[@id="reg"]')
input.send_keys('923123')

button=driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/form/button')
button.click()


