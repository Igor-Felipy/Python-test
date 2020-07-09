from selenium import webdriver

driver = webdriver.Chrome('Python-test/aprendendo_automaitzacao_testes/chromedriver')
driver.get('https://www.python.org/')
driver.find_element_by_css_selector('#id-search-field').send_keys("python")
driver.find_element_by_css_selector('#submit').click()
driver.quit()
