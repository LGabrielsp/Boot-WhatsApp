from selenium import webdriver
import time

class WhatsappBot:
    def _init_(self):
        self.mensagem= "Bom dia, tudo de bom hoje"
        self.grupos = ["Casa", "Testes"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang-pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def EnviarMensagem(self):
        # <span dir="auto" title="Casa" class="ggj6brxn gfz4du6o r7fjleex g0rxnol2 lhj4utae le5p0ye3 l7jjieqr i0jNr">Casa</span>
        # <div tabindex="-1" class="p3_M1">
        # <span data-icon="send" class="">
        self.driver.get('https://web.whatsapp.com/')
        time.spleep(30)
        for grupo in self.grupos:
            grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
            time.spleep(3)
            grupo.click()
            chat_box = self.driver.find_element_by_class_name('_p3_M1')
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element_y_xpath("//span[@daa-icon='send']")
            time.sleep(3)
            botao_enviar.click()
            time.sleep(3)

bot = WhatsappBot()
bot.EnviarMensagens()

                
