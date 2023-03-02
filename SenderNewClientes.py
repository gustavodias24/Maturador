from selenium.webdriver.common.by import By
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
import os
from undetected_chromedriver import Chrome, options
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, NoAlertPresentException, \
    ElementClickInterceptedException
from colorama import Fore, Style
from random import randint
from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from alright import WhatsApp
from random import shuffle
import pyperclip


class BotStart:

    def __init__(self, nav):
        self.nav = nav

    def rpc(self, s):
        for sy in ["+", "-", "estádigitando…", " "]:
            s = s.replace(sy, "")
        return s

    def get_hora(self, tempo):
        if 0 <= tempo <= 4:
            buceta = "Boa noite"
        elif 5 <= tempo <= 12:
            buceta = "Bom dia"
        elif 13 <= tempo <= 17:
            buceta = "Boa tarde"
        elif tempo > 17:
            buceta = "Boa noite"
        else:
            buceta = "Olá tudo bem?"
        return buceta

    def findXpath(self, xpath, time=False, seconds=2):

        tempo = seconds

        while True:
            try:
                return self.nav.find_element(By.XPATH, xpath)
            except NoSuchElementException or StaleElementReferenceException:
                if time:
                    if tempo <= 0:
                        return False
                    tempo -= 1
                    sleep(2)

    def selectFala(self):
        tardeOuNoite = self.get_hora(int(str(datetime.now().time()).split(":")[0]))
        # Divulgar venda Inscritos

        text1 = f"""💬 Oi! {tardeOuNoite},
Estamos aqui para ajudar seu conteúdo na internet a brilhar. Quer saber mais sobre nossos serviços de divulgação? 🤔

Acesse o nosso site👇
https://compartilhatube.net/
O nosso aplicativo de engajamento rápido no YouTube é GRÁTIS 🤳 ➡️  https://play.google.com/store/apps/details?id=br.com.internet.ganhatube

Depoimento de clientes satisfeitos 🗣️👉 compartilhatube.net/depoimento
         """

        text2 = f"""
        {tardeOuNoite}🚀 
Quer aumentar sua presença online e alcançar mais público? Nós temos a solução ideal para você! 💡 Conheça nossos serviços de divulgação de conteúdo na internet. 😎 Tem interesse em saber mais? 🤔
Acesse o nosso site👇
https://compartilhatube.net/

O nosso aplicativo de engajamento rápido no YouTube é GRÁTIS 🤳 ➡️  https://play.google.com/store/apps/details?id=br.com.internet.ganhatube

Depoimento de clientes satisfeitos 🗣️👉 compartilhatube.net/depoimento
        """

        text3 = f"""{tardeOuNoite}
💻 Seu conteúdo na internet merece destaque! Com nossa equipe especializada, alcançamos resultados eficazes e garantimos seu sucesso online. Tem interesse em conhecer mais? 🤔
Acesse o nosso site👇
https://compartilhatube.net/

O nosso aplicativo de engajamento rápido no YouTube é GRÁTIS 🤳 ➡️  https://play.google.com/store/apps/details?id=br.com.internet.ganhatube

Depoimento de clientes satisfeitos 🗣️👉 compartilhatube.net/depoimento
"""

        text4 = f"""🤗 Oi! {tardeOuNoite}, 
Estamos aqui para transformar a presença do seu conteúdo na internet. Quer aumentar seu engajamento e visibilidade online? 😎 Conheça nossos serviços agora mesmo! Tem interesse em saber mais? 🤔
Acesse o nosso site👇
https://compartilhatube.net/

O nosso aplicativo de engajamento rápido no YouTube é GRÁTIS 🤳 ➡️  https://play.google.com/store/apps/details?id=br.com.internet.ganhatube

Depoimento de clientes satisfeitos 🗣️👉 compartilhatube.net/depoimento
"""

        text5 = f"""{tardeOuNoite}
🔥 Seu conteúdo na internet precisa de mais visibilidade? Nós temos a solução perfeita! Com nossos serviços de divulgação, alcançamos resultados eficientes e garantimos seu sucesso online.😎 Tem interesse em saber mais? 🤔
Acesse o nosso site👇
https://compartilhatube.net/

O nosso aplicativo de engajamento rápido no YouTube é GRÁTIS 🤳 ➡️  https://play.google.com/store/apps/details?id=br.com.internet.ganhatube

Depoimento de clientes satisfeitos 🗣️👉 compartilhatube.net/depoimento
"""

        text6 = f"""{tardeOuNoite}💡
Quer aprimorar a imagem do seu conteúdo na internet? Nós temos a solução ideal para você! Com nossa equipe especializada, aumentamos seu engajamento e visibilidade online. Tem interesse em saber mais? 🤔
Acesse o nosso site👇
https://compartilhatube.net/

O nosso aplicativo de engajamento rápido no YouTube é GRÁTIS 🤳 ➡️  https://play.google.com/store/apps/details?id=br.com.internet.ganhatube

Depoimento de clientes satisfeitos 🗣️👉 compartilhatube.net/depoimento
"""

        text7 = f"""Olá {tardeOuNoite}🤗!
Nós da equipe de divulgação de conteúdo na internet estamos aqui para transformar a presença do seu conteúdo online. Quer aumentar seu sucesso e alcançar mais público? 😎 Conheça nossos serviços agora mesmo! Tem interesse em saber mais? 🤔
Acesse o nosso site👇
https://compartilhatube.net/

O nosso aplicativo de engajamento rápido no YouTube é GRÁTIS 🤳 ➡️  https://play.google.com/store/apps/details?id=br.com.internet.ganhatube

Depoimento de clientes satisfeitos 🗣️👉 compartilhatube.net/depoimento
"""

        text8 = f"""{tardeOuNoite} 💻
Quer destacar o seu conteúdo na internet? Nós temos a solução perfeita para você! Com nossos serviços de divulgação, garantimos resultados eficazes e aprimoramos sua imagem digital. Tem interesse em saber mais? 🤔
Acesse o nosso site👇
https://compartilhatube.net/

O nosso aplicativo de engajamento rápido no YouTube é GRÁTIS 🤳 ➡️  https://play.google.com/store/apps/details?id=br.com.internet.ganhatube

Depoimento de clientes satisfeitos 🗣️👉 compartilhatube.net/depoimento
"""

        text9 = f"""{tardeOuNoite} 🚀
Está procurando uma forma de aumentar a presença do seu conteúdo na internet? Nós temos a solução ideal para você! Com nossa equipe especializada, alcançamos resultados eficientes e garantimos seu sucesso online. Tem interesse em saber mais? 🤔
Acesse o nosso site👇
https://compartilhatube.net/

O nosso aplicativo de engajamento rápido no YouTube é GRÁTIS 🤳 ➡️  https://play.google.com/store/apps/details?id=br.com.internet.ganhatube

Depoimento de clientes satisfeitos 🗣️👉 compartilhatube.net/depoimento
"""

        text10 = f"""🔥 {tardeOuNoite},
Torne-se um influenciador de sucesso no YouTube🎥 com a ajuda de nossos inscritos reais e engajados. 60 dias de reposição garantidos. Pergunte sobre preço. 🚀📈
Acesse o nosso site👇
https://compartilhatube.net/

O nosso aplicativo de engajamento rápido no YouTube é GRÁTIS 🤳 ➡️  https://play.google.com/store/apps/details?id=br.com.internet.ganhatube

Depoimento de clientes satisfeitos 🗣️👉 compartilhatube.net/depoimento
"""

        msg2 = """
*Se os links não tiver funcionando você pode:*
( 1 ) Copiar a mensagem e mandar de volta para mim e
( 2 ) Fechar e abrir a nossa conversa        
                """
        return [[text1, text2, text3, text4, text5, text6, text7, text8, text9, text10][randint(0, 9)], msg2]

    def sendEmoji(self, text):
        elem = self.findXpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
        try:
            act = ActionChains(self.nav)
            pyperclip.copy(text)
            elem.click()
            act.key_down(Keys.CONTROL).key_down("v").key_up(Keys.CONTROL).perform()
            elem.send_keys(Keys.ENTER)
        except ElementClickInterceptedException:
            self.senderMsg(text)

    def senderMsg(self, numero):
        try:
            whats = WhatsApp(browser=self.nav)

            print(Fore.GREEN + "Enviando mensagens...")

            falaBot = self.selectFala()

            whats.find_user(numero)
            self.sendEmoji(falaBot[0])
            sleep(2.5)
            whats.send_message(falaBot[1])
            sleep(randint(20, 35))

        except:
            try:
                self.nav.switch_to.alert.send_keys(Keys.ENTER)
                sleep(2.5)
            except NoAlertPresentException:
                sleep(1)

            sleep(10)
            self.senderMsg(numero)

    def startPreAutomatic(self):
        tiverNumero = True

        profiles = os.listdir(
            os.path.join(
                os.getcwd(),
                "profiles"
            )
        )

        shuffle(profiles)

        while tiverNumero:

            for profile in profiles:

                print(Fore.MAGENTA + Style.BRIGHT + "Profile atual: " + profile)

                with (open(f"{os.path.dirname(__file__)}/datas/contacts.txt")) as file:

                    range_sender = 25  # 35

                    allLines = file.read().split("\n")

                    try:
                        allLines.remove('')
                    except ValueError:
                        continue

                    if allLines:
                        conta = allLines[0:range_sender]

                        with open(f"{os.path.dirname(__file__)}/datas/contacts.txt", "w") as fileUpdate:
                            fileUpdate.writelines([l + "\n" for l in allLines[range_sender:]])

                        for line in conta:
                            self.senderMsg(line)

                    else:
                        tiverNumero = False

            print("Esperando para ciclar novamente")
            sleep(300)
