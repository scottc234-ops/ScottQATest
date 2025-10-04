from selenium import webdriver driver = webdriver.Chrome() driver.get(‘http://automationpractice.com’) assert ‘My Store’ in driver.title driver.quit()
