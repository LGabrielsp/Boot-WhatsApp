from selenium import webdriver
import time

class WhatsappBot:
    def __init__(self):
	    # Mensagem que será enviada
        self.mensagem = "Bom dia, tudo de bom hoje"
	    # Grupos para que será enviada
        self.grupos = ["Casa", "Testes"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe', chrome_options=options)

    def EnviarMensagens(self):
        print(self.driver)
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(30)
        for grupo in self.grupos:
            grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
            time.spleep(3)
            grupo.click()
            chat_box = self.driver.find_element_by_class_name('_p3_M1')
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            time.sleep(3)
            botao_enviar.click()
            time.sleep(3)

bot = WhatsappBot()
bot.EnviarMensagens()