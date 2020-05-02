from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path=r'./chromedriver')
driver.get('http://54.144.35.65/wp-login.php?redirect_to=http%3A%2F%2F54.144.35.65%2Fwp-admin%2F&reauth=1')
time.sleep(5)
#//*[@id="user_login"] nome de usuario
#//*[@id="user_pass"] senha
#//*[@id="wp-submit"] botao de login
#<input type="submit" name="wp-submit" id="wp-submit" class="button button-primary button-large" value="Acessar">
#/html/body/div[1]/form/p[3]/input[1]

preencher_usuario = driver.find_element_by_xpath('//*[@id="user_login"]')
preencher_usuario.click()
time.sleep(3)
preencher_usuario.send_keys('pifam')
preencher_senha = driver.find_element_by_xpath('//*[@id="user_pass"]')
preencher_senha.click()
time.sleep(3)
preencher_senha.send_keys('')
botao_ir = driver.find_element_by_xpath('/html/body/div[1]/form/p[3]/input[1]')
botao_ir.click()