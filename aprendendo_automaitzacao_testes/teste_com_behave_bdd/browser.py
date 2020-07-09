from selenium import webdriver


class Browser(object):
    # Inicia o browser chrome
    driver = webdriver.Chrome('chromedriver')
    # Define o tempo máximo paracarregamento da página
    driver.set_page_load_timeout(30)
    # Maximiza a janela do browser ao ser iniciado
    driver.Maximize_window()

    # Fecha o browser
    def browser_quit(self):
        self.driver.quit()

    # Limpa o browser
    def browser_clear(self):
        self.driver.delete_all_cookies()
        self.driver.execute_script('window.localStorage.clear()')
        self.driver.execute_script('window.sessionStorage.clear()')
        self.driver.refresh()
